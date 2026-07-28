import csv
import os
from datetime import datetime
from PySide6.QtCore import Signal, QSize, QTimer
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QFileDialog
from Device_controllers.papago_controller import PapagoController
from Device_controllers.tunnel_plc_controller import TunnelPLCController
from Gui.Charts.zoomable_chart import ZoomableChart
from Qt_files.Qt_python.ui_wind_tunnel_config_view import Ui_Form
from Utils.number_validator import FloatValidator, IntValidator


class ConfigurationView(QWidget):
    RETURN_TO_MAIN = Signal()
    SETTINGS_CHANGES = Signal(dict)

    def __init__(self, plc: TunnelPLCController, papago: PapagoController):
        QWidget.__init__(self)
        self.concentric: bool = False
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.data_to_save = {"time": "00:00:00", "Velocity [m/s]": 0.0,
                             "Temp [°C]": 0.0, "pressure [Pa]": 0.0, "frequency [Hz]": 0.0}

        self.configuration_data = { "frequency": 0.0, "velocity": 0.0, "pid": False}

        self.reset_save_file = False
        self.save_timer = QTimer()
        self.save_timer.timeout.connect(self._save_data)
        self.save_file_name = ""
        self.save_file_path = ""
        self.save_count = 0
        self.saving = False
        self.float_validator = FloatValidator(0, 100)
        self.int_validator = IntValidator(1000)

        # Validators
        self.ui.set_velocity_le.setValidator(self.float_validator)
        self.ui.set_frequency_le.setValidator(self.float_validator)

        self.regulation: bool = False

        self.tunnel_plc = plc
        self.papago = papago

        self._init_graphical_changes()
        self._bind_buttons()
        self._bind_emits()

    def _init_graphical_changes(self):
        # charts setup block
        self.chart = ZoomableChart(
            name="",
            x_axis_seconds=600,
            y_axis=(0, 50),
            line_name=["Wind velocity[m/s]", "Wind temperature [°C]"],
            line_count=2
        )

        self.ui.scale_chart.addWidget(self.chart)

    def _bind_buttons(self):
        # saving handling
        self.ui.change_dir_btn.clicked.connect(self._open_dir_dialog)
        self.ui.set_name_btn.clicked.connect(self._set_save_name)

        self.ui.set_velocity_rb.clicked.connect(self._set_velocity_mode)
        self.ui.set_frequency_rb.clicked.connect(self._set_frequency_mode)

        self.ui.set_frequency_le.editingFinished.connect(self._set_frequency_value)
        self.ui.set_velocity_le.editingFinished.connect(self._set_velocity_value)

        self.ui.start_tunnel_btn.clicked.connect(self.start_tunnel)
        self.ui.stop_tunnel_btn.clicked.connect(self.stop_tunnel)

        self.ui.restart_chart_btn.clicked.connect(self.chart.reset_axis)

    def _bind_emits(self):
        self.tunnel_plc.PLC_DATA.connect(self._handle_plc_data)
        self.papago.PAPAGO_DATA.connect(self._handle_papago_data)
        self.tunnel_plc.PLC_CONNECTED.connect(self.set_available)

    # Data allocation block
    def _handle_papago_data(self, papago_data: dict):
        if self.saving:
            self.data_to_save["P temp [°C]"] = papago_data.get("temperature")
            self.data_to_save["P hum [%]"] = papago_data.get("humidity")
            self.data_to_save["A pressure"] = papago_data.get("pressure")

    def _handle_plc_data(self, plc_data: dict):
        self.chart.update_chart([plc_data.get("wind_filtered"), plc_data.get("average_temp")])
        if self.saving:
            self.data_to_save["Velocity [m/s]"] = plc_data.get("wind_filtered")
            self.data_to_save["Temp [°C]"] = plc_data.get("average_temp")
            self.data_to_save["pressure [Pa]"] = plc_data.get("pressure_filtered")
            self.data_to_save["frequency [Hz]"] = plc_data.get("frequency")

    def start_tunnel(self):
        config = self.configuration_data
        self.tunnel_plc.switch_pid(config.get("pid"))
        if not config.get("pid"):
            self.tunnel_plc.set_wind_velocity(config.get("velocity"))
        else:
            self.tunnel_plc.set_engine_frequency(config.get("frequency"))

        self.start_saving()
        self.tunnel_plc.start_engine()

        self.ui.start_tunnel_btn.setEnabled(False)
        self.ui.stop_tunnel_btn.setEnabled(True)

    def stop_tunnel(self):
        self.tunnel_plc.switch_pid(False)
        self.tunnel_plc.set_wind_velocity(0)
        self.tunnel_plc.set_engine_frequency(0)
        self.tunnel_plc.stop_engine()
        self.stop_saving()
        self.ui.start_tunnel_btn.setEnabled(True)
        self.ui.stop_tunnel_btn.setEnabled(False)

    def reset_gui_after_external_stop(self):
        self.stop_saving()
        self.ui.start_tunnel_btn.setEnabled(True)
        self.ui.stop_tunnel_btn.setEnabled(False)

    def set_available(self, state: bool):
        if state is False and self.ui.stop_tunnel_btn.isEnabled():
            self.stop_tunnel()
        self.ui.start_tunnel_btn.setEnabled(state)

    # Setting block
    def _update_configuration(self, key: str, value):
        self.configuration_data[key] = value
        self.SETTINGS_CHANGES.emit(self.configuration_data)

    def _set_velocity_mode(self):
        self._update_configuration("pid", False)

    def _set_velocity_value(self):
        req_velocity = float(self.ui.set_velocity_le.text())
        self._update_configuration("velocity", req_velocity)

    def _set_frequency_mode(self):
        self._update_configuration("pid", True)

    def _set_frequency_value(self):
        req_frequency = float(self.ui.set_frequency_le.text()) if self.ui.set_frequency_le.text() != "" else 0
        self._update_configuration("frequency", req_frequency)

    def enable_setting_velocity(self, concentric: bool):
        self.ui.set_velocity_le.setEnabled(concentric)
        self.ui.set_velocity_rb.setEnabled(concentric)
        self.concentric = concentric
        if not concentric:
            self.deselect_radiobuttons()

    def deselect_radiobuttons(self):
        self.ui.set_velocity_rb.setChecked(False)
        self.ui.set_frequency_rb.setChecked(False)

    # Saving block
    def start_saving(self):
        self.saving = True
        self._get_file_path()
        self.save_count = 0
        self.save_timer.start(1000)
        self.reset_save_file = True

    def stop_saving(self):
        self.saving = False
        self.save_timer.stop()

    def _open_dir_dialog(self):
        options = QFileDialog(self).options()
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder", "", options=options)
        self.ui.dir_path_line.setText(folder_path)

    def _save_data(self):
        save_duration = self.ui.save_timer_le.text()
        if self.ui.save_timer_chb.isChecked() and save_duration != "" and self.save_count >= int(save_duration) - 1:
            self.stop_saving()

        exists = os.path.exists(self.save_file_path)

        time = datetime.now().strftime("%H:%M:%S")[:-5]
        self.data_to_save["time"] = time

        if self.reset_save_file:
            open(self.save_file_path, "w")
            exists = False
            self.reset_save_file = False

        with open(self.save_file_path, 'a', newline="") as f:
            writer = csv.writer(f)
            if not exists:
                writer.writerow(self.data_to_save.keys())
            writer.writerow(self.data_to_save.values())
        self.save_count += 1

    def _set_save_name(self):
        self.save_file_name = self.ui.file_name_le.text()

    def _get_file_path(self):
        file_path = self.ui.dir_path_line.text()
        if file_path == "":
            file_path = os.getcwd()
        if self.save_file_name == "":
            name = "Wind_tunnel_" + datetime.now().strftime("%Y-%m-%d_%H%M")
        else:
            name = self.save_file_name

        file_path += f"/{name}.csv"
        self.save_file_path = file_path
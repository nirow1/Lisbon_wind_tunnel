import csv
import os
from datetime import datetime
from PySide6.QtCore import Signal, QSize, QTimer
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QWidget, QFileDialog

from Device_controllers.papago_controller import PapagoController
from Device_controllers.plc_controller import PLCController
from Qt_files.Qt_python.ui_Configuration_view import Ui_Form
from Utils.number_validator import FloatValidator, IntValidator


class ConfigurationView(QWidget):
    RETURN_TO_MAIN = Signal()
    SETTINGS_CHANGES = Signal(dict)

    def __init__(self, plc: PLCController, papago: PapagoController):
        QWidget.__init__(self)
        self.concentric: bool = False
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.data_to_save = {"time": "00:00:00", "P temp [°C]": 0.0, "P hum [%]": 0.0,"A pressure": 0.0,
                             "Velocity [m/s]": 0.0, "Velocity max-min[m/s]": 0.0,
                             "Temp [°C]": 0.0, "Temp max-min[°C]":0.0,
                             "pressure [Pa]": 0.0, "pressure max-min[Pa]": 0.0,
                             "frequency [Hz]": 0.0}
        self.configuration_data = {"ramp_up": 0, "ramp_down": 0, "run_duration": 0, "frequency": 0.0, "velocity": 0.0, "pid": False, "control": False}
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
        self.ui.ramp_up_le.setValidator(self.int_validator)
        self.ui.ramp_down_le.setValidator(self.int_validator)
        self.ui.run_duration_le.setValidator(self.int_validator)

        self.regulation: bool = False

        self.plc = plc
        self.papago = papago

        self._init_graphical_changes()
        self._bind_buttons()
        self._bind_emits()

    def _init_graphical_changes(self):
        self.ui.change_dir_btn.setIcon(QIcon("./App_data/dir_icon.png"))
        self.ui.change_dir_btn.setIconSize(QSize(54, 30))

        self.ui.ramp_img_lbl.setFixedSize(QSize(500, 250))
        self.ui.ramp_img_lbl.setScaledContents(True)
        self.ui.ramp_img_lbl.setPixmap(QPixmap("./App_data/vykres_rampa.png"))

    def _bind_buttons(self):
        # saving handling

        self.ui.change_dir_btn.clicked.connect(self._open_dir_dialog)
        self.ui.set_name_btn.clicked.connect(self._set_save_name)

        self.ui.ramp_up_btn.clicked.connect(self._set_rump_up)
        self.ui.ramp_down_btn.clicked.connect(self._set_rump_down)
        self.ui.run_duration_btn.clicked.connect(self._set_run_duration)

        self.ui.set_velocity_rb.clicked.connect(self._set_velocity_mode)
        self.ui.set_frequency_rb.clicked.connect(self._set_frequency_mode)

        self.ui.set_frequency_le.editingFinished.connect(self._set_frequency_value)
        self.ui.set_velocity_le.editingFinished.connect(self._set_velocity_value)

        self.ui.ramp_chb.clicked.connect(self._switch_ramp)

    def _bind_emits(self):
        self.plc.PLC_DATA.connect(self._handle_plc_data)
        self.papago.PAPAGO_DATA.connect(self._handle_papago_data)

    # Data allocation block
    def _handle_papago_data(self, papago_data: dict):
        if self.saving:
            self.data_to_save["P temp [°C]"] = papago_data.get("temperature")
            self.data_to_save["P hum [%]"] = papago_data.get("humidity")
            self.data_to_save["A pressure"] = papago_data.get("pressure")

    def _handle_plc_data(self, plc_data: dict):
        if self.saving:
            self.data_to_save["Velocity [m/s]"] = plc_data.get("wind_velocity")
            self.data_to_save["Velocity max-min[m/s]"] = plc_data.get("wind_velocity_maxmin")
            self.data_to_save["Temp [°C]"] = plc_data.get("average_temp")
            self.data_to_save["Temp max-min[°C]"] = plc_data.get("avg_temp_maxmin")
            self.data_to_save["pressure [Pa]"] = plc_data.get("diff_pressure")
            self.data_to_save["pressure max-min[Pa]"] = plc_data.get("pressure_maxmin")
            self.data_to_save["frequency [Hz]"] = plc_data.get("engine_rotations")

    # Setting block
    def _update_configuration(self, key: str, value):
        self.configuration_data[key] = value
        self.SETTINGS_CHANGES.emit(self.configuration_data)

    def _set_velocity_mode(self):
        self.ui.set_velocity_rb.setChecked(True)
        self.ui.set_frequency_rb.setChecked(False)
        self._update_configuration("pid", False)

    def _set_velocity_value(self):
        req_velocity = float(self.ui.set_velocity_le.text())
        self._update_configuration("velocity", req_velocity)

    def _set_frequency_mode(self):
        self.ui.set_velocity_rb.setChecked(False)
        self.ui.set_frequency_rb.setChecked(True)
        self._update_configuration("pid", True)

    def _set_frequency_value(self):
        req_frequency = float(self.ui.set_frequency_le.text())
        self._update_configuration("frequency", req_frequency)

    def _set_rump_up(self):
        ramp_up = 0 if self.ui.ramp_up_le.text() == "" else int(self.ui.ramp_up_le.text())
        self._update_configuration("ramp_up", ramp_up)

    def _set_rump_down(self):
        ramp_down = 0 if self.ui.ramp_down_le.text() == "" else int(self.ui.ramp_down_le.text())
        self._update_configuration("ramp_down", ramp_down)

    def _set_run_duration(self):
        run_dur = 0 if self.ui.run_duration_le.text() == "" else int(self.ui.run_duration_le.text())
        self._update_configuration("run_duration", run_dur)

    def _switch_ramp(self):
        self._update_configuration("control", self.ui.ramp_chb.isChecked())

    def get_configuration(self)->dict:
        return self.configuration_data

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

    def switch_ramp_off(self):
        self.ui.ramp_chb.setChecked(False)
        self._update_configuration("control", False)

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
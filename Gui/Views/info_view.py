from PySide6.QtCore import QSize, Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QFileDialog, QWidget

from Device_controllers.driver_2d_plc_controller import Driver2DPLCController
from Device_controllers.driver_3d_plc_controller import Driver3DPLCController
from Device_controllers.scale_plc_controller import ScalePLCController
from Device_controllers.tlaskan_controller import TlaskanController
from Device_controllers.tunnel_plc_controller import TunnelPLCController
from Gui.Custom_functions.saving_thread import SavingThread
from Qt_files.Qt_python.ui_wind_tunnel_Info_view import Ui_Form
from Utils.number_validator import FloatValidator


class InfoPanel(QWidget):
    STOP_TUNNEL = Signal()

    def __init__(self, tunnel_plc: TunnelPLCController,
                 driver_3d: Driver3DPLCController,
                 driver_2d: Driver2DPLCController,
                 scales: ScalePLCController, 
                 tlaskans: tuple[TlaskanController, TlaskanController],
                 ):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self._average_speed = [0]
        self._req_velocity: float = 0.0

        self.tunnel_plc = tunnel_plc
        self.driver_3d = driver_3d
        self.driver_2d = driver_2d
        self.scales = scales
        self.tlaskans = tlaskans

        self.configuration_data = { "frequency": 0.0, "velocity": 0.0, "pid": False}

        self.save_thread = SavingThread(200)

        self.float_validator = FloatValidator(0, 50)
        self.ui.set_velocity_le.setValidator(self.float_validator)
        self.ui.set_frequency_le.setValidator(self.float_validator)

        self._initial_graphical_changes()
        self._bind_buttons()
        self._bind_emits()

    def _initial_graphical_changes(self):
        self.ui.disconnect_tunnel_btn.hide()
        self.set_buttons_state(False)
        self.ui.change_dir_btn.setIcon(QIcon("./App_data/dir_icon.png"))
        self.ui.change_dir_btn.setIconSize(QSize(54, 30))
        self.ui.stop_saving_btn.setVisible(False)

    def _bind_buttons(self):
        self.ui.connect_tunel_btn.clicked.connect(self._connect_tunnel)
        self.ui.disconnect_tunnel_btn.clicked.connect(self.disconnect_tunnel)

        self.ui.start_tunnel_btn.clicked.connect(self.start_tunnel)
        self.ui.stop_tunnel_btn.clicked.connect(self.stop_tunnel)

        self.ui.set_frequency_le.editingFinished.connect(self._set_frequency_value)
        self.ui.set_velocity_le.editingFinished.connect(self._set_velocity_value)
        self.ui.set_velocity_rb.clicked.connect(lambda: self._set_frequency_mode(False))
        self.ui.set_frequency_rb.clicked.connect(lambda: self._set_frequency_mode(True))

        self.ui.start_saving_btn.clicked.connect(self._start_saving)
        self.ui.stop_saving_btn.clicked.connect(self._stop_saving)
        self.ui.change_dir_btn.clicked.connect(self._open_dir_dialog)
        self.ui.set_name_btn.clicked.connect(lambda: self.save_thread.set_save_file_name(self.ui.file_name_le.text()))
        self.ui.save_timer_chb.clicked.connect(lambda: self.save_thread.activate_timer(self.ui.save_timer_chb.isChecked(), self.ui.save_timer_le.text()))

    def _bind_emits(self):
        self.tunnel_plc.SENSOR_VALUES.connect(self._handle_plc_data)
        self.tunnel_plc.PLC_CONNECTED.connect(self.set_available)
        self.tunnel_plc.PAPAGO_DATA.connect(self._handle_papago_data)
        self.scales.SCALE_DATA.connect(self._handle_scale_data)

    def _handle_plc_data(self, plc_data):
        wind_velocity = plc_data.get("speed")
        frequency = plc_data.get("frequency")
        temp = plc_data.get("average_temp")
        pressure = plc_data.get("pressure_filtered")

        self.ui.wind_velocity_lbl.setText(f"{wind_velocity!s}")
        self.ui.frequency_lbl.setText(f"{frequency!s}")
        self.ui.average_temp_lbl.setText(f"{temp!s}")
        self.ui.pressure_lbl.setText(f"{pressure!s}")

        if self.save_thread.saving:
            self.save_thread.update_key_value("Velocity [m/s]", wind_velocity)
            self.save_thread.update_key_value("Temp [°C]", temp)
            self.save_thread.update_key_value("pressure [Pa]", pressure)
            self.save_thread.update_key_value("frequency [Hz]", frequency)

    def _handle_scale_data(self, data):
        if self.save_thread.saving:
            self.save_thread.update_key_value("FX [N]", data.get("x"))
            self.save_thread.update_key_value("FY [N]", data.get("y"))
            self.save_thread.update_key_value("FZ [N]", data.get("z"))
            self.save_thread.update_key_value("MX [Nm]", data.get("mx"))
            self.save_thread.update_key_value("MY [Nm]", data.get("my"))
            self.save_thread.update_key_value("MZ [Nm]", data.get("mz"))

    def _handle_papago_data(self, data):
        self.ui.temp_lbl.setText(str(data.get("P_temp")))
        self.ui.humidity_lbl.setText(str(data.get("P_humidity")))
        self.ui.atm_pressure_lbl.setText(str(data.get("P_pressure")))

        if self.save_thread.saving:
            self.save_thread.update_key_value("P Temp [°C]", data.get("P_temp"))
            self.save_thread.update_key_value("P Humidity [%]", data.get("P_hum"))
            self.save_thread.update_key_value("P Pressure [Pa]", data.get("P_pressure"))

    def _set_velocity_value(self):
        req_velocity = float(self.ui.set_velocity_le.text())
        self._update_configuration("velocity", req_velocity)

    def _set_frequency_mode(self, state):
        self._update_configuration("pid", state)

    def _set_frequency_value(self):
        req_frequency = float(self.ui.set_frequency_le.text()) if self.ui.set_frequency_le.text() != "" else 0
        self._update_configuration("frequency", req_frequency)

    def _update_configuration(self, key: str, value):
        self.configuration_data[key] = value

    def start_tunnel(self):
        self.set_check_btn_state(False)
        config = self.configuration_data
        self.tunnel_plc.switch_pid(config.get("pid"))
        if not config.get("pid"):
            self.tunnel_plc.set_wind_velocity(config.get("velocity"))
        else:
            self.tunnel_plc.set_engine_frequency(config.get("frequency"))

        self.tunnel_plc.start_engine()

        self.set_velocity_control_state(False)
        self.ui.start_tunnel_btn.setEnabled(False)
        self.ui.stop_tunnel_btn.setEnabled(True)

    def stop_tunnel(self):
        self.set_check_btn_state(True)
        self.tunnel_plc.switch_pid(False)
        self.tunnel_plc.stop_engine()
        self.set_velocity_control_state(True)
        self.ui.start_tunnel_btn.setEnabled(True)
        self.ui.stop_tunnel_btn.setEnabled(False)

    def set_buttons_state(self, state: bool):
        self.ui.stop_tunnel_btn.setEnabled(state)
        self.ui.start_tunnel_btn.setEnabled(state)

    def _set_buttons_state(self, state: bool):
        self.ui.start_tunnel_btn.setEnabled(state)
        self.ui.stop_tunnel_btn.setEnabled(not state)

    def set_velocity_control_state(self, state: bool):
        self.ui.set_velocity_le.setEnabled(state)
        self.ui.set_velocity_rb.setEnabled(state)
        self.ui.set_velocity_le.setEnabled(state)
        self.ui.set_velocity_rb.setEnabled(state)

    def set_available(self, connected: bool):
        """Handle real PLC connection changes only (PLC_CONNECTED)."""
        if connected is False and self.ui.stop_tunnel_btn.isEnabled():
            self.stop_tunnel()
        self.ui.plc_not_connected_lbl.setVisible(not connected)
        if connected:
            if not self.ui.stop_tunnel_btn.isEnabled():
                self.ui.start_tunnel_btn.setEnabled(True)
        else:
            self.ui.start_tunnel_btn.setEnabled(False)
            self.ui.stop_tunnel_btn.setEnabled(False)

    def set_ready(self, ready: bool):
        """Enable Start only when drive reports ready and tunnel is not running."""
        if self.ui.stop_tunnel_btn.isEnabled():
            return
        self.ui.start_tunnel_btn.setEnabled(bool(ready))

    def set_check_btn_state(self, state: bool):
        self.ui.set_velocity_rb.setEnabled(state)
        self.ui.set_frequency_rb.setEnabled(state)
        self.ui.set_frequency_le.setEnabled(state)
        self.ui.set_velocity_le.setEnabled(state)

    def reset_gui_after_external_stop(self):
        self.ui.start_tunnel_btn.setEnabled(True)
        self.ui.stop_tunnel_btn.setEnabled(False)

    def _csv_devices(self):
        return *self.tlaskans, *self.scales.tenso_scanners

    def _start_saving(self):
        self.save_thread.start_saving()
        for device in self._csv_devices():
            device.start_csv_logging()
        self._set_saving_buttons_state(False)

    def _stop_saving(self):
        self.save_thread.stop_saving()
        for device in self._csv_devices():
            device.stop_csv_logging()
        self._set_saving_buttons_state(True)

    def _set_saving_buttons_state(self, state: bool):
        self.ui.start_saving_btn.setVisible(state)
        self.ui.stop_saving_btn.setVisible(not state)

    def _open_dir_dialog(self):
        options = QFileDialog(self).options()
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder", "", options=options)
        self.ui.dir_path_line.setText(folder_path)
        self.save_thread.set_file_path(folder_path)
        for device in self._csv_devices():
            device.set_csv_path(folder_path)

    def _connect_tunnel(self):
        self._change_connect_btns_state(False)

        #connecting
        self.tunnel_plc.start()
        self.driver_3d.start()
        self.driver_2d.start()
        self.scales.start()
        self.tlaskans[0].start()
        self.tlaskans[1].start()

        self._set_buttons_state(True)

    def disconnect_tunnel(self):
        try:
            self._change_connect_btns_state(True)
            self.set_available(False)

            self.tlaskans[0].disconnect()
            self.tlaskans[1].disconnect()
            self.scales.disconnect()
            self.tunnel_plc.disconnect()
            self.driver_3d.disconnect()
            self.driver_2d.disconnect()

            self._set_buttons_state(False)
        except Exception as e:
            print(e)

    def _change_connect_btns_state(self, state: bool):
        self.ui.connect_tunel_btn.setVisible(state)
        self.ui.disconnect_tunnel_btn.setVisible(not state)



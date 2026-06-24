from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget
from Device_controllers.papago_controller import PapagoController
from Qt_files.Qt_python.ui_wind_tunnel_Info_view import Ui_Form
from Device_controllers.plc_controller import PLCController

class InfoPanel(QWidget):
    STOP_TUNNEL = Signal()

    def __init__(self, plc: PLCController, papago: PapagoController):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self._average_speed = [0]
        self._req_velocity: float = 0.0

        self.plc = plc
        self.papago = papago

        self._initial_graphical_changes()
        self._bind_buttons()
        self._bind_emits()

    def _initial_graphical_changes(self):
        self.ui.disconnect_tunnel_btn.hide()
        self.enable_buttons(False)
        self.ui.zero_values_btn.setHidden(True)
        self.ui.reserved_error_lbl.setVisible(False)

    def _bind_buttons(self):
        self.ui.connect_tunel_btn.clicked.connect(self._connect_tunnel)
        self.ui.disconnect_tunnel_btn.clicked.connect(self.disconnect_tunnel)

        self.ui.pump_chb.clicked.connect(lambda: self.plc.switch_pump(self.ui.pump_chb.isChecked()))
        self.ui.cooling_chb.clicked.connect(lambda: self.plc.switch_cooling(self.ui.cooling_chb.isChecked()))

    def _bind_emits(self):
        self.plc.PLC_DATA.connect(self._handle_plc_data)
        self.papago.PAPAGO_DATA.connect(self._handle_papago_data)
        self.plc.PLC_CONNECTED.connect(self.show_plc_connected_message)

    def _handle_papago_data(self, papago_data):
        self.ui.humidity_lbl.setText(str(papago_data.get("humidity")))
        self.ui.atm_pressure_lbl.setText(str(papago_data.get("pressure")))
        self.ui.temp_lbl.setText(str(papago_data.get("temperature")))

    def switch_off_cooling(self):
        self.ui.cooling_chb.setChecked(False)

    def switch_off_pump(self):
        self.ui.pump_chb.setChecked(False)

    def set_button_state(self, state: bool):
        self.ui.cooling_chb.setEnabled(state)
        self.ui.pump_chb.setEnabled(state)

    def _handle_plc_data(self, plc_data):
        wind_velocity = plc_data.get("wind_velocity")
        wind_maxmin = plc_data.get("wind_velocity_maxmin")
        rotations = plc_data.get("engine_rotations")
        temp = plc_data.get("average_temp")
        temp_maxmin = plc_data.get("avg_temp_maxmin")
        pressure = plc_data.get("diff_pressure")
        pressure_maxmin = plc_data.get("pressure_maxmin")

        self.ui.wind_velocity_lbl.setText(f"{str(wind_velocity)}")
        self.ui.max_min_velocity_lbl.setText(f"{str(wind_maxmin)}")
        self.ui.frequency_lbl.setText(f"{str(rotations)}")
        self.ui.average_temp_lbl.setText(f"{str(temp)}")
        self.ui.max_min_temp_lbl.setText(f"{str(temp_maxmin)}")
        self.ui.pressure_lbl.setText(f"{str(pressure)}")
        self.ui.max_min_pressure_lbl.setText(f"{str(pressure_maxmin)}")

    def show_plc_connected_message(self, connected: bool):
        self.ui.plc_not_connected_lbl.setVisible(not connected)

    def enable_buttons(self, state: bool):
        self.ui.zero_values_btn.setEnabled(state)
        self.ui.stop_tunnel_btn.setEnabled(state)

    def _connect_tunnel(self):
        self.ui.connect_tunel_btn.hide()
        self.ui.disconnect_tunnel_btn.show()

        #connecting
        self.plc.start()
        self.papago.start()

        self.enable_buttons(True)

    def disconnect_tunnel(self):
        try:
            self.ui.disconnect_tunnel_btn.hide()
            self.ui.connect_tunel_btn.show()

            self.plc.disconnect()

            self.enable_buttons(False)
        except Exception as e:
            print(e)



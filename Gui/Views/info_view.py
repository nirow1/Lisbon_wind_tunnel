from PySide6.QtCore import Signal, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget
from Device_controllers.papago_controller import PapagoController
from Device_controllers.tunnel_plc_controller import TunnelPLCController
from Qt_files.Qt_python.ui_wind_tunnel_Info_view import Ui_Form

class InfoPanel(QWidget):
    STOP_TUNNEL = Signal()

    def __init__(self, tunnel_plc: TunnelPLCController, papago: PapagoController):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self._average_speed = [0]
        self._req_velocity: float = 0.0

        self.tunnel_plc = tunnel_plc
        self.papago = papago

        self._initial_graphical_changes()
        self._bind_buttons()
        self._bind_emits()

    def _initial_graphical_changes(self):
        self.ui.disconnect_tunnel_btn.hide()
        self.enable_buttons(False)
        self.ui.change_dir_btn.setIcon(QIcon("./App_data/dir_icon.png"))
        self.ui.change_dir_btn.setIconSize(QSize(54, 30))
        self.ui.reserved_error_lbl.setVisible(False)

    def _bind_buttons(self):
        self.ui.connect_tunel_btn.clicked.connect(self._connect_tunnel)
        self.ui.disconnect_tunnel_btn.clicked.connect(self.disconnect_tunnel)

    def _bind_emits(self):
        self.tunnel_plc.SENSOR_VALUES.connect(self._handle_plc_data)
        self.papago.PAPAGO_DATA.connect(self._handle_papago_data)
        self.tunnel_plc.PLC_CONNECTED.connect(self.show_plc_connected_message)

    def _handle_papago_data(self, papago_data):
        self.ui.humidity_lbl.setText(str(papago_data.get("humidity")))
        self.ui.atm_pressure_lbl.setText(str(papago_data.get("pressure")))
        self.ui.temp_lbl.setText(str(papago_data.get("temperature")))

    def _handle_plc_data(self, plc_data):
        wind_velocity = plc_data.get("wind_filtered")
        frequency = plc_data.get("frequency")
        temp = plc_data.get("average_temp")
        pressure = plc_data.get("pressure_filtered")

        self.ui.wind_velocity_lbl.setText(f"{str(wind_velocity)}")
        self.ui.frequency_lbl.setText(f"{str(frequency)}")
        self.ui.average_temp_lbl.setText(f"{str(temp)}")
        self.ui.pressure_lbl.setText(f"{str(pressure)}")

    def show_plc_connected_message(self, connected: bool):
        self.ui.plc_not_connected_lbl.setVisible(not connected)

    def enable_buttons(self, state: bool):
        self.ui.stop_tunnel_btn.setEnabled(state)

    def _connect_tunnel(self):
        self.ui.connect_tunel_btn.hide()
        self.ui.disconnect_tunnel_btn.show()

        #connecting
        self.tunnel_plc.start()
        self.papago.start()

        self.enable_buttons(True)

    def disconnect_tunnel(self):
        try:
            self.ui.disconnect_tunnel_btn.hide()
            self.ui.connect_tunel_btn.show()

            self.tunnel_plc.disconnect()

            self.enable_buttons(False)
        except Exception as e:
            print(e)



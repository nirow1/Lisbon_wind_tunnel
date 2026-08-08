from Device_controllers.tunnel_plc_controller import TunnelPLCController
from Device_controllers.driver_3d_plc_controller import DriverPLCController
from Device_controllers.scale_plc_controller import ScalePLCController
from Qt_files.Qt_python.ui_wind_tunnel_main_view import Ui_MainWindow
from Device_controllers.tlaskan_controller import TlaskanController
from Device_controllers.papago_controller import PapagoController
from Gui.Views.configuration_view import ConfigurationView
from Gui.Views.traverser_view import TraverserView
from Gui.Views.pressure_view import PressureView
from Gui.Views.settings_view import SettingsView
from PySide6.QtWidgets import QMainWindow, QLabel
from Gui.Views.scale_view import ScaleView
from Gui.Views.info_view import InfoPanel
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.current_frequency = 0

        # device communication
        self.tunnel_plc = TunnelPLCController()
        self.driver_plc = DriverPLCController()
        #self.scale_plc = ScalePLCController()
        self.tlaskan = TlaskanController("192.168.10.91")
        self.tlaskan_2 = TlaskanController("192.168.10.90")
        self.papago = PapagoController()

        self.control_byte = {}

        # creating views
        self.info_panel = InfoPanel(self.tunnel_plc, self.driver_plc, self.papago)
        self.ui.control_panel_lo.addWidget(self.info_panel)

        self.config_view = ConfigurationView(self.tunnel_plc, self.papago)
        self.ui.stackedWidget.addWidget(self.config_view)

        self.settings_pg = SettingsView(self.tunnel_plc)
        self.ui.stackedWidget.addWidget(self.settings_pg)

        self.traverser_view = TraverserView(self.driver_plc)
        self.ui.stackedWidget.addWidget(self.traverser_view)

        self.scale_view = ScaleView()
        self.ui.stackedWidget.addWidget(self.scale_view)

        self.pressure_view = PressureView(self.tlaskan, self.tlaskan_2)
        self.ui.stackedWidget.addWidget(self.pressure_view)

        self._init_graphical_changes()
        self._bind_buttons()
        self._handle_emits()

    def _init_graphical_changes(self):
        self.ui.stackedWidget.setCurrentWidget(self.config_view)
        self.ui.j4_logo_lbl.setPixmap(QPixmap('./App_data/4j_logo_150x50.png'))

        for i in range(1,4):
            led: QLabel = self.ui.widget_203.findChild(QLabel, "led_" + str(i))
            led.setPixmap(QPixmap('./App_data/grey_led_15.png'))

        self.change_led(self.ui.est_converter_ld, "red", False)
        self.change_led(self.ui.est_service_ld, "red", False)

        self.setWindowIcon(QIcon("./App_data/ico.png"))
        self.setWindowTitle("Wind Tunnel")
        self.setMinimumSize(QSize(1400, 790))

    def _bind_buttons(self):
        self.ui.pid_settings_pg_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.login_pg))
        self.ui.config_pg_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.config_view))
        self.ui.next_params_pg_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.next_params_pg))
        self.ui.drivers_pg_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.traverser_view))
        self.ui.scales_pg_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.scale_view))
        self.ui.pressures_pg_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.pressure_view))

        self.ui.log_in_btn.clicked.connect(self._check_login)
        self.ui.password_le.setEchoMode(self.ui.password_le.EchoMode.Password)

    def _handle_emits(self):
        self.settings_pg.RETURN_TO_MAIN.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.config_view))
        self.config_view.TEST_RUNNING.connect(
            lambda running: self.info_panel.set_buttons_state(not running)
        )

        self.tunnel_plc.SENSOR_VALUES.connect(self._handle_plc_data)
        self.tunnel_plc.STATUS_DATA.connect(self._handle_status_data)
        self.tunnel_plc.CONTROL_BYTE.connect(self._handle_control_byte_data)
        self.tunnel_plc.DRIVER_DATA.connect(self._handle_driver_data)
        self.tunnel_plc.SAFETY_DIAGNOSTICS.connect(self._handle_safety_diagnostics)

    def _handle_plc_data(self, plc_data: dict):
        self.ui.temp_in_raw_lbl.setText(str(plc_data.get("temp_input_filtered")))
        self.ui.temp_out_raw_lbl.setText(str(plc_data.get("temp_output_filtered")))
        self.ui.diff_pres_raw_lbl.setText(str(plc_data.get("pressure_raw")))
        self.ui.diff_pres_fltr_lbl.setText(str(plc_data.get("pressure_filtered")))

    def _handle_status_data(self, status_data: dict):
        self.change_led(self.ui.led_1, "green", status_data.get("rdy"))
        self.change_led(self.ui.led_2, "blue", not status_data.get("safety"))
        self.change_led(self.ui.led_3, "red", status_data.get("e-stop"))
        self.change_led(self.ui.led_4, "red", status_data.get("drive_error"))

        self.info_panel.set_available(status_data.get("rdy"))

    def _handle_control_byte_data(self, control_byte_data: dict):
        if control_byte_data == self.control_byte:
            return

        turned_off = [key for key in control_byte_data
                      if self.control_byte.get(key) == 1 and control_byte_data.get(key) == 0]

        external_change = self.tunnel_plc.control_byte != control_byte_data
        self.control_byte = control_byte_data.copy()

        if not external_change:
            return

        self.tunnel_plc.control_byte.update(control_byte_data)

        if "start" in turned_off:
            self.info_panel.reset_gui_after_external_stop()

    def _handle_driver_data(self, fan_params: dict):
        self.ui.driver_status_lbl.setText(str(fan_params.get("driver_status")))
        self.ui.error_code_lbl.setText(str(fan_params.get("error_code")))
        self.ui.output_lbl.setText(str(fan_params.get("power")))
        self.ui.current_lbl.setText(str(fan_params.get("current")))
        self.ui.moment_lbl.setText(str(fan_params.get("torque")))
        self.ui.engine_temp_lbl.setText(str(fan_params.get("motor_temp")))
        self.ui.converter_temp_lbl.setText(str(fan_params.get("drive_temp")))

    def _handle_safety_diagnostics(self, status_params: dict):
        self.change_led(self.ui.est_converter_ld, "red", not status_params.get("estop_main"))
        self.change_led(self.ui.est_service_ld, "red", not status_params.get("estop_panel"))

    def _check_login(self):
        if self.ui.user_name_le.text() == "admin" and self.ui.password_le.text() == "admin":
            self.ui.user_name_le.setText("")
            self.ui.password_le.setText("")
            self.ui.stackedWidget.setCurrentWidget(self.settings_pg)

    def on_app_exit(self):
        self.tunnel_plc.disconnect()
        self.driver_plc.disconnect()
        #self.scale_plc.disconnect()
        self.tlaskan.disconnect()
        self.tlaskan_2.disconnect()
        self.info_panel.disconnect_tunnel()

    @staticmethod
    def change_led(label: QLabel, color: str, state: bool):
        if state:
            label.setPixmap(QPixmap(f"./App_data/{color}_led_15.png"))
        else:
            label.setPixmap(QPixmap('./App_data/grey_led_15.png'))

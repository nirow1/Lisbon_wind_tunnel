from Device_controllers.papago_controller import PapagoController
from Gui.Views.configuration_view import ConfigurationView
from Gui.Views.settings_view import SettingsView
from Qt_files.Qt_python.ui_wind_tunnel_main_view import Ui_MainWindow
from Device_controllers.plc_controller import PLCController
from PySide6.QtWidgets import QMainWindow, QLabel, QTableWidgetItem
from Gui.Views.info_view import InfoPanel
from Gui.Charts.zoomable_chart import ZoomableChart
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._init_graphical_changes()
        self.current_frequency = 0

        # charts setup block
        self.chart = ZoomableChart(
            name="",
            x_axis_seconds=600,
            y_axis=(0, 50),
            line_name=["Wind velocity[m/s]", "Wind temperature [°C]"],
            line_count=2
        )

        self.ui.scale_chart.addWidget(self.chart)

        # device communication
        self.plc = PLCController()
        self.papago = PapagoController()

        self.control_byte = {}

        # creating views
        self.info_panel = InfoPanel(self.plc, self.papago)
        self.ui.control_panel_lo.addWidget(self.info_panel)

        self.config_panel = ConfigurationView(self.plc, self.papago)
        self.ui.stackedWidget.addWidget(self.config_panel)

        self.settings_pg = SettingsView(self.plc)
        self.ui.stackedWidget.addWidget(self.settings_pg)

        self._handle_emits()
        self._bind_buttons()

    def _init_graphical_changes(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.wind_vel_pg)

        self.ui.j4_logo_lbl.setPixmap(QPixmap('./App_data/4j_logo_150x50.png'))

        for i in range(1,8):
            led: QLabel = self.ui.widget_203.findChild(QLabel, "led_" + str(i))
            led.setPixmap(QPixmap('./App_data/grey_led_15.png'))

        self.change_led(self.ui.est_converter_ld, "red", False)
        self.change_led(self.ui.est_service_ld, "red", False)
        self.change_led(self.ui.est_measure_space_ld, "red", False)
        self.change_led(self.ui.est_entry_doors_ld, "red", False)
        self.change_led(self.ui.est_hexapod_ld, "red", False)
        self.change_led(self.ui.est_doors_meas_space_ld, "red", False)
        self.change_led(self.ui.est_doors_meas_space_ld_2, "red", False)

        self.ui.tableWidget.insertRow(0)
        self.ui.tableWidget.setRowHeight(0, 40)

        self.setWindowIcon(QIcon("./App_data/ico.png"))
        self.setWindowTitle("Wind Tunnel")
        self.setMinimumSize(QSize(1400, 790))

    def _bind_buttons(self):
        self.ui.pid_settings_pg_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.login_pg))
        self.ui.config_pg_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.config_panel))
        self.ui.run_pg_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.wind_vel_pg))
        self.ui.next_params_pg_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.next_params_pg))

        self.ui.log_in_btn.clicked.connect(self._check_login)
        self.ui.password_le.setEchoMode(self.ui.password_le.EchoMode.Password)

        self.ui.restart_chart_btn.clicked.connect(self.chart.reset_axis)

        self.ui.start_tunnel_btn.clicked.connect(self.start_tunnel)
        self.ui.stop_tunnel_btn.clicked.connect(self.stop_tunnel)
        self.info_panel.ui.stop_tunnel_btn.clicked.connect(self.stop_tunnel)

    def _handle_emits(self):
        self.settings_pg.RETURN_TO_MAIN.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.wind_vel_pg))

        self.plc.PLC_DATA.connect(self._handle_plc_data)
        self.plc.STATUS_DATA.connect(self._handle_status_data)
        self.plc.PLC_CONNECTED.connect(self.set_available)
        self.plc.CONTROL_BYTE.connect(self._handle_control_byte_data)
        self.plc.PARAM_DATA_FAN.connect(self._handle_fan_params)
        self.plc.PARAM_DATA_STATUS.connect(self._handle_status_params)

        self.info_panel.STOP_TUNNEL.connect(self.config_panel.deselect_radiobuttons)

        self.config_panel.SETTINGS_CHANGES.connect(self._add_changes_to_table)

    def _handle_plc_data(self, plc_data: dict):
        self.chart.update_chart([plc_data.get("wind_velocity"), plc_data.get("average_temp")])

        self.ui.temp_in_raw_lbl.setText(str(plc_data.get("temp_entry")))
        self.ui.temp_out_raw_lbl.setText(str(plc_data.get("temp_exit")))
        self.ui.diff_pres_raw_lbl.setText(str(plc_data.get("diff_pressure_raw")))
        self.ui.diff_pres_fltr_lbl.setText(str(plc_data.get("diff_pressure")))

    def _handle_status_data(self, status_data: dict):
        self.change_led(self.ui.led_1, "green", status_data.get("rdy"))
        self.change_led(self.ui.led_2, "red", status_data.get("e-stop"))
        self.change_led(self.ui.led_3, "red", status_data.get("doors"))
        self.change_led(self.ui.led_4, "red", status_data.get("surge_protection"))
        self.change_led(self.ui.led_5, "red", status_data.get("driver_error"))
        self.change_led(self.ui.led_6, "blue", not status_data.get("safety"))
        self.change_led(self.ui.led_7, "green", status_data.get("concetrc"))

        self.info_panel.set_button_state(status_data.get("rdy"))
        self.ui.start_tunnel_btn.setEnabled(status_data.get("rdy"))

        self.config_panel.enable_setting_velocity(status_data.get("concetrc"))

    def _handle_control_byte_data(self, control_byte_data: dict):
        if control_byte_data == self.control_byte:
            return

        turned_off = [key for key in control_byte_data
                      if self.control_byte.get(key) == 1 and control_byte_data.get(key) == 0]

        external_change = self.plc.control_byte != control_byte_data
        self.control_byte = control_byte_data.copy()

        if not external_change:
            return

        self.plc.control_byte.update(control_byte_data)

        if "pump" in turned_off:
            self.info_panel.switch_off_pump()

        if "cooling" in turned_off:
            self.info_panel.switch_off_cooling()

        if "start" in turned_off:
            self._reset_gui_after_external_stop()

        if "control" in turned_off:
            self.config_panel.switch_ramp_off()

    def _handle_fan_params(self, fan_params: dict):
        self.ui.driver_status_lbl.setText(str(fan_params.get("driver_status")))
        self.ui.error_code_lbl.setText(str(fan_params.get("error_code")))
        self.ui.output_lbl.setText(str(fan_params.get("output")))
        self.ui.current_lbl.setText(str(fan_params.get("current")))
        self.ui.moment_lbl.setText(str(fan_params.get("moment")))
        self.ui.engine_temp_lbl.setText(str(fan_params.get("engine_temp")))
        self.ui.converter_temp_lbl.setText(str(fan_params.get("converter_temp")))

    def _handle_status_params(self, status_params: dict):
        self.change_led(self.ui.est_converter_ld, "red", not status_params.get("est_converter"))
        self.change_led(self.ui.est_service_ld, "red", not status_params.get("est_service"))
        self.change_led(self.ui.est_measure_space_ld, "red", not status_params.get("est_measure_space"))
        self.change_led(self.ui.est_entry_doors_ld, "red", not status_params.get("est_entry_doors"))
        self.change_led(self.ui.est_hexapod_ld, "red", not status_params.get("est_hexapod"))
        self.change_led(self.ui.est_doors_meas_space_ld, "red", not status_params.get("est_doors_meas_space"))
        self.change_led(self.ui.est_doors_meas_space_ld_2, "red", not status_params.get("est_doors_meas_space_2"))

    def set_available(self, state: bool):
        if self.ui.stop_tunnel_btn.isEnabled():
            self.stop_tunnel()
        self.ui.start_tunnel_btn.setEnabled(state)

    def start_tunnel(self):
        config = self.config_panel.get_configuration()
        self.plc.switch_pid(config.get("pid"))
        if not config.get("pid"):
            self.plc.set_wind_velocity(config.get("velocity"))
        else:
            self.plc.set_engine_frequency(config.get("frequency"))


        self.plc.set_ramp_up(config.get("ramp_up"))
        self.plc.set_ramp_down(config.get("ramp_down"))
        self.plc.set_run_dur(config.get("run_duration"))
        self.config_panel.start_saving()
        self.plc.switch_control(config.get("control"))
        self.plc.start_engine()

        self.ui.start_tunnel_btn.setEnabled(False)
        self.ui.stop_tunnel_btn.setEnabled(True)

    def _reset_gui_after_external_stop(self):
        """PLC zastavilo motor externě — pouze reset GUI, bez zápisu do PLC."""
        self.config_panel.stop_saving()
        self.ui.start_tunnel_btn.setEnabled(True)
        self.ui.stop_tunnel_btn.setEnabled(False)

    def stop_tunnel(self):
        self.plc.switch_pid(False)
        self.plc.set_wind_velocity(0)
        self.plc.set_engine_frequency(0)
        self.plc.switch_control(False)
        self.plc.set_ramp_up(0)
        self.plc.set_ramp_down(0)
        self.plc.set_run_dur(0)
        self.plc.stop_engine()
        self.config_panel.stop_saving()
        self.ui.start_tunnel_btn.setEnabled(True)
        self.ui.stop_tunnel_btn.setEnabled(False)

    def _add_changes_to_table(self, changes: dict):
        if not changes.get("pid"):
            self.ui.tableWidget.hideColumn(1)
            self.ui.tableWidget.showColumn(0)
        else:
            self.ui.tableWidget.hideColumn(0)
            self.ui.tableWidget.showColumn(1)

        self.ui.tableWidget.setItem(0, 0, QTableWidgetItem(str(changes.get("velocity"))))
        self.ui.tableWidget.setItem(0, 1, QTableWidgetItem(str(changes.get("frequency"))))
        self.ui.tableWidget.setItem(0, 2, QTableWidgetItem(str(changes.get("control"))))
        self.ui.tableWidget.setItem(0, 3, QTableWidgetItem(str(changes.get("ramp_up"))))
        self.ui.tableWidget.setItem(0, 4, QTableWidgetItem(str(changes.get("ramp_down"))))
        self.ui.tableWidget.setItem(0, 5, QTableWidgetItem(str(changes.get("run_duration"))))

    def _check_login(self):
        if self.ui.user_name_le.text() == "admin" and self.ui.password_le.text() == "admin":
            self.ui.user_name_le.setText("")
            self.ui.password_le.setText("")
            self.ui.stackedWidget.setCurrentWidget(self.settings_pg)

    def _zero_values_of_all_measurements(self):
        pass

    def on_app_exit(self):
        self.plc.disconnect()
        self.info_panel.disconnect_tunnel()

    @staticmethod
    def change_led(label: QLabel, color: str, state: bool):
        if state:
            label.setPixmap(QPixmap(f"./App_data/{color}_led_15.png"))
        else:
            label.setPixmap(QPixmap('./App_data/grey_led_15.png'))

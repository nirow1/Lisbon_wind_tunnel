import csv
import os
from datetime import datetime

from PySide6.QtCore import QTimer, QObject


class SavingThread(QObject):
    def __init__(self, interval=1000):
        super().__init__()

        self.save_timer = QTimer()
        self.save_timer.setInterval(interval)
        self.save_timer.timeout.connect(self._save_data)

        self.data_to_save = {}
        self.saving = False
        self.reset_save_file = False
        self.timer_state = False
        self._save_file_name = ""
        self._save_folder_path = ""
        self._save_path = ""
        self.save_count = 0
        self.save_duration = 0

    def start_saving(self):
        self.saving = True
        self.save_count = 0
        self._update_save_path()
        self.save_timer.start()
        self.reset_save_file = True

    def stop_saving(self):
        self.saving = False
        self.save_timer.stop()

    def activate_timer(self, state: bool, duration: str):
        self.timer_state = state
        self.save_duration = int(duration)

    def update_key_value(self, key: str, value):
        self.data_to_save[key] = value

    def update_saving_data(self, data: dict):
        self.data_to_save.update(data)

    def _save_data(self):
        if self.timer_state and self.save_duration != "" and self.save_count >= int(self.save_duration) - 1:
            self.stop_saving()

        exists = os.path.exists(self._save_folder_path)

        time = datetime.now().strftime("%H:%M:%S")[:-5]
        self.data_to_save["time"] = time

        if self.reset_save_file:
            open(self._save_folder_path, "w")
            exists = False
            self.reset_save_file = False

        with open(self._save_folder_path, 'a', newline="") as f:
            writer = csv.writer(f)
            if not exists:
                writer.writerow(self.data_to_save.keys())
            writer.writerow(self.data_to_save.values())
        self.save_count += 1

    def set_save_file_name(self, name: str):
        self._save_file_name = name

    def set_file_path(self, path: str):
        self._save_folder_path = path

    def _update_save_path(self):
        file_path = self._save_folder_path

        if self._save_folder_path == "":
            file_path = os.getcwd()

        if self._save_file_name == "":
            name = "Wind_tunnel_" + datetime.now().strftime("%Y-%m-%d_%H%M")
        else:
            name = self._save_file_name

        file_path += f"/{name}.csv"
        self._save_path = file_path
import csv
import os
from datetime import datetime

from PySide6.QtCore import QObject, QTimer


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
        try:
            self.save_duration = int(duration) if duration.strip() else 0
        except ValueError:
            self.save_duration = 0

    def update_key_value(self, key: str, value):
        self.data_to_save[key] = value

    def update_saving_data(self, data: dict):
        self.data_to_save.update(data)

    def _save_data(self):
        if self.timer_state and self.save_duration > 0 and self.save_count >= self.save_duration - 1:
            self.stop_saving()

        if not self._save_path:
            self._update_save_path()

        self.data_to_save["time"] = datetime.now().strftime("%H:%M:%S")

        write_header = self.reset_save_file or not os.path.exists(self._save_path)
        mode = "w" if self.reset_save_file else "a"
        self.reset_save_file = False

        with open(self._save_path, mode, newline="") as f:
            writer = csv.writer(f)
            if write_header:
                writer.writerow(self.data_to_save.keys())
            writer.writerow(self.data_to_save.values())
        self.save_count += 1

    def set_save_file_name(self, name: str):
        self._save_file_name = name.strip()

    def set_file_path(self, path: str):
        self._save_folder_path = path.strip() if path else ""

    def _update_save_path(self):
        folder = self._save_folder_path if self._save_folder_path else os.getcwd()

        if self._save_file_name:
            name = self._save_file_name
            if name.lower().endswith(".csv"):
                name = name[:-4]
        else:
            name = "Wind_tunnel_" + datetime.now().strftime("%Y-%m-%d_%H%M")

        self._save_path = os.path.join(folder, f"{name}.csv")

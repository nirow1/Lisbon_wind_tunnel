import csv
import os
import threading


class DeviceCsvLogger:
    """Thread-safe CSV session for high-rate device streams."""

    def __init__(
        self,
        basename: str,
        header: list[str] | tuple[str, ...] | None = None,
        delimiter: str = ",",
        ip: str = "",
    ):
        self._basename = basename
        self._header = list(header) if header else []
        self._delimiter = delimiter
        self._ip = ip
        self._directory = ""
        self._file = None
        self._writer = None
        self._lock = threading.Lock()

    @property
    def active(self) -> bool:
        return self._writer is not None

    def set_directory(self, path: str) -> None:
        self._directory = path if path else ""

    def _filename(self) -> str:
        safe_ip = self._ip.replace(".", "_") if self._ip else "device"
        name = f"{self._basename}_{safe_ip}.csv"
        if self._directory:
            path = os.path.join(self._directory, name)
        else:
            path = name
        return os.path.abspath(path)

    def start(self) -> None:
        with self._lock:
            self._stop_unlocked()
            path = self._filename()
            directory = os.path.dirname(path)
            if directory:
                os.makedirs(directory, exist_ok=True)
            self._file = open(path, "w", newline="", buffering=1)
            self._writer = csv.writer(self._file, delimiter=self._delimiter)
            if self._header:
                self._writer.writerow(self._header)
            self._file.flush()
            print(f"CSV logging to: {path}")

    def stop(self) -> None:
        with self._lock:
            self._stop_unlocked()

    def _stop_unlocked(self) -> None:
        if self._file is not None:
            try:
                self._file.flush()
                self._file.close()
            except Exception as e:
                print(f"Error closing CSV: {e}")
            self._file = None
            self._writer = None

    def write_row(self, row) -> None:
        with self._lock:
            if self._writer is None:
                return
            self._writer.writerow(row)
            if self._file is not None:
                self._file.flush()

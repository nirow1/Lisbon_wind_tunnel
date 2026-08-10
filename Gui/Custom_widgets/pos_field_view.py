from PySide6.QtWidgets import QWidget, QGraphicsView, QGraphicsScene, QVBoxLayout
from PySide6.QtGui import QBrush, QPen
from PySide6.QtCore import Qt, QRectF


class PositionFieldWidget(QWidget):
    def __init__(self,
                 device_width=1000,
                 device_height=1000,
                 field_width_px=300,
                 field_height_px=300,
                 point_radius=6,
                 parent=None):
        super().__init__(parent)

        self.device_width = float(device_width)
        self.device_height = float(device_height)
        self.field_width_px = float(field_width_px-3)
        self.field_height_px = float(field_height_px-3)
        self.point_radius = float(point_radius)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # Scene in pixel space
        self.scene = QGraphicsScene(0, 0, self.field_width_px, self.field_height_px)
        self.view = QGraphicsView(self.scene)
        self.view.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.view)

        # Background rectangle
        self.scene.addRect(
            QRectF(0, 0, self.field_width_px, self.field_height_px),
            QPen(Qt.GlobalColor.black),
            QBrush(Qt.GlobalColor.white)
        )

        # Point item
        r = self.point_radius
        self.point_item = self.scene.addEllipse(
            -r, -r, 2*r, 2*r,
            QPen(Qt.GlobalColor.red),
            QBrush(Qt.GlobalColor.red)
        )
        self.point_item.setPos(0.0, 0.0)

    def update_position(self, x_cm: float, y_cm: float):
        """Update point based on device coordinates (cm)."""

        # Ensure floats
        x_cm = float(x_cm)
        y_cm = float(y_cm)

        # Clamp to device boundaries
        x_cm = max(0.0, min(self.device_width, x_cm))
        y_cm = max(0.0, min(self.device_height, y_cm))

        # Current widget size (pixel space)
        w = float(self.width())
        h = float(self.height())

        # Convert device → pixel coordinates
        x_px = (x_cm / self.device_width) * w
        y_px = (y_cm / self.device_height) * h

        # Update graphics item
        self.point_item.setPos(x_px, y_px)

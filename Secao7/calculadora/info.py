from PySide6.QtWidgets import QLabel, QWidget
from variables import SMALL_FONTE_SIZE
from PySide6.QtCore import Qt

class Info(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.confifStyle()

    def confifStyle(self):
        self.setStyleSheet(f'font-size: {SMALL_FONTE_SIZE}px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)

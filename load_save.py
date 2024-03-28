from PyQt6.QtWidgets import (
    QMainWindow,
    QPushButton
)


class LogHouseLoadSaveWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Load Profile")
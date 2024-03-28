import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QToolBar,
    QStatusBar,
    QLineEdit
)

WINDOW_SIZE = 500

class LogHouseMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the main window settings
        self.setWindowTitle("LogHouse")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)

        # Set the layout for the central widget
        self.generalLayout = QVBoxLayout()

        # Set the central widget which all other widgets will inherit from
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)

    def _createMainPage(self):
        # Create the main page
        self.display = QLineEdit()
        self.display.setFixedHeight(WINDOW_SIZE)

def main():
    app = QApplication([])
    window = LogHouseMainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
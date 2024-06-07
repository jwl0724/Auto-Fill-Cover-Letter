import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget
from PyQt6 import QtGui


class screen:
    def __init__(self, width, height):
        self.app = QApplication(sys.argv)
        self.window = QWidget()
        self.window.setWindowTitle("Cover Letter AutoFiller")
        self.window.setWindowIcon(QtGui.QIcon("assets/icon.png"))

        # calculate screen location
        dimension = self.app.primaryScreen().size()
        self.window.setGeometry(offset_center(dimension.width() / 2, width),
            offset_center(dimension.height() / 2, height), width, height)


    def run(self):
        self.window.show()
        sys.exit(self.app.exec())


    def add_label(self, message: str, x: int, y: int, tag: str = None) -> None:
        if tag == None: label = QLabel(f"{message}")
        else: label = QLabel(f"<{tag}>{message}</{tag}>", parent=self.window)
        label.move(x, y)


    def get_window_dimensions(self):
        return self.window.size()


def offset_center(position: int, length: int) -> int:
    return int(position - length / 2)

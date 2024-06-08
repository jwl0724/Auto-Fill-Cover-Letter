import sys
import PyQt6.QtWidgets as qt
from PyQt6 import QtGui


class screen:
    def __init__(self, width, height):
        self.app = qt.QApplication(sys.argv)
        self.window = qt.QWidget()
        self.window.setWindowTitle("Cover Letter AutoFiller")
        self.window.setWindowIcon(QtGui.QIcon("assets/icon.png"))

        # calculate screen location
        dimension = self.app.primaryScreen().size()
        self.window.setGeometry(offset_center(dimension.width() / 2, width),
            offset_center(dimension.height() / 2, height), width, height)

        # populate initial view
        self.add_label("Cover Letter Autofiller", int(width / 2), int(height / 3), "h1", offset=True)
        button_width, button_height = 100, 30
        self.add_button("Upload .docx File", button_width, button_height, width / 2, height / 2, offset=True)
        

    def run(self):
        self.window.show()
        sys.exit(self.app.exec())


    def add_label(self, message: str, x: int, y: int, tag: str = None, offset: bool = False) -> None:
        if tag == None: label = qt.QLabel(f"{message}")
        else: label = qt.QLabel(f"<{tag}>{message}</{tag}>", parent=self.window)
        if offset: 
            label_dimensions = label.fontMetrics().boundingRect(label.text())
            print(label_dimensions.width(), label_dimensions.height(), label.text())
            label.move(offset_center(x, label_dimensions.width()), offset_center(y, label_dimensions.height()))
        else: label.move(x, y)


    def add_button(self, message: str, width: int, height: int, x: int, y: int, tag: str = None, offset: bool = False) -> None:
        if tag == None: button = qt.QPushButton(message, parent=self.window)
        else: button = qt.QPushButton(f"<{tag}>{message}</{tag}>", parent=self.window)
        button.setFixedSize(width, height)
        if offset: button.move(offset_center(x, button.size().width()), offset_center(y, button.size().height()))
        else: button.move(x, y)


    def get_window_dimensions(self):
        return self.window.size()


def offset_center(position: int, length: int) -> int:
    return int(position - length / 2)

from PySide6.QtWidgets import QWidget

from interface_ui import Ui_Form
from hPyT import *


class QrcodeView(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setWindowTitle(' ')
        self.set_titlebar_color()

    def set_titlebar_color(self):
        title_bar_color.set(self, '#FFFFFF')  # sets the titlebar color to white

    def get_text(self) -> str:
        return self.ui.le_text.text()

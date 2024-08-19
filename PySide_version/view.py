from PySide6.QtGui import QFontDatabase, QFont
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QPushButton, QLineEdit
from hPyT import *

from interface_ui import Ui_Form
import resource_rc


def load_font_from_qrc():
    font_id = QFontDatabase.addApplicationFont(":assets/Figtree-Black.ttf")
    if font_id != -1:
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        font = QFont(font_family, 11)
        font.setStyleStrategy(QFont.StyleStrategy.PreferQuality | QFont.StyleStrategy.PreferAntialias)
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)

        return font
    else:
        print("Error: Failed to load font from QRC")
        return None


class QrcodeView(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.apply_font()

        self.setWindowTitle(' ')
        self.set_titlebar_color()

    def set_titlebar_color(self):
        title_bar_color.set(self, '#FFFFFF')  # sets the titlebar color to white

    def get_text(self) -> str:
        return self.ui.le_text.text()

    def draw_image(self, pixmap):
        if pixmap:
            self.ui.lbl_img.setPixmap(pixmap)
        else:
            self.ui.lbl_img.clear()

    def get_image(self) -> QPixmap:
        return self.ui.lbl_img.pixmap()

    def apply_font(self):
        font = load_font_from_qrc()
        if font:
            for type_ in (QPushButton, QLineEdit):
                for widget in self.findChildren(type_):
                    widget.setFont(font)

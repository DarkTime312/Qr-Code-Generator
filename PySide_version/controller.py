from PySide6.QtGui import QPixmap

from view import QrcodeView
from model import QrcodeModel


class QrcodeController:
    def __init__(self):
        super().__init__()
        self.view = QrcodeView()
        self.model = QrcodeModel()
        self.connect_signals_to_slots()

    def connect_signals_to_slots(self):
        self.view.ui.le_text.textChanged.connect(self.create_image)

    def create_image(self, text: str):
        image: QPixmap = self.model.create_qr(text)
        if image:
            self.view.ui.lbl_img.setPixmap(image)
        else:
            self.view.ui.lbl_img.clear()

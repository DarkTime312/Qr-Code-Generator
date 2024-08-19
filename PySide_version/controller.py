from PySide6.QtGui import QPixmap, QFontDatabase, QFont
from PySide6.QtWidgets import QFileDialog, QMessageBox

from model import QrcodeModel
from view import QrcodeView


class QrcodeController:
    def __init__(self):
        super().__init__()
        self.view = QrcodeView()

        self.model = QrcodeModel()
        self.connect_signals_to_slots()

    def connect_signals_to_slots(self):
        self.view.ui.btn_generate.clicked.connect(self.create_image)
        self.view.ui.btn_save.clicked.connect(self.save_image)
        self.view.ui.le_text.returnPressed.connect(self.create_image)

    def create_image(self):
        current_text: str = self.view.get_text()
        image: QPixmap = self.model.create_qr(current_text)
        self.view.draw_image(image)

    def save_image(self):
        pixmap = self.view.get_image()

        if pixmap.isNull():
            QMessageBox.warning(self.view, 'No Image', 'No Image has been generated.')
            return

        save_path, _ = QFileDialog.getSaveFileName(self.view, filter="PNG (*.png)")

        if not save_path:
            return

        result = pixmap.save(save_path, "PNG", 100)

        if result:
            QMessageBox.information(self.view, 'Success', f"Qr code saved successfully to {save_path}")
        else:
            QMessageBox.critical(self.view, 'Error', f"Operation Failed.")

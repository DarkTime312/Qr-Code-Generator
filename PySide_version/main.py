import sys

from PySide6.QtWidgets import QApplication

from controller import QrcodeController

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QrcodeController()
    window.view.show()
    sys.exit(app.exec())

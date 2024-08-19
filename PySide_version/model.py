import qrcode
from PIL.ImageQt import QPixmap

# QR code image size
IMG_WIDTH = 400
IMG_HEIGHT = 400


class QrcodeModel:
    def __init__(self):
        super().__init__()

    @staticmethod
    def create_qr(current_text: str) -> QPixmap | None:
        """Generates A qr code from provided text by user.
            It then updates the Label widget with new image.
        """
        if not current_text:
            return None

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=3,
        )
        # Add data to the QR code
        qr.add_data(current_text)
        qr.make(fit=True)

        # Create an image from the QR code instance
        qr_image = qr.make_image(fill_color="black", back_color="white")
        pix_map = qr_image.toqpixmap()

        return pix_map

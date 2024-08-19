import qrcode
from PIL.ImageQt import QPixmap
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import RadialGradiantColorMask

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

        qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L,
                           box_size=10,
                           border=3,
                           version=3,
                           )
        qr.add_data(current_text)

        img = qr.make_image(image_factory=StyledPilImage,
                            color_mask=RadialGradiantColorMask(),
                            fit=True)
        pixmap = img.toqpixmap()
        return pixmap

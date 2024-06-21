import tkinter as tk
from PIL import Image
from tkinter.filedialog import asksaveasfilename

import qrcode
import customtkinter as ctk

# QR code image size
IMG_WIDTH = 400
IMG_HEIGHT = 400


class QrCodeGenerator(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color='white')
        self.geometry(f'{IMG_WIDTH+150}x{IMG_HEIGHT+150}')
        self.title('')
        self.iconbitmap('assets/empty.ico')
        self.minsize(width=120, height=0)

        self.top_frame = TopFrame(self, width=IMG_WIDTH, height=IMG_HEIGHT, fg_color='white')
        self.top_frame.place(relx=0.5, rely=0.4, anchor='center', relwidth=0.6, relheight=0.6)

        self.bottom_frame = BottomFrame(self,
                                        fg_color='#021fb3',
                                        height=100,
                                        corner_radius=20
                                        )
        self.bottom_frame.place(relx=0, rely=0.8, relwidth=1, relheight=0.235, anchor='nw')


class TopFrame(ctk.CTkFrame):
    """Frame which contains qr code image inside a label."""
    def __init__(self, parent, **kwargs):
        super().__init__(master=parent, **kwargs)
        # Label which contains generated qr code
        # An initial placeholder image added for our program start up.
        qr_img = ctk.CTkImage(Image.open('assets/Placeholder.png'), size=(IMG_WIDTH, IMG_HEIGHT))
        self.image_label = ctk.CTkLabel(self, image=qr_img, text='')
        self.image_label.pack(expand=True, fill='both')


class BottomFrame(ctk.CTkFrame):
    """Frame which contains Entry box and button."""
    def __init__(self, parent, **kwargs):
        super().__init__(master=parent, **kwargs)
        self.pil_image = None  # will contain the pillow Image version.
        self.parent = parent
        self.label_widget = self.parent.top_frame.image_label

        # A frame to contain the buttons
        self.buttons_frame = ctk.CTkFrame(self, fg_color='#021fb3')
        self.buttons_frame.place(relx=0.5, rely=0.4, anchor='center')

        # Entry box
        self.ent_var = tk.StringVar()
        # A function will run each time user types something.
        self.ent_var.trace_add(mode='write',
                               callback=self.create_qr)
        self.entry = ctk.CTkEntry(self.buttons_frame,
                                  width=200,
                                  fg_color='#2e54e8',
                                  border_width=0,
                                  text_color='white',
                                  textvariable=self.ent_var,
                                  )
        self.entry.grid(row=0, column=0, padx=5)

        # save button
        self.button = ctk.CTkButton(self.buttons_frame,
                                    text='Save',
                                    fg_color='#2e54e8',
                                    width=80,
                                    command=self.save_image
                                    )
        self.button.grid(row=0, column=1, padx=5)

    def create_qr(self, *args):
        """Generates A qr code from provided text by user.
            It then updates the Label widget with new image.
        """
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=3,
        )

        # Add data to the QR code
        qr.add_data(self.entry.get())
        qr.make(fit=True)

        # Create an image from the QR code instance
        qr_image = qr.make_image(fill_color="black", back_color="white")

        # Convert qrcode.image.pil.PilImage to PIL.Image.Image
        self.pil_image = qr_image.get_image()
        # img = qrcode.make(self.entry.get()).get_image()
        new_qr = ctk.CTkImage(self.pil_image, size=(IMG_WIDTH, IMG_HEIGHT))
        self.label_widget.configure(image=new_qr)

    def save_image(self):
        """Prompts user for a file name and then saves the qr image."""
        if self.pil_image:  # Image already generated
            file_name = asksaveasfilename(title='Save location', defaultextension='.png')
            if file_name:  # If a name has been specified
                self.pil_image.save(file_name)


app = QrCodeGenerator()
app.mainloop()

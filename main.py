import tkinter as tk
from tkinter import ttk
from PIL import Image

import qrcode
from qrcode.image.pure import PyPNGImage

import customtkinter as ctk

ctk.set_default_color_theme('dark-blue')


class QrCodeGenerator(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('400x430')
        self.title('')
        self.iconbitmap('assets/empty.ico')
        self.minsize(width=120, height=0)

        self.top_frame = TopFrame(self, width=400, height=400, fg_color='green')
        # self.top_frame.pack(expand=True, fill='both')
        self.top_frame.place(relx=0.5, rely=0.4, anchor='center', relwidth=0.6, relheight=0.6)

        self.bottom_frame = BottomFrame(self,
                                        fg_color='#021fb3',
                                        height=100,
                                        corner_radius=20
                                        )
        self.bottom_frame.place(relx=0, rely=0.8, relwidth=1, relheight=0.35)


class TopFrame(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(master=parent, **kwargs)

        self.qr_img = ctk.CTkImage(Image.open('assets/Placeholder.png'), size=(300, 300))
        self.image_label = ctk.CTkLabel(self, image=self.qr_img, fg_color='red', text='')
        self.image_label.pack(expand=True, fill='both')


class BottomFrame(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(master=parent, **kwargs)
        self.parent = parent

        # Entry box
        self.buttons_frame = ctk.CTkFrame(self, fg_color='#021fb3')
        self.buttons_frame.place(relx=0.5, rely=0.3, anchor='center')
        # self.buttons_frame.pack(expand=True, fill='x', anchor='n')
        self.ent_var = tk.StringVar()
        self.ent_var.trace_add(mode='write',
                               callback=self.create_qr)
        self.entry = ctk.CTkEntry(self.buttons_frame,
                                  width=180,
                                  fg_color='#2e54e8',
                                  border_width=0,
                                  text_color='white',
                                  textvariable=self.ent_var
                                  )
        # self.entry.pack(side='left')
        self.entry.columnconfigure((0, 1, 2), weight=1)
        self.entry.grid(row=0, column=0, columnspan=2, padx=5)

        self.button = ctk.CTkButton(self.buttons_frame, text='Save', fg_color='#2e54e8', width=50)
        self.button.grid(row=0, column=2, padx=5)

    def create_qr(self, *args):
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
        pil_image = qr_image.get_image()
        # img = qrcode.make(self.entry.get()).get_image()
        self.new_qr = ctk.CTkImage(pil_image, size=(300, 300))
        self.parent.top_frame.image_label.configure(image=self.new_qr)


app = QrCodeGenerator()
app.mainloop()

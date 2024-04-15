#!/usr/bin/env python3

# qr_code.py
# This program allows a user to create a QR code for a url or text, with
# the user's own image as a logo in the middle.
# qr_code.py © 2024 by Milan Darji.
# Licensed under CC BY 4.0 | Creative Commons # Attribution 4.0 International.
# This license requires that reusers give credit to the creator. It allows 
# reusers to distribute, remix, adapt, and build upon the material in any 
# medium or format, even for commercial purposes.
# https://creativecommons.org/licenses/by/4.0/

# WARNING: Make sure to pre-install Pillow and qrcode libraries in your 
# virtual env for this project and definitely not generally or else 
# it can create conflicts

# import modules
from PIL import Image
import qrcode

# INITIALIZE THE VARIABLES
image_filename = 'Robot_image.png' # save image in in project directory
QR_filename = 'my_qrcode.png'       # filename for final QR code
# the QRCode can point to a url or to text
content = 'https://docs.google.com/forms/d/e/1FAIpQLSfekikVIpgNQtXxiyfSHA098Osuu4QGjz_lKPwY34n8qIgCEQ/viewform'
QRcolor = 'Blue'                    # QRColor holds name of color for QR code
background_color = 'White'
basewidth = 200                     # base width for logo

if __name__ == "__main__":
    
    logo = Image.open(image_filename)   # open image
    # adjust image size
    scale_width = (basewidth/float(logo.size[0]))
    height = int((float(logo.size[1])*float(scale_width)))
        # LANCZOS is an antialiasing, resize method based on convolutions
    logo = logo.resize((basewidth, height), Image.LANCZOS)
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

    # pass the content to QRcode
    qr.add_data(content)

    # generate the base QR code (no color yet)
    qr.make()

    # add color to the QR code
    QRimg = qr.make_image(
        fill_color=QRcolor, back_color=background_color).convert('RGB')

    # set size of QR code
    pos = ((QRimg.size[0] - logo.size[0]) // 2,
        (QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)

    # save the QR code in the project folder as PNG file
    QRimg.save(QR_filename)

    print('QR code saved as', QR_filename)
# QR_codes

qr_codes.py © 2024 by Milan Darji.

*Licensed under CC BY 4.0 | Creative Commons # Attribution 4.0 International.*
*This license requires that reusers give credit to the creator. It allows reusers to distribute, remix, adapt, and build upon the material in any medium or format, even for commercial purposes. https://creativecommons.org/licenses/by/4.0/*

## Basics
This program allows a user to create a QR code for a url or text, with the user's own image as a logo in the middle.

The image for the logo needs to be saved in the project folder. This program supports PNG and JPG formats but not SVG, RAW, HEIC, etc.

The QRCode can point to a url or display text.

**WARNING: Make sure to pre-install Pillow and qrcode libraries in your virtual env for this project and definitely not generally or else it can create conflicts.**

## Pillow module 

Replaces Python Image Library and is used to open the image for the qr code. Use PIL to call it. Documentation: https://pillow.readthedocs.io/en/stable/index.html.

## qrcode module 

Documentation: https://github.com/lincolnloop/python-qrcode.
Segno is another option for a QR code generation module. https://realpython.com/python-generate-qr-code/

## Variables

**image_filename:** filename of the image for the logo

**QR_filename:** filename for saving final QR code

**content:** the URL (or text you want displayed when the QR code is scanned)

**QRcolor:** color for QR code squares

**background_color:** obvious

**basewidth:** base width for logo, basically this determines the size of the logo
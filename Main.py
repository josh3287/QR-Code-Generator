#This is a QR Code Generator
#Install all necessary libraries
# Create a function that collects a text and converts it to a qrcode
# Save QR code
import qrcode

def generate_qrcode(text):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color = "black", back_color = "white")
    img.save("qrimag07.png")


url = input("Enter your URL: ")
generate_qrcode(url)
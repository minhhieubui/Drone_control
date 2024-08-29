import qrcode
from PIL import Image
from pyzbar import pyzbar
from pyzbar.pyzbar import decode



my_url = "https://www.facebook.com/hieuminhbuii"
img = qrcode.make(my_url)
# img.save('my_link1.png')


# img = Image.open('my_link2.png')
# qr_output = pyzbar.decode(img)
# print("my_link2.png decode:")
# print(qr_output)


# Detect QRCode







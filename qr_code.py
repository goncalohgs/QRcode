import qrcode

linkedin_link = 'https://www.linkedin.com/in/goncalohsilva/'

qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)

qr.add_data(linkedin_link)
qr.make()

img = qr.make_image(fill_color = 'black', back_color = 'white')

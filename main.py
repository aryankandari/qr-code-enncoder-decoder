import qrcode

data = "Hey! There, I am Aryan.\nIt is pleasure meeting you."

qr = qrcode.QRCode(version=1, box_size=4, border=5)

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill_color='red', back_color='white')

img.save('/Users/kandari/Workspace/Python/project/qr-code-enncoder-decoder/myqrcode2.png')
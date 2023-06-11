from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('/Users/kandari/Workspace/Python/project/qr-code-enncoder-decoder/myqrcode2.png')

result = decode(img)

print(result)
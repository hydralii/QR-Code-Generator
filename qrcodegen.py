import pyqrcode
import io

link = input("URL to transform onto a qr code: ")
url = pyqrcode.create(link)

url.svg('output.svg', scale=4)
buffer = io.BytesIO()
url.svg(buffer)
print("Done!")
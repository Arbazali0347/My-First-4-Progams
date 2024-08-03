import qrcode
new = qrcode.make("http//www.google.com")
content = new.save("ne_picture.png")

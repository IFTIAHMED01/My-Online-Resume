import qrcode

# Generating the qr static image for link
img = qrcode.make("https://iftiahmed01.github.io/My-Online-Resume/")

img.save("qr.png")
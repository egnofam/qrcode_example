# import modules
import qrcode

# create a varible on which we want to link a qrcode
qr=qrcode.QRCode(
    version = 1,
    box_size = 15,
    border = 10 
)


# add the link for the qrcode to open
data = "https://sites.google.com/view/emmanuelgnofam"
qr.add_data(data)
qr.make(fit=True)


# adding the color
img = qr.make_image(fill='black',back_color='white')
# save the qrcode as a png file
img.save("qrcodewithlink.png")
print("Hi Jesus")
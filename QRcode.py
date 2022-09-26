import os
import qrcode
import random
from tkinter import *
from tkinter import ttk
from PIL import Image

def codeMaker():
    randomNumber = random.randint(0,1000)
    img = qrcode.make(user_input.get())
    type(img)  # qrcode.image.pil.PilImage
    if os.path.exists(saveAs):
        img.save(saveName+str(randomNumber)+imgFormat)
    else:
        img.save(saveAs)

def previewQR():
    preImg = Image.open(saveAs)
    preImg.show()
    
imgFormat = ".png"
saveName = str("qr_code")
saveAs = str(saveName+imgFormat)

root = Tk()

frm = ttk.Frame(root, padding=10)
frm.grid()

user_input = StringVar()
entry = ttk.Entry(frm,textvariable=user_input).grid(column=0,row=6)

ttk.Label(frm, text="QRCodeMaker").grid(column=0,row=4)
ttk.Label(frm, text="Put link or text down below").grid(column=0,row=5)
ttk.Button(frm, text="Preview", command=previewQR).grid(column=1,row=7)
ttk.Button(frm, text="Create",command=codeMaker).grid(column=1,row=5)
ttk.Button(frm,text="Quit",command=root.destroy).grid(column=1,row=6)

root.mainloop()

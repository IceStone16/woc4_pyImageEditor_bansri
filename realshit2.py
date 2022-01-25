from tkinter import *
import tkinter as TK
from PIL import Image,ImageTk,ImageOps
import tkinter.filedialog
from tkinter.ttk import *
bc=0
def MainOpen():
    global img, im, MLabel,RSiz
    mainscreen.FName = TK.filedialog.askopenfilename( title="Open Your Image" ,filetypes=(("jpg files", "*.jpg"), ("jpeg files", "*.jpeg"),("png files", "*.png")))
    im = Image.open(mainscreen.FName)
    RSiz = im.resize((600,600))
    img = ImageTk.PhotoImage(RSiz)
    Lab1 = Label(WorkingArea, image=img).place(x=1, y=0)
def FLHor():
    global RSiz
    RSiz=RSiz.transpose(Image.FLIP_LEFT_RIGHT)
    global hi
    hi=ImageTk.PhotoImage(RSiz)
    Lab1=Label(WorkingArea,image=hi).place(x=1,y=0)
def FLVer():
    global RSiz
    RSiz=RSiz.transpose(Image.FLIP_TOP_BOTTOM)
    global hi
    hi=ImageTk.PhotoImage(RSiz)
    Lab1=Label(WorkingArea,image=hi).place(x=1,y=0)
def RTRit():
    global RSiz
    RSiz=RSiz.transpose(Image.ROTATE_270)
    global hi
    hi=ImageTk.PhotoImage(RSiz)
    Lab1=Label(WorkingArea,image=hi).place(x=1,y=0)
def RTLef():
    global RSiz
    RSiz=RSiz.transpose(Image.ROTATE_90)
    global hi
    hi=ImageTk.PhotoImage(RSiz)
    Lab1=Label(WorkingArea,image=hi).place(x=1,y=0)
def BlkNWht():
    global bc
    if bc%2==0:
        bc=3
        global Rsiz
        global bcha
        bcha=RSiz
        bcha=bcha.convert("L")
        global hi
        hi=ImageTk.PhotoImage(bcha)
        yechap=Label(WorkingArea,image=hi).place(x=1,y=0)
    else:
        hi=ImageTk.PhotoImage(RSiz)
        yechap=Label(WorkingArea,image=hi).place(x=1,y=0)
        bc=0
def InvrtC():
    global RSiz
    pixels = RSiz.load()
    for i in range(RSiz.size[0]):
        for j in range(RSiz.size[1]):
            x,y,z = pixels[i,j][0],pixels[i,j][1],pixels[i,j][2]
            x,y,z = abs(x-255), abs(y-255), abs(z-255)
            pixels[i,j] = (x,y,z)
    global hi
    hi=ImageTk.PhotoImage(RSiz)
    Lab1=Label(WorkingArea,image=hi).place(x=1,y=1)
def SAve():
        global RSiz
        RSiz= RSiz.save("save1.jpg")
mainscreen=TK.Tk()
mainscreen.title("Image Editor(beta version)")
WorkingArea=TK.Canvas(mainscreen,height=600,width=600,bg="black").grid(row=1,rowspan=12,column=0,columnspan=200)
OFile=TK.Button(mainscreen,text="Open File",bg="black",fg="white",command=MainOpen).grid(row=5,column=201,sticky="W")
SFile=TK.Button(mainscreen,text="Save File",bg="black",fg="white",command=SAve).grid(row=5,column=202,sticky="W")
cropS=TK.Button(mainscreen,text="Select Crop",bg="black",fg="white").grid(row=1,column=202)
flipH=TK.Button(mainscreen,text="Flip Horizontally",bg="black",fg="white",command=FLHor).grid(row=2,column=201)
flipV=TK.Button(mainscreen,text="Flip Vertically",bg="black",fg="white",command=FLVer).grid(row=2,column=203)
BandW=TK.Button(mainscreen,text="Black and White",bg="black",fg="white",command=BlkNWht).grid(row=4,column=201)
RotL=TK.Button(mainscreen,text="Rotate Left",bg="black",fg="white",command=RTLef).grid(row=3,column=201)
RotR=TK.Button(mainscreen,text="Rotate Right",bg="black",fg="white",command=RTRit).grid(row=3,column=203)
ContA=TK.Button(mainscreen,text="Invert Color",bg="black",fg="white",command=InvrtC).grid(row=4,column=203)
mainscreen.mainloop()



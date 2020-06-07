from tkinter import *

root =Tk()
topframe = Frame(root)
topframe.pack()

bottomframe =Frame(root)
bottomframe.pack(side=BOTTOM)

topbutton = Button(topframe,text="Click here",fg="Red")
bottombutton = Button(bottomframe,text="Click here",fg="Green")

topbutton.pack()
bottombutton.pack()

root.mainloop()

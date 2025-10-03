# Program Name: Assignment3.py
# Course: IT3883/Section W01
# Student Name: John Blair
# Assignment Number: 3
# Due Date: 10/03/2025
# Purpose: GUI MPG to KM/L conversion


from tkinter import *
from tkinter import StringVar

def conversion(self):
    try:
        KMPH=float(MPG.get())*0.425143707
        KMPH.set(str(KMPH))
    except:
        print("Error in Conversion")




root=Tk()
root.title("Fuel Efficiency Converter")
root.geometry("350x75")
Label(root,text="Please Enter MPG").grid(row=1,column=1,sticky=W)
MPG=StringVar()
Entry(root,textvariable=MPG,justify="center").grid(row=1,column=2,sticky=E)
KMPH=StringVar()
conversion(root)
Label(root,text="KM/L").grid(row=2,column=1,sticky=W)
Label(root,textvariable=KMPH).grid(row=2,column=2,sticky=W)
root.mainloop()




#0.425143707
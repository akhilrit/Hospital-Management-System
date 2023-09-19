import random
import time 
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox


def main():
    root=Tk()
    app= windows1(root)
    root.mainloop()

class windows1:
    def __init__(self,master):
        self.master=master
        self.master.title("Pharmacy management system")
        self.master.geometry('1350x750+0+0') # x-axis,y-axis,0,0 are location from top leftmost
        self.frame= Frame(self.master)
        self.frame.pack()

        self.LabelTitle=Label(self.frame, text="Pharmacy management system", font= ("arial", 40, "bold"), bd=10, relief= "sunken" )
        self.LableTitle.grid(  row=0,  column=0,  columnspan=2,  pady=2)


if __name__=="__main__":
    main()
 
# -*- coding: utf-8 -*-
"""


@author: Het Suthar
"""

from tkinter import *

main = Tk(className = " Calculator")
main.geometry("250x200")

main.after(1, lambda: main.focus_force())
main.configure(bg='cornflower blue')

a = StringVar()
b = StringVar()

lbNo1 = Label(main, text = "Enter Number 1:  ")
lbNo1.grid(row=0, column=0, pady=20, padx = 10)

txNo1 = Text(main, height = 1, width=15)
txNo1.grid(row= 0, column=1)

lbNo2 = Label(main, text = "Enter Number 2:  ")
lbNo2.grid(row=1, column=0)

txNo2 = Text(main, height = 1, width=15)
txNo2.grid(row= 1, column=1)



def add():
     ans = float(txNo1.get("1.0","end-1c")) + float(txNo2.get("1.0","end-1c"))
     lbAnswer.config(text ="Answer is : " + str( ans))
     lbAnswer.place(x = 100, y= 150)

def sub():
     ans = float(txNo1.get("1.0","end-1c")) -  float(txNo2.get("1.0","end-1c"))
     lbAnswer.config(text ="Answer is : " + str( ans))
     lbAnswer.place(x = 100, y= 150)
     
def mul():
     ans = float(txNo1.get("1.0","end-1c")) * float(txNo2.get("1.0","end-1c"))
     lbAnswer.config(text ="Answer is : " + str( ans))
     lbAnswer.place(x = 100, y= 150)
     
def div():
     ans = float(txNo1.get("1.0","end-1c")) / float(txNo2.get("1.0","end-1c"))
     lbAnswer.config(text ="Answer is : " + str( ans))
     lbAnswer.place(x = 100, y= 150)

btnAdd = Button(main, text = "+", width = 7, height = 1, command = add)
btnAdd.grid(row = 2, column = 0, pady=5, padx = 0)



    
btnSub = Button(main, text = "-", width = 7, height = 1, command = sub)
btnSub.grid(row = 2, column = 1, pady=5, padx = 0)

btnMul = Button(main, text = "*", width = 7, height = 1, command = mul)
btnMul.grid(row = 3, column = 0, pady=5, padx = 0)

btnDiv = Button(main, text = "/", width = 7, height = 1, command = div)
btnDiv.grid(row = 3, column = 1, pady=5, padx = 0)

lbAnswer = Label(main, text = "hl")
lbAnswer.place(x = 100, y= 150)

lbName = Label(main, text = "hetsuthar028")
lbName.place(x = 100, y = 180)

lbAnswer.place_forget()



mainloop()
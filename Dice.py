from tkinter import *
import random

window = Tk()
window.title("DICE")
window.geometry("780x450")
window.configure(bg='pale Turquoise2')
window.resizable(False,False)

def picknumber():
    lable["text"]= str(random.randint(1,6))
    lable1["text"]= str(random.randint(1,6))


button=Button(window, width=30 , height= 8, bg='green', fg='blue', command= picknumber, bd=3 ,
              relief=SUNKEN, activebackground='white', text='ROLL', font=("bold", 16))
button.grid(row=0, column=0, padx=10, pady=10)
button.place(relx=0.5, rely=0.26, anchor=CENTER)

lable=Label(window, width=30 , height=8,bg='orange', fg='purple',font=("bold",16) )
lable.grid(row=1, column=0)
lable.place(relx=0.5, rely=0.5)

lable1=Label(window, width=30 , height=8,bg='yellow', fg='purple',font=("bold",16) )
lable1.grid(row=1, column=1)
lable1.place(relx=0.03, rely=0.5)

lable_dice1=Label(window, text="Dice one" ,width=8 , height=2,bg='yellow', fg='black',font=("bold",16) )
lable_dice1.grid(row=1, column=1)
lable_dice1.place(relx=0.19, rely=0.5)

lable_dice2=Label(window, text="Dice two" ,width=8 , height=2,bg='orange', fg='black',font=("bold",16) )
lable_dice2.grid(row=1, column=0)
lable_dice2.place(relx=0.67, rely=0.5)



window.mainloop()




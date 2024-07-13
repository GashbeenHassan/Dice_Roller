from tkinter import *
import random

window = Tk()
window.title("ROLL THE DICE")
window.geometry("380x350")
window.configure(bg='pale Turquoise2')
window.resizable(False, False)

# Load dice images
dice_images = [PhotoImage(file=f'dice{i}.png') for i in range(1, 7)]

def picknumber():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    lable.config(image=dice_images[dice1 - 1])
    lable1.config(image=dice_images[dice2 - 1])

button = Button(window, width=20, height=2, bg='brown', fg='white', command=picknumber, bd=3,
                relief=SUNKEN, text='ROLL', font=("bold", 14))
button.grid(row=0, column=0, padx=10, pady=10)
button.place(relx=0.5, rely=0.12, anchor=CENTER)

lable = Label(window, width=200, height=150, bg='pale Turquoise2', fg='purple', font=("bold", 16))
lable.grid(row=1, column=0)
lable.place(relx=0.01, rely=0.3)

lable1 = Label(window, width=200, height=150, bg='pale Turquoise2', fg='purple', font=("bold", 16))
lable1.grid(row=1, column=1)
lable1.place(relx=0.45, rely=0.3)

lable_dice1 = Label(window, text="Dice one", width=8, height=1, bg='pale Turquoise2', fg='black', font=("bold", 16))
lable_dice1.grid(row=1, column=1)
lable_dice1.place(relx=0.14, rely=0.71)

lable_dice2 = Label(window, text="Dice two", width=8, height=1, bg='pale Turquoise2', fg='black', font=("bold", 16))
lable_dice2.grid(row=1, column=0)
lable_dice2.place(relx=0.58, rely=0.71)

window.mainloop()
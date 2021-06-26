import tkinter
from tkinter import *

root = tkinter.Tk()

orderLabel = Label(root, text="What do you want to order?")

items = [
    ("Pizza", "Pizza"),
    ("Noodles", "Noodles"),
    ("Fried Rice", "Fried Rice"),
    ("Burger", "Burger"),
    ("Sandwich", "Sandwich")
]

orderItem = StringVar()

for item, stuff in items:
    Radiobutton(root, text=item, variable=orderItem, value=stuff).pack(anchor=W)

def order(Item):
    myLabel = Label(root, text=f"You ordered {Item}")
    myLabel.pack()

orderButton = Button(root, text="Order", command=lambda: order(orderItem.get())).pack()

root.mainloop()
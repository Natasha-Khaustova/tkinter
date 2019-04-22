#12 random circle with random colors
from tkinter import *
from random import randint, choice
colors=['green', 'blue', 'red', 'yellow', 'pink', '#B918ff', '#FF01CC']

root = Tk()
canv = Canvas(root, width=400, height=400)
canv.pack()
for i in range(12):
    R = randint(10, 40)  # radius
    x = randint(R, 400 - R)
    y = randint(R, 400 - R)
    color = choice(colors)
    canv.create_oval(x-R, y-R, x+R, y+R, fill=color)
root.mainloop()

from tkinter import*

root=Tk()
root.geometry("300x150")

fr_top=Frame(root)
fr_top.pack(side="top", fill="both")
fr_bottom=Frame(root)
fr_bottom.pack(side="bottom", fill="both")
fr_bottom_of_top=Frame(root)
fr_bottom_of_top.pack(anchor="center")

btn1=Button(fr_top, text="1")
btn3=Button(fr_top, text="3")
btn1.pack(side="left")
btn3.pack(side="right")
btn2=Button(fr_bottom_of_top, text="2")
btn2.pack(side="right")
btn5=Button(fr_bottom, text="5")
btn5.pack(side="right")
btn4=Button(fr_bottom, text="4")
btn4.pack(side="right", padx=8)

root.mainloop()

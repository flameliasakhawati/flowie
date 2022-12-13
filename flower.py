import turtle
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

master = Tk()
p1 = PhotoImage(file = 'love.png')
master.iconphoto(False, p1)
messagebox.showinfo("Hi Alika cantik!!", "Ada sesuatu nih buat kamu..")
turtle.bgcolor("black")
turtle.speed(0)
turtle.hideturtle()
colors = ["powder blue","pink","maroon"]
for i in range(150):
    for c in colors:
        turtle.color(c)
        turtle.circle(190-i,90)
        turtle.lt(89)
        turtle.circle(190-i,90)
        turtle.lt(17)
        turtle.end_fill()

mainloop()
turtle.mainloop()

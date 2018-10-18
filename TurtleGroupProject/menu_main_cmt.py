#original version credit Craig Coleman @ 10.183.1.26/python/tk/cwc_project/menu_main_cwc.py  Used with permission.
import tkinter as tk
import turtle
from random import randint
from box import *
from psychtriangle import *
# *************************************************************************
#main tk (the menu starts below)
root = tk.Tk()
root.option_add("*Font", "courier")
root.wm_title("MENU - Caleb, Gerrardo, Ivan and Jaeden's Python Presentation")
root.minsize(400, 200)
a = tk.Button(root, text="Festive Triangle",font=('courier', '20') ,command=tri)
b = tk.Button(root, text="Box Spiral",font=('courier', '20') ,command=spiral)\
#c = tk.Button(root, text="Box Spiral",font=('courier', '20') ,command=spiral)
#d = tk.Button(root, text="Box Spiral",font=('courier', '20') ,command=spiral)
t1 = tk.Label(root, text="Festive Traingle: Caleb T",font=('courier', '10'))
t2 = tk.Label(root, text=" Box Spiral: Jaeden Brewer",font=('courier', '10'))
#t3 = tk.Label(root, text = "SOAR (Stack of Activation Records)",font=('courier', '10'))
#t4 =tk.Label(root, text=" Box Spiral: Jaeden Brewer",font=('courier', '10'))
a.pack()
b.pack()
#c.pack()
#d.pack()
t1.pack()
t2.pack()
#t3.pack()
#t4.pack()
root.mainloop()

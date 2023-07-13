
from tkinter import*



root = Tk()
root.geometry = ()
root.title = ("All In One")

main_menu = Menu(root)
root.config(menu = main_menu)

def calculator():
    Label()

options_menu = Menu(main_menu)
main_menu.add_cascade(label="Options",menu=options_menu)
options_menu.add_command(label="Calculator", command=calculator)

formula = StringVar()
entered_formula = ""

label_calculator = Label(root, textvariable=formula,height = "2",width= "50")
label_calculator.pack()

frame = Frame(root)
frame.pack()

def button_press():
    

button0= Button(frame,text="0",command = lambda:button_press(0)) 
button0.grid(row=0,column=0)

button1= Button(frame,text="1",command = lambda:button_press(1)) 
button1.grid(row=1,column=0)

button2= Button(frame,text="2",command = lambda:button_press(2)) 
button2.grid(row=2,column=0)

button3= Button(frame,text="3",command = lambda:button_press(3)) 
button3.grid(row=0,column=1)

button4= Button(frame,text="4",command = lambda:button_press(4)) 
button4.grid(row=1,column=1)

button5= Button(frame,text="5",command = lambda:button_press(5)) 
button5.grid(row=2,column=1)

button6= Button(frame,text="6",command = lambda:button_press(6)) 
button6.grid(row=0,column=2)

button7= Button(frame,text="7",command = lambda:button_press(7)) 
button7.grid(row=1,column=2)

button8= Button(frame,text="8",command = lambda:button_press(8)) 
button8.grid(row=2,column=2)

button9= Button(frame,text="9",command = lambda:button_press(9)) 
button9.grid(row=0,column=3)


root.mainloop()
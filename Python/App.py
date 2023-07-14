#All In one App
#importing tkinter
from tkinter import*

#opening window
root = Tk()
root.title = ("All In One")

#A basic menu bar setup for future iterations
main_menu = Menu(root)
root.config(menu = main_menu)


calculation=""
#placeholder function for now
def calculator(): 
    #This function allows a live display of the numbers clicked on the calculator
    #I have set the calculation as a global variable so i can use it for other functions
    def display(user_input):
        global calculation
        calculation += str(user_input)
        display_text.delete(1.0,'end')
        display_text.insert(1.0,calculation)

    #This fuction does the calculation part
    #Using try and except I evaluate(eval) the calculation once its done it displays the new number
    #but if the evaluation goes wrong the program will reset.
    def calculate():
        global calculation
        try:
            calculation = str(eval(calculation))
            display_text.delete(1.0)
            display_text.insert(1.0,calculation)
        except:
            clear()
            display_text.insert(1.0,"Error, please check your entry")
            
    #This function is for the clear button on the calculator, if clicked the display box clears.
    def clear():
        global calculation
        calculation=""
        display_text.delete(1.0,'end')

        
    #These are all the buttons/texts/labels used for the calculator
    #Lambda records the buttons clicked then sends the buttons clicked back to the display function
    #Then when equal is clicked the calculate function uses the data from display function
    #to print the final answer
    display_text = Text(root,height='5',width='10',bg='blue')
    display_text.grid(rowspan= 5,column=0)

    button0= Button(root,text="0",command = lambda:display(0)) 
    button0.grid(row=1,column=1)

    button1= Button(root,text="1",command = lambda:display(1)) 
    button1.grid(row=2,column=1)

    button2= Button(root,text="2",command = lambda:display(2)) 
    button2.grid(row=3,column=1)

    button3= Button(root,text="3",command = lambda:display(3)) 
    button3.grid(row=1,column=2)

    button4= Button(root,text="4",command = lambda:display(4)) 
    button4.grid(row=2,column=2)

    button5= Button(root,text="5",command = lambda:display(5)) 
    button5.grid(row=3,column=2)

    button6= Button(root,text="6",command = lambda:display(6)) 
    button6.grid(row=1,column=3)

    button7= Button(root,text="7",command = lambda:display(7)) 
    button7.grid(row=2,column=3)

    button8= Button(root,text="8",command = lambda:display(8)) 
    button8.grid(row=3,column=3)

    button9= Button(root,text="9",command = lambda:display(9)) 
    button9.grid(row=1,column=4)

    subtract_button = Button(root,text='-',command=lambda:display("-"))
    subtract_button.grid(row=2,column = 4)

    add_button = Button(root,text='+',command=lambda:display("+"))
    add_button.grid(row=3,column=4)

    divide_button = Button(root,text ='/',command=lambda:display("/"))
    divide_button.grid(row=1,column=5)

    multiply_button = Button(root,text='x',command=lambda:display("*"))
    multiply_button.grid(row=2,column=5)

    clear_button = Button(root,text='C',command= clear)
    clear_button.grid(row=3,column=5)

    equal_button = Button(root,text='=',command=calculate)
    equal_button.grid(row=0,column=5)


#More of the menubar
options_menu = Menu(main_menu)
main_menu.add_cascade(label="Options",menu=options_menu)
options_menu.add_command(label="Calculator", command=calculator)



root.mainloop()
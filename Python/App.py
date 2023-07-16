#All In one App
#importing tkinter and messagebox
from tkinter import*
from tkinter import messagebox

#opening window
root = Tk()
root.title = ("All In One")
root.resizable(0,0)

#A basic menu bar setup for future iterations
main_menu = Menu(root)
root.config(menu = main_menu,bg="#40e0d0")


solve=""
#This function integrates calculator into the menubar 
def calculator(): 
    
    #This function allows a live display of the numbers clicked on the calculator
    #I have set the calculation as a global variable so i can use it for other functions
    def display(user_input):
        global solve
        solve += str(user_input)
        display_text.delete(1.0,'end')
        display_text.insert(1.0,solve)

    #This fuction does the calculation part
    #Using try and except I evaluate(eval) the calculation once its done it displays the new number
    #but if the evaluation goes wrong the program will reset.
    def calculate():
        global solve
        try:
            solve = str(eval(solve))
            display_text.delete(1.0,'end')
            display_text.insert(1.0,solve)
        except:
            clear()
            display_text.insert(1.0,"Error, please check your entry")
            
    #This function is for the clear button on the calculator, if clicked the display box clears.
    #A messagebox popup will allow user to confirm their choice
    def clear():
        if messagebox.askyesno(message="This will clear your calculation are you sure?") == True:
            global solve
            solve=""
            display_text.delete(1.0,'end')
        else:
            pass

       

        
    #These are all the buttons/texts/labels used for the calculator
    #Lambda records the buttons clicked then sends the buttons clicked back to the display function
    #Then when equal is clicked the calculate function uses the data from display function
    #to print the final answer
    display_text = Text(root,height='2',width='20',bg='#cccccc',font=('xenara','15'))
    display_text.grid(row=0,columnspan=5,)
    
    button0= Button(root,text="0",command = lambda:display(0),
                    height = '2', width = '2',font='xenara',bg='#8aecff') 
    
    button0.grid(row=1,column=0)

    button1= Button(root,text="1",command = lambda:display(1),bg='#8aecff',
                    height = '2', width = '2',font='xenara') 
    
    button1.grid(row=1,column=1)

    button2= Button(root,text="2",command = lambda:display(2),bg='#8aecff',
                    height = '2', width = '2',font='xenara') 
    
    button2.grid(row=1,column=2)

    button3= Button(root,text="3",command = lambda:display(3),bg='#8aecff',
                    height = '2', width = '2',font='xenara') 
    
    button3.grid(row=1,column=3)

    button4= Button(root,text="4",command = lambda:display(4),bg='#8aecff',
                    height = '2', width = '2',font='xenara') 
    
    button4.grid(row=1,column=4)

    button5= Button(root,text="5",command = lambda:display(5),bg='#8aecff',
                    height = '2', width = '2',font='xenara') 
    
    button5.grid(row=2,column=0)

    button6= Button(root,text="6",command = lambda:display(6),bg='#8aecff',
                    height = '2', width = '2',font='xenara') 
    
    button6.grid(row=2,column=1)

    button7= Button(root,text="7",command = lambda:display(7),bg='#8aecff',
                    height = '2', width = '2',font='xenara') 
    
    button7.grid(row=2,column=2)

    button8= Button(root,text="8",command = lambda:display(8),bg='#8aecff',
                    height = '2', width = '2',font='xenara') 
    
    button8.grid(row=2,column=3)

    button9= Button(root,text="9",command = lambda:display(9),bg='#8aecff',
                    height = '2', width = '2',font='xenara')
    
    button9.grid(row=2,column=4)

    subtract_button = Button(root,text='-',command=lambda:display("-"),bg='#8aecff',
                             height = '2', width = '2',font='xenara')
    
    subtract_button.grid(row=3,column = 0)

    add_button = Button(root,text='+',command=lambda:display("+"),bg='#8aecff',
                        height = '2', width = '2',font='xenara')
    
    add_button.grid(row=3,column=1)

    divide_button = Button(root,text ='/',command=lambda:display("/"),bg='#8aecff',
                           height = '2', width = '2',font='xenara')
    
    divide_button.grid(row=3,column=2)

    multiply_button = Button(root,text='x',command=lambda:display("*"),bg='#8aecff',
                             height = '2', width = '2',font='xenara')
    
    multiply_button.grid(row=3,column=3)

    clear_button = Button(root,text='C',command= clear,
                          height = '2', width = '2',bg='#FF0000',font='xenara')
    
    clear_button.grid(row=3,column=4)

    equal_button = Button(root,text='=',command=calculate,
                          height = '2', width = '2',background="#86DC3D",font='xenara')
    
    equal_button.grid(row=4,column=2)
    
    decimal_button = Button(root,text='.',command=lambda:display("."),bg='#8aecff',
                             height = '2', width = '2',font='xenara')
    decimal_button.grid(row=4,column=3)

#More of the menubar
options_menu = Menu(main_menu)
main_menu.add_cascade(label="Options",menu=options_menu)
options_menu.add_command(label="Calculator", command=calculator)



root.mainloop()
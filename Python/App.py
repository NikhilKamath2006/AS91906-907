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

def exit():
    confirm = messagebox.askyesno(message='Do you want to exit?')
    if confirm ==True:
        root.quit
    elif confirm != True:
        pass


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

    decimal_button = Button(root,text='.',command=lambda:display("."),bg='#8aecff',
                             height = '2', width = '2',font='xenara')
    decimal_button.grid(row=4,column=3)


    #This function is for the clear button on the calculator, if clicked the display box clears.
    #A messagebox popup will allow user to confirm their choice
    def clear():
        if messagebox.askyesno(message="This will clear your calculation are you sure?") == True:
            global solve
            solve=""
            display_text.delete(1.0,'end')
        else:
            pass
    
    clear_button = Button(root,text='C',command= clear,
                          height = '2', width = '2',bg='#FF0000',font='xenara')
    
    clear_button.grid(row=3,column=4)

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

    equal_button = Button(root,text='=',command=calculate,
                          height = '2', width = '2',background="#86DC3D",font='xenara')
    
    equal_button.grid(row=4,column=2)
    

def tax():
     #This function calculates the tax depending on the amount of money earned
    def calculate_tax():
        global after_tax
        global tax_topay
        int_salary = int(salary.get())
        if 0< int_salary <= (14000):
            after_tax = int_salary*0.895
            tax_topay = int_salary*0.105
            taxed_label.config(text=('You will have $',after_tax,"after tax, so you will be paying $",tax_topay,"tax"))
            
        elif 14000< int_salary <= 48000:
            tax_topay = ((int_salary-14000)*0.175)+1470
            after_tax = int_salary-tax_topay
            taxed_label.config(text=('You will have $',after_tax,"after tax, so you will be paying $",tax_topay,"tax"))
        elif 48000< int_salary <= 70000:
            tax_topay = ((int_salary-48000)*0.3)+7420
            after_tax = int_salary-tax_topay
            taxed_label.config(text=('You will have $',after_tax,"after tax, so you will be paying $",tax_topay,"tax"))
        elif 70000< int_salary <= 180000:
            tax_topay = ((int_salary-70000)*0.33)+14020
            after_tax = int_salary-tax_topay
            taxed_label.config(text=('You will have $',after_tax,"after tax, so you will be paying $",tax_topay,"tax"))
        elif 180000< int_salary <= 10000000000:
            
            tax_topay = ((int_salary-180000)*0.39)+50320
            after_tax = int_salary-tax_topay
            taxed_label.config(text=('You will have $',after_tax,"after tax, so you will be paying $",tax_topay,"tax"))
        else:
            messagebox.showerror('invalid','Please check your entry again')
    #labels and buttons for the tax calculator
    tax_label = Label(root,text='What is your yearly income?',bg="#ffdb58",font='xenara',borderwidth=5,relief='groove')
    tax_label.grid()
    taxed_label2 = Label(root,bg='#40e0d0',font='xenara')
    taxed_label2.grid()
    taxed_label = Label(root,bg="#40e0d0",font='xenara')
    taxed_label.grid()
    salary = Entry(root)
    salary.grid()
    tax_button = Button(root,text='Tax Me!',command = calculate_tax ,bg="#ffdb58",font='xenara')
    tax_button.grid()


#More of the menubar
options_menu = Menu(main_menu)
main_menu.add_cascade(label="Options",menu=options_menu)
options_menu.add_command(label="Calculator", command=calculator)
options_menu.add_command(label='Exit', command= exit)
options_menu.add_command(label='Tax', command= tax)
root.mainloop()
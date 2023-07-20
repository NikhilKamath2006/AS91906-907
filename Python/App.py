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


frame1 = Frame(root,bg="#40e0d0")
frame2 = Frame(root,bg="#40e0d0")

welcome_label=Label(root,text='Welcome to the smart calculator!',bg='yellow',font='xenara',height='5',borderwidth=5,relief='solid')
welcome_label.grid(columnspan=5,rowspan=5)

solve=""
after_tax=''
tax_topay=''

def frame_forget():
    welcome_label.grid_forget()
    frame1.grid_forget()
    frame2.grid_forget()

#This function integrates calculator into the menubar 
def frame_calculator():
    frame_forget()
    frame1.grid() 

    
    #This function allows a live display of the numbers clicked on the calculator
    #I have set the calculation as a global variable so i can use it for other functions
    def display(user_input):
        global solve
        solve += str(user_input)
        live_display.delete(1.0,'end')
        live_display.insert(1.0,solve)

    #This fuction does the calculation part
    #Using try and except I evaluate(eval) the calculation once its done it displays the new number
    #but if the evaluation goes wrong the program will reset.
    def calculate():
        global solve
        try:
            solve = str(eval(solve))
            live_display.delete(1.0,'end')
            live_display.insert(1.0,solve)
        except:
            clear()
            live_display.insert(1.0,"Error, please check your entry")
            
    #This function is for the clear button on the calculator, if clicked the display box clears.
    #A messagebox popup will allow user to confirm their choice
    def clear():
        if messagebox.askyesno(message="This will clear your calculation are you sure?") == True:
            global solve
            solve=""
            live_display.delete(1.0,'end')
        else:
            pass

    def decimal():
        pass

        
    #These are all the buttons/texts/labels used for the calculator
    #Lambda records the buttons clicked then sends the buttons clicked back to the display function
    #Then when equal is clicked the calculate function uses the data from display function
    #to print the final answer
    live_display = Text(frame1,height='2',width='20',bg='#cccccc',font=('xenara','15'))
    live_display.grid(row=0,columnspan=5,)
    
    button0= Button(frame1,text="0",command = lambda:display(0),
                    height = '2', width = '2',font='xenara',bg='#8aecff') 
    
    button0.grid(row=1,column=0)

    button1= Button(frame1,text="1",command = lambda:display(1),bg='#8aecff',
                    height = '2', width = '2',font='xenara') 
    
    button1.grid(row=1,column=1)

    button2= Button(frame1,text="2",command = lambda:display(2),bg='#8aecff',
                    height = '2', width = '2',font='xenara') 
    
    button2.grid(row=1,column=2)

    button3= Button(frame1,text="3",command = lambda:display(3),bg='#8aecff',
                    height = '2', width = '2',font='xenara') 
    
    button3.grid(row=1,column=3)

    button4= Button(frame1,text="4",command = lambda:display(4),bg='#8aecff',
                    height = '2', width = '2',font='xenara') 
    
    button4.grid(row=1,column=4)

    button5= Button(frame1,text="5",command = lambda:display(5),bg='#8aecff',
                    height = '2', width = '2',font='xenara') 
    
    button5.grid(row=2,column=0)

    button6= Button(frame1,text="6",command = lambda:display(6),bg='#8aecff',
                    height = '2', width = '2',font='xenara') 
    
    button6.grid(row=2,column=1)

    button7= Button(frame1,text="7",command = lambda:display(7),bg='#8aecff',
                    height = '2', width = '2',font='xenara') 
    
    button7.grid(row=2,column=2)

    button8= Button(frame1,text="8",command = lambda:display(8),bg='#8aecff',
                    height = '2', width = '2',font='xenara') 
    
    button8.grid(row=2,column=3)

    button9= Button(frame1,text="9",command = lambda:display(9),bg='#8aecff',
                    height = '2', width = '2',font='xenara')
    
    button9.grid(row=2,column=4)

    subtract_button = Button(frame1,text='-',command=lambda:display("-"),bg='#8aecff',
                             height = '2', width = '2',font='xenara')
    
    subtract_button.grid(row=3,column = 0)

    add_button = Button(frame1,text='+',command=lambda:display("+"),bg='#8aecff',
                        height = '2', width = '2',font='xenara')
    
    add_button.grid(row=3,column=1)

    divide_button = Button(frame1,text ='/',command=lambda:display("/"),bg='#8aecff',
                           height = '2', width = '2',font='xenara')
    
    divide_button.grid(row=3,column=2)

    multiply_button = Button(frame1,text='x',command=lambda:display("*"),bg='#8aecff',
                             height = '2', width = '2',font='xenara')
    
    decimal_button = Button(frame1,text='.',command=lambda:display("."),bg='#8aecff',
                             height = '2', width = '2',font='xenara')
    decimal_button.grid(row=4,column=3)
    
    multiply_button.grid(row=3,column=3)

    clear_button = Button(frame1,text='C',command= clear,
                          height = '2', width = '2',bg='#FF0000',font='xenara')
    
    clear_button.grid(row=3,column=4)

    equal_button = Button(frame1,text='=',command=calculate,
                          height = '2', width = '2',background="#86DC3D",font='xenara')
    
    equal_button.grid(row=4,column=2)
    
#framing for tax
def tax_frame():
    frame_forget()
    frame2.grid()

    #calculation for tax
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
   
    #label and buttons for tax calculator
    tax_label = Label(frame2,text='What is your yearly income?',bg="#ffdb58",font='xenara',borderwidth=5,relief='groove')
    tax_label.grid()
    taxed_label = Label(frame2,bg="#40e0d0",font='xenara')
    taxed_label.grid()
    salary = Entry(frame2)
    salary.grid()
    tax_button = Button(frame2,text='Tax Me!',command = calculate_tax ,bg="#ffdb58",font='xenara')
    tax_button.grid()

#More of options menu
options_menu = Menu(main_menu)
main_menu.add_cascade(label="Options",menu=options_menu)
options_menu.add_command(label="Calculator", command=frame_calculator) 
options_menu.add_command(label="Exit", command= root.quit)
options_menu.add_command(label="Tax", command=tax_frame)
root.mainloop()

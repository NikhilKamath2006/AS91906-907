#importing tkinter and messgaebox
from tkinter import*
from tkinter import messagebox

#setting up main window
root = Tk()
main_menu = Menu(root)
root.config(menu = main_menu,bg="#40e0d0")


solve = ""

#Class for the calculator feature
class   Calculator:
    def __init__(self,calc_frame):
        #These are all the buttons/texts/labels used for the calculator
        #Lambda records the buttons clicked then sends the buttons clicked back to the display function
        #Then when equal is clicked the calculate function uses the data from display function
        #to print the final answer
        frame_1 = Frame(calc_frame)
        frame_1.grid()

        self.live_display = Text(frame_1,height='2',width='20',bg='#cccccc',font=('xenara','15'))
        self.live_display.grid(row=0,columnspan=5,)
        
        self.button0= Button(frame_1,text="0",command = lambda:self.display(0),
                        height = '2', width = '2',font='xenara',bg='#8aecff') 
        
        self.button0.grid(row=1,column=0)

        self.button1= Button(frame_1,text="1",command = lambda:self.display(1),bg='#8aecff',
                        height = '2', width = '2',font='xenara') 
        
        self.button1.grid(row=1,column=1)

        self.button2= Button(frame_1,text="2",command = lambda:self.display(2),bg='#8aecff',
                        height = '2', width = '2',font='xenara') 
        
        self.button2.grid(row=1,column=2)

        self.button3= Button(frame_1,text="3",command = lambda:self.display(3),bg='#8aecff',
                        height = '2', width = '2',font='xenara') 
        
        self.button3.grid(row=1,column=3)

        self.button4= Button(frame_1,text="4",command = lambda:self.display(4),bg='#8aecff',
                        height = '2', width = '2',font='xenara') 
        
        self.button4.grid(row=1,column=4)

        self.button5= Button(frame_1,text="5",command = lambda:self.display(5),bg='#8aecff',
                        height = '2', width = '2',font='xenara') 
        
        self.button5.grid(row=2,column=0)

        self.button6= Button(frame_1,text="6",command = lambda:self.display(6),bg='#8aecff',
                        height = '2', width = '2',font='xenara') 
        
        self.button6.grid(row=2,column=1)

        self.button7= Button(frame_1,text="7",command = lambda:self.display(7),bg='#8aecff',
                        height = '2', width = '2',font='xenara') 
        
        self.button7.grid(row=2,column=2)

        self.button8= Button(frame_1,text="8",command = lambda:self.display(8),bg='#8aecff',
                        height = '2', width = '2',font='xenara') 
        
        self.button8.grid(row=2,column=3)

        self.button9= Button(frame_1,text="9",command = lambda:self.display(9),bg='#8aecff',
                        height = '2', width = '2',font='xenara')
        
        self.button9.grid(row=2,column=4)

        self.subtract_button = Button(frame_1,text='-',command=lambda:self.display("-"),bg='#8aecff',
                                height = '2', width = '2',font='xenara')
        
        self.subtract_button.grid(row=3,column = 0)

        self.add_button = Button(frame_1,text='+',command=lambda:self.display("+"),bg='#8aecff',
                            height = '2', width = '2',font='xenara')
        
        self.add_button.grid(row=3,column=1)

        self.divide_button = Button(frame_1,text ='/',command=lambda:self.display("/"),bg='#8aecff',
                            height = '2', width = '2',font='xenara')
        
        self.divide_button.grid(row=3,column=2)

        self.multiply_button = Button(frame_1,text='x',command=lambda:self.display("*"),bg='#8aecff',
                                height = '2', width = '2',font='xenara')
        
        self.decimal_button = Button(frame_1,text='.',command=lambda:self.display("."),bg='#8aecff',
                                height = '2', width = '2',font='xenara')
        self.decimal_button.grid(row=4,column=3)
        
        self.multiply_button.grid(row=3,column=3)

        self.clear_button = Button(frame_1,text='C',command= self.clear,
                            height = '2', width = '2',bg='#FF0000',font='xenara')
        
        self.clear_button.grid(row=3,column=4)

        self.equal_button = Button(frame_1,text='=',command= self.calculate,
                            height = '2', width = '2',background="#86DC3D",font='xenara')
        
        self.equal_button.grid(row=4,column=2)
            
        
    def display(self,user_input):
        global solve
        solve += str(user_input)
        self.live_display.delete(1.0,'end')
        self.live_display.insert(1.0,solve)

    #This fuction does the calculation part
    #Using try and except I evaluate(eval) the calculation once its done it displays the new number
    #but if the evaluation goes wrong the program will reset.
    def calculate(self):
        global solve
        try:
            solve = str(eval(solve))
            self.live_display.delete(1.0,'end')
            self.live_display.insert(1.0,solve)
        except:
            self.clear()
            self.live_display.insert(1.0,"Error, please check your entry")
            
    #This function is for the clear button on the calculator, if clicked the display box clears.
    #A messagebox popup will allow user to confirm their choice
    def clear(self):
        if messagebox.askyesno(message="This will clear your calculation are you sure?") == True:
            global solve
            solve=""
            self.live_display.delete(1.0,'end')
        else:
            pass



        
#Class for the tax feature
class Tax:
    def __init__(self,tax_frame):
        frame_2 = Frame(tax_frame)
        frame_2.grid()

        #These are the labels and buttons used for the tax calculator
        self.tax_label = Label(tax_frame,text='What is your yearly income?',bg="#ffdb58",font='xenara',borderwidth=5,relief='groove')
        self.tax_label.grid()

        self.taxed_label = Label(tax_frame,bg="#40e0d0",font='xenara')
        self.taxed_label.grid()
        
        self.salary = Entry(root)
        self.salary.grid()
        
        self.tax_button = Button(tax_frame,text='Tax Me!',command = self.calculate_tax ,bg="#ffdb58",font='xenara')
        self.tax_button.grid()
    #This function calculates the tax depending on the salary using if statments
    def calculate_tax(self):
        int_salary = int(self.salary.get())
        if 0< int_salary <= (14000):
            after_tax = int_salary*0.895
            tax_topay = int_salary*0.105
            self.taxed_label.config(text=f'You will have ${after_tax} after tax, so you will be paying ${tax_topay} in tax')
        
            
        elif 14000< int_salary <= 48000:
            tax_topay = ((int_salary-14000)*0.175)+1470
            after_tax = int_salary-tax_topay
            self.taxed_label.config(text=f'You will have ${after_tax} after tax, so you will be paying ${tax_topay} in tax')
        
        elif 48000< int_salary <= 70000:
            tax_topay = ((int_salary-48000)*0.3)+7420
            after_tax = int_salary-tax_topay
            self.taxed_label.config(text=f'You will have ${after_tax} after tax, so you will be paying ${tax_topay} in tax')
        
        elif 70000< int_salary <= 180000:
            tax_topay = ((int_salary-70000)*0.33)+14020
            after_tax = int_salary-tax_topay
            self.taxed_label.config(text=f'You will have ${after_tax} after tax, so you will be paying ${tax_topay} in tax')
        
        elif 180000< int_salary <= 10000000000:
            tax_topay = ((int_salary-180000)*0.39)+50320
            after_tax = int_salary-tax_topay
            self.taxed_label.config(text=f'You will have ${after_tax} after tax, so you will be paying ${tax_topay} in tax')
        
        #These two statments are for invalid entries by the user
        elif self.salary.get != int:
            messagebox.showerror('Error','Error,Please check entry')
        else :
            messagebox.showerror('Error','Error,Please check entry')


#Linking the classes to menubar
options_menu = Menu(main_menu)
main_menu.add_cascade(label="Options",menu=options_menu)
options_menu.add_command(label="Calculator", command=Calculator(root)) 
options_menu.add_command(label="Exit", command= root.quit)
options_menu.add_command(label="Tax", command =Tax(root))
    
                               
root.mainloop()
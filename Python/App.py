from tkinter import*


root = Tk()
root.geometry = ('500x500')

mainmenu = Menu

def _quit():  
   root.quit()  
   root.destroy()  
   exit()  
#Create Menu   
mainmenu=Menu(root)  
root.config(menu=mainmenu)  
#File Menu  
main= Menu(mainmenu)  
main.add_command(label="Exit", command=_quit)  
mainmenu.add_separator(label="Options", menu= main)
  



root.mainloop()
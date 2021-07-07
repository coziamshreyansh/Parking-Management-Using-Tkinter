import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from gui2 import gui2



win= tk.Tk()
win.title('Parking Made Easy') 
win.geometry('600x500')     #width,height of win window
#To bring window in center of the screen of user
win.geometry("{}x{}+{}+{}".format(600, 500, int((win.winfo_screenwidth()/2) - (600/2)), int((win.winfo_screenheight()/2) - (500/2))))
win.configure(bg="light green")

#create labels

namelabel=tk.Label(win, text=" Customer Name ", bg="yellow")
namelabel.grid(row=0, column=0, padx=10, pady=10)

timelabel=tk.Label(win, text=" Entry Time ", bg="yellow")
timelabel.grid(row=1, column=0, padx=10, pady=10)

infolabel=tk.Label(win, text=" Vehicle Info ", bg="yellow")
infolabel.grid(row=2, column=0, padx=10, pady=10)

typelabel=tk.Label(win, text=" Car Type ", bg="yellow")
typelabel.grid(row=3, column=0, padx=10, pady=10)

#create entrybox
global name_var, emergencyfuel_var, carwash_var, detail_var

name_var=tk.StringVar(win)
name_eb = tk.Entry(win, width=16,bg= 'blue', textvariable= name_var)
name_eb.grid(row=0, column=1)
name_eb.focus()

time_var= tk.StringVar(win)
time_eb = tk.Entry(win, width=16,bg= 'blue', textvariable= time_var)
time_eb.grid(row=1, column=1, padx=10, pady=10)

info_var=tk.StringVar(win)
info_eb = tk.Entry(win, width=16,bg= 'blue', textvariable=  info_var)
info_eb.grid(row=2, column=1, padx=10, pady=10)

#create combobox
cartype_var=tk.StringVar(win)
cartype = ttk.Combobox(win, width=16 , textvariable= cartype_var )
cartype ['values'] = (' SUV', ' SEDAN' ,' HATCHBACK' , ' UTILITY'  )
cartype.current(0) #bydefault value show
cartype.grid(row=3, column=1, padx=10, pady=10)





#button's function is defined in this manner
def action():
    messagebox.showinfo("Done!", "Your details submitted successfully!!!") #display a messagebox
    win.destroy() #destroy/close the current window 
    gui2(name_var,cartype_var) #execute the another window for further procedure of entering details

#create button
ok_button=tk.Button(win, text="OK", bg="red" , command=action)
ok_button.grid(row=4,column=2, padx=10, pady=10)

win.mainloop()





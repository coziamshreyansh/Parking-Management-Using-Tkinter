import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from gui3 import gui3

def gui2(name_var,cartype_var):
    win= tk.Tk()
    win.title('Parking Made Easy')
    win.geometry('600x500')     #width,height of win window

    win.focus_force() #To bring the window in focus

    #To bring window in center of the screen of user
    win.geometry("{}x{}+{}+{}".format(600, 500, int((win.winfo_screenwidth()/2) - (600/2)), int((win.winfo_screenheight()/2) - (500/2))))

    win.configure(background="light green")

    #create labels

    fuellabel=tk.Label(win, text=" Emergency Fuel ", bg="yellow")
    fuellabel.grid(row=0, column=0, padx=10, pady=10)

    detaillabel=tk.Label(win, text=" Residency Detail", bg="yellow")
    detaillabel.grid(row=1, column=0, padx=10, pady=10)

    washlabel=tk.Label(win, text=" Car Wash ", bg="yellow")
    washlabel.grid(row=2, column=0, padx=10, pady=10)

   


    #create combobox
    emergencyfuel_var=tk.StringVar(win)
    emergencyfuel = ttk.Combobox(win, width=25 , textvariable= emergencyfuel_var)
    emergencyfuel ['values'] = (' YES ', ' NO' )
    emergencyfuel.grid(row=0, column=1, padx=10, pady=10)

    residency_var = tk.StringVar(win)
    residency = ttk.Combobox(win, width=25 , textvariable= residency_var)
    residency ['values'] = (' YES ', ' NO' )
    residency.grid(row=1, column=1, padx=10, pady=10)

    carwash_var=tk.StringVar(win)
    carwash= ttk.Combobox(win, width=25 , textvariable= carwash_var )
    carwash ['values'] = (' YES ', ' NO' )
    carwash.grid(row=2, column=1, padx=10, pady=10)
    
    def action():
        messagebox.showinfo("Done!", "Your details submitted successfully!!!")
        win.destroy()
        gui3(name_var,cartype_var,emergencyfuel_var,carwash_var,residency_var) #create this in another .py file similarly... this will have a function to show the result
        
    ok_button=tk.Button(win, text="OK", command=action, bg="red" )
    ok_button.grid(row=4,column=2, padx=10, pady=10)

    win.mainloop()
    
if __name__ == "__main__":                  #To run the main program indiviually
    gui2()

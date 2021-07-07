import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def gui3(name_var,cartype_var,emergencyfuel_var,carwash_var,residency_var):
    win= tk.Tk()
    win.title('Parking Made Easy')
    win.focus_force() #To bring the window in focus
    win.geometry('600x500')

        #To bring window in center of the screen of user
    win.geometry("{}x{}+{}+{}".format(600, 500, int((win.winfo_screenwidth()/2) - (600/2)), int((win.winfo_screenheight()/2) - (500/2))))

    win.configure(background="light green")
    #create labels

    exitlabel=tk.Label(win, text="Total Duration(in Hrs)" , bg="yellow")
    exitlabel.grid(row=0, column=0, padx=10, pady=10)

    

    feedbacklabel=tk.Label(win, text=" Feedback ", bg="yellow")
    feedbacklabel.grid(row=1, column=0, padx=10, pady=10)

    #create Option


    
    exit_var = tk.IntVar()
    exit_eb = tk.Entry(win, width=25, textvariable= exit_var)
    exit_eb.grid(row=0, column=1, padx=10, pady=10)

    

    #create radiobutton
    feedback_var=tk.StringVar()
    feedback1 = ttk.Radiobutton(win,width=15,text='Highly Satisfied',   value='1',    variable= feedback_var)
    feedback2 = ttk.Radiobutton(win,width=15,text='Satisfied' ,value='2',  variable= feedback_var)
    feedback3 = ttk.Radiobutton(win,width=15, text='Average',value='3', variable= feedback_var)
    feedback4 = ttk.Radiobutton(win,width=15, text='Unsatisfied',value='4', variable= feedback_var)
    feedback5 = ttk.Radiobutton(win,width=15, text='Highly Unsatisfied',value='5', variable= feedback_var)
    feedback1.grid(row=2, column=1,  padx=5, pady=5)
    feedback2.grid(row=3, column=1,  padx=5, pady=5)
    feedback3.grid(row=4, column=1,  padx=5, pady=5)
    feedback4.grid(row=5, column=1,  padx=5, pady=5)
    feedback5.grid(row=6, column=1,  padx=5, pady=5)
    
    def action1():
        global net_amount
        if(emergencyfuel_var == 'YES'):
            net_amount = 800
        else:
            net_amount = 0

            
        if (cartype_var == 'SUV'):
            net_amount += 100
        elif(cartype_var == 'SEDAN'):
            net_amount += 80
        elif(cartype_var == 'HATCHBACK'):
            net_amount += 60
        else:
            net_amount += 50


        net_amount += int(exit_var.get())*10
        if(carwash_var == 'YES'):
            net_amount += 60
        if(residency_var == 'YES'):
            net_amount +=50

        result_string = "Total Bill  is: Rs." + str(net_amount)
        messagebox.showinfo("Bill!", result_string)
        win.destroy()

    ok_button1=tk.Button(win, text="OK", command=action1, bg="red" )
    ok_button1.grid(row=4,column=2, padx=10, pady=10)
    
    win.mainloop()
      
if __name__ == "__main__":                  #To run this program indiviually
        gui3() 

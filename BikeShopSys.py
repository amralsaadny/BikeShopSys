import tkinter as tk
from tkinter import ttk, Menu
import mysql.connector

TITLE_FONT = ("Verdana", 22)
FONT = ("Verdana", 14)


class BikeShopApp(tk.Tk):
    
    user = None

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Bike Shop System")

        container = tk.Frame(self)
        container.pack()

        self.frames = {}

        for F in (LoginPage, PosPage, AdminPage, CustomerPage):
            frame = F(container, self)
            self.frames[F] = frame

            frame.grid(row=0, column = 0, padx = 60, pady=100, sticky="nsew")


        self.show_curr_frame(LoginPage)

    #initializes navigation bar
    def init_nav(self, controller):        
        menubar = Menu(self)
        self.config(menu=menubar)
        
        fileMenu = Menu(menubar)
        

        menubar.add_cascade(label="System", menu=fileMenu)
        

        fileMenu.add_command(label="Logout", command=exit)
        

        if controller.user>1:
            adminMenu = Menu(menubar)
            menubar.add_cascade(label="Admin", menu=adminMenu)
            adminMenu.add_command(label="Employee Tools", command=exit)

    #connect to database
    def init_db(self):
        pass

    '''
    method to pull the current frame to the front
    '''
    def show_curr_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    
'''
Employee login page
accepts a user id 
cross checks with the database
starts POS page if user is valid
'''
class LoginPage(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        pageTitle = ttk.Label(self, text = "Login", font = TITLE_FONT)
        pageTitle.grid(row = 0, column= 1,columnspan = 2,  padx = 10, pady = 10,sticky="EW")
        label1 = ttk.Label(self, text="Employee Id:", font = FONT)
        label1.grid(row = 1, column = 0, padx = 10, pady = 10)

        entry = ttk.Entry(self)
        entry.grid(row = 1, column= 1, padx = 10, pady = 10)

        logButton = ttk.Button(self, text= "Login", command=lambda: self.login(controller, userid= entry.get()))
        logButton.grid(row=1, column=2,  padx = 10, pady = 10)



    def login(self, controller, userid):
        #set the current user id
        #TEMP
        controller.user = int(userid)
        controller.init_nav(controller)
        controller.show_curr_frame(PosPage)


class PosPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        pageTitle = ttk.Label(self, text = "POS System", font = TITLE_FONT)
        pageTitle.grid(row = 0, column= 0,columnspan = 2,  padx = 10, pady = 10,sticky="EW")


class AdminPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        pageTitle = ttk.Label(self, text = "POS System", font = TITLE_FONT)
        pageTitle.grid(row = 0, column= 0,columnspan = 2,  padx = 10, pady = 10,sticky="EW")

class CustomerPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        pageTitle = ttk.Label(self, text = "POS System", font = TITLE_FONT)
        pageTitle.grid(row = 0, column= 0,columnspan = 2,  padx = 10, pady = 10,sticky="EW")
        

app = BikeShopApp()
w, h = app.winfo_screenwidth(), app.winfo_screenheight()
app.geometry("%dx%d+0+0" % (w/2, h/2))
app.mainloop()
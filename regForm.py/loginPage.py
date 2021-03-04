from tkinter import *



class LoginPage(Tk):

    def __init__(self):
        super().__init__()
        self.title('Login')
        self.RETURNVALUE = 0
        img = PhotoImage(file="image/logo.png")      
        canvas = Canvas(self, width = 310, height = 296)      
        label = Label(self, text="St. Thomas' College of Enginnering & Technology\nSTCET - 2021")
        canvas1 = Canvas(self, width = 310, height = 296)
        URN = Label(self, text = "University Roll Number:")
        PW = Label(self, text = "Password (use DOB) :")
        login_button = Button(self, text="Login",command=self.login, relief='solid', bd=3)
        FNR_button = Button(self, text="For New Registeration",command= self.FNR_quit, relief='solid', bd=1)
        
        
        canvas.create_image(10,10, anchor=NW, image=img)
        label.config(font=("Courier", 30), fg='darkblue')
        canvas1.create_image(10,10, anchor=NW, image=img)
        URN.config(font=("Courier", 15))
        PW.config(font=("Courier", 15))
        login_button.config(font=("Courier", 20))
        FNR_button.config(font=("Courier", 20), bg='skyblue', fg='red')

        URN_field = Entry(self)
        PW_field = Entry(self)


        canvas.grid(row=0, column=0)
        label.grid(row=0, column=1, columnspan=2)
        canvas1.grid(row=0, column=3)
        URN.grid(row= 1, column=1, sticky=NE, pady = 10)
        PW.grid(row= 2, column=1, sticky=NE, pady = 10)
        URN_field.grid(row=1, column=2, sticky=NW, pady = 10)
        PW_field.grid(row=2, column=2, sticky=NW, pady = 10)
        login_button.grid(row=3, column=1, columnspan=2, pady = 10)
        FNR_button.grid(row=4, column=1, columnspan=2, pady = 40)

        self.mainloop()

    def FNR_quit(self):
        self.destroy()
        self.RETURNVALUE = 'FNR'

    def login(self):
        self.destroy()
        self.RETURNVALUE = 'LOGIN'
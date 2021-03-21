from tkinter import *
from tkinter import messagebox



class LoginPage(Tk):

    def __init__(self, width, height, condition):
        super().__init__()
        self.title('Login Page')
        self.RETURNVALUE = 0
        self.geometry(f'{width}x{height}')
        self.minsize(1800,600)
        self.id = 0
        self.password = 0
        self.frame = Frame(self, bd=2, highlightthickness=0, bg="white")
        self.create(width, height)
        if condition:
            messagebox.showerror('Error', "User does not exist.")
        self.mainloop()


    def create(self, width, height):
        
        self.img = PhotoImage(file="image/logo.png")      
        self.home_img = PhotoImage(file="image/home.png")

        home_canvas = Canvas(self, width=width, height=height)
        canvas = Canvas(self.frame, width = 310, height = 296, bg="white", highlightthickness=0)      
        Label(self.frame, text="St. Thomas' College of Enginnering & Technology\nSTCET - 2021", bg="white", font=("Courier", 30), fg='darkblue').grid(row=0, column=1, columnspan=2)
        canvas1 = Canvas(self.frame, width = 310, height = 296, bg="white", highlightthickness=0)
        Label(self.frame, text = "College Roll Number:", bg="white", font=("Courier", 15)).grid(row= 1, column=1, sticky=NE, pady = 10)
        Label(self.frame, text = "Password:", bg="white", font=("Courier", 15)).grid(row= 2, column=1, sticky=NE, pady = 10)
        Button(self.frame, text="Login",command=self.login, relief='solid', bd=3, font=("Courier", 20), bg='#CEC8AE').grid(row=3, column=1, columnspan=2, pady = 10)
        Button(self.frame, text="For New Registeration",command= self.FNR_quit, relief='solid', bd=1, font=("Courier", 20), bg='#A24744', fg='white').grid(row=4, column=1, columnspan=2, pady = 40)
        
        home_canvas.create_image(width/2, height/2, image=self.home_img, anchor="c")
        canvas.create_image(10,10, anchor=NW, image=self.img)
        canvas1.create_image(10,10, anchor=NW, image=self.img)

        self.URN_field = Entry(self.frame)
        self.PW_field = Entry(self.frame)

        canvas.grid(row=0, column=0)
        canvas1.grid(row=0, column=3)

        
        self.URN_field.grid(row=1, column=2, sticky=NW, pady = 10)
        self.PW_field.grid(row=2, column=2, sticky=NW, pady = 10)

        home_canvas.place(relx=0.5, rely=0.5, anchor="c")
        self.frame.place(relx=0.5, rely=0.5, anchor="c")
        self.frame.focus_force()
        self.frame.lift()
        self.update()

    def FNR_quit(self):
        self.destroy()
        self.RETURNVALUE = 'FNR'

    def login(self):
        self.id = self.URN_field.get()
        self.password = self.PW_field.get()
        try:
            int(self.id)
        except:
            messagebox.showerror('Error', "Invalid Roll Number.")
        else:
            if self.id == '' or self.password == '':
                messagebox.showerror('Error', "Field can't be empty.")
            else:
                self.destroy()
                self.RETURNVALUE = 'LOGIN'
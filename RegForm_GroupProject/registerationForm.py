from tkinter import *
from tkinter import messagebox
from datetime import datetime
from checkBox import CheckBox

class RegisterationForm(Tk, CheckBox):

    def __init__(self, new_roll, width, height):
        super().__init__()

        ## Title
        self.title('Welcome to registeration Form')
        self.geometry(f'{width}x{height}')
        self.minsize(1800,600)
        # self.resizable(width=False, height=False)

        ## Intializing Variable
        self.College_Roll_Number = new_roll
        self.Candidates_Name = 0
        self.Father_Name = 0
        self.Mothers_Name = 0
        self.Date_of_Birth = 0
        self.Gender = 0
        self.Identification_Type = 0
        self.Identification_Number = 0
        self.Premises_Name = 0
        self.Locality = 0
        self.State = 0
        self.District = 0
        self.Pincode = 0
        self.Email = 0
        self.Mobile = 0
        self.Year_of_Passing_12 = 0
        self.Board_12 = 0
        self.Course_12 = '10+2'
        self.Total_Marks_12 = 0
        self.Obtained_Marks_12 = 0
        self.Marks_percentage_12 = 0
        self.Year_of_Passing_10 = 0
        self.Board_10 = 0
        self.Course_10 = 10
        self.Total_Marks_10 = 0
        self.Obtained_Marks_10 = 0
        self.Marks_percentage_10 = 0
        self.temp_10= StringVar()
        self.temp_12= StringVar()
        self.is_successfully_submitted = False

        home_img = PhotoImage(file="image/home.png")
        home_canvas = Canvas(self, width=width, height=height)
        home_canvas.create_image(width/2, height/2, image=home_img, anchor="c")
        home_canvas.place(relx=0.5, rely=0.5, anchor="c")

        self.Header()

        self.Frame1()

        self.mainloop()


    ## Header #########
    def Header(self):

        self.header = Frame(self, bg='white')
        self.header.place(relx=0.5, rely=0.5, anchor="c")

        ## Create Widget for Header
        self.img = PhotoImage(file="image/logo.png")
        canvas = Canvas(self.header, width = 300, height = 296, bg='white', highlightthickness=0)      
        Label(self.header, text="St. Thomas' College of Enginnering & Technology\nSTCET - 2021", bg='white', font=("Courier", 30)).grid(row=0, column=1, columnspan=2)
        canvas1 = Canvas(self.header, width = 300, height = 296, bg='white', highlightthickness=0)
        
        canvas.create_image(0,0, anchor=NW, image=self.img)
        canvas1.create_image(0,0, anchor=NW, image=self.img)

        ## Using Grid Method
        canvas.grid(row=0, column=0)
        canvas1.grid(row=0, column=3, pady=40)


    ## Personal Details Frame #########
    def Frame1(self):

        ## Creating Frame
        self.frame = Frame(self.header, relief='solid', bg='white')
        self.frame.grid(row=1, column=0, columnspan=4, padx = 40, pady = 10, ipadx=25, sticky=E)


        ## Creating widgets for Taking Personal Data Inputs
        Label(self.frame, text="Personal Details", font=("Courier", 20), fg='red', bg='white').grid(row=0, column=0, padx=20, pady=10, sticky=S)

        w = Canvas(self.frame, width=1540, height=3)
        w.create_rectangle(0, 0, 1800, 3, fill="blue", outline = 'blue')

        Label(self.frame, text="Candidate's Name", font=("Courier", 20), bg='white').grid(row=2, column=1) 
        Label(self.frame, text="Father's Name", font=("Courier", 20), bg='white').grid(row=3, column=1) 
        Label(self.frame, text="Mother's Name", font=("Courier", 20), bg='white').grid(row=4, column=1) 
        Label(self.frame, text="Date of Birth (DD/MM/YYYY)", font=("Courier", 20), bg='white').grid(row=5, column=1) 
        Label(self.frame, text="Gender", font=("Courier", 20), bg='white').grid(row=6, column=1)
        Label(self.frame, text="Identification Type", font=("Courier", 20), bg='white').grid(row=7, column=1) 
        Label(self.frame, text="Identification Number", font=("Courier", 20), bg='white').grid(row=8, column=1)

        self.candidate_name_field = Entry(self.frame)
        self.father_name_field = Entry(self.frame)
        self.mother_name_field = Entry(self.frame)
        self.dob_field = Entry(self.frame)
        self.var1 = StringVar(self.frame)
        self.var1.set("Select Gender")
        self.gender_field = OptionMenu(self.frame,self.var1,"Male","Female","Others")
        self.gender_field.config(width=15)
        self.var2 = StringVar(self.frame)
        self.var2.set("Select Identification Type")
        self.identification_type_field = OptionMenu(self.frame,self.var2,"Aadhar Card","Passport","Driver's License")
        self.identification_type_field.config(width=15)
        self.identification_num_field = Entry(self.frame)

        Button(self.frame, text="Next", fg="Black", padx=25, bg="skyblue", command=self.Frame1to2).grid(row=9, column=0, columnspan=4, pady=25)
       

        # Using Grid Method
        w.grid(row=1, column=0, columnspan=4, sticky=N, pady=10)
        self.candidate_name_field.grid(row=2, column=2, ipadx="100")
        self.father_name_field.grid(row=3, column=2, ipadx="100")
        self.mother_name_field.grid(row=4, column=2, ipadx="100")
        self.dob_field.grid(row=5, column=2, ipadx="100")
        self.gender_field.grid(row=6, column=2, ipadx="100")
        self.identification_type_field.grid(row=7, column=2, ipadx="100")
        self.identification_num_field.grid(row=8, column=2, ipadx="100")

        
    

    ## Address Details Frame #########
    def Frame1to2(self):

        ## Taking input from Frame1
        self.Candidates_Name = self.candidate_name_field.get()
        self.Father_Name = self.father_name_field.get()
        self.Mothers_Name = self.mother_name_field.get()
        self.Date_of_Birth = self.dob_field.get()
        self.Gender = self.var1.get()
        self.Identification_Type = self.var2.get()
        self.Identification_Number = self.identification_num_field.get()

        if self.Candidates_Name == '' or self.Father_Name == '' or self.Mothers_Name == '' or self.Date_of_Birth == '' or self.Gender == 'Select Gender' or self.Identification_Type == 'Select Identification Type' or self.Identification_Number == '':
            messagebox.showerror('Error', "Field can't be empty.")
        elif self.checkDOB(self.Date_of_Birth):
            messagebox.showerror('Error', "Invalid Date of Birth.")
        else:
            ## Destroy Frame1
            self.frame.destroy()
            ## Calling Frame2
            self.Frame2()

    def Frame2(self):

        ## Creating Frame
        self.frame = Frame(self.header, relief='solid', bg='white')
        self.frame.grid(row=1, column=0, columnspan=4, padx = 40, pady = 10, ipadx=25, sticky=E)

        ## Creating widgets for Taking Address Data Inputs
        Label(self.frame, text="Present Address", font=("Courier", 20), fg='red', bg='white').grid(row=0, column=0, padx=20, pady=10, sticky=S)

        w = Canvas(self.frame, width=1540, height=3)
        w.create_rectangle(0, 0, 1800, 3, fill="blue", outline = 'blue')


        Label(self.frame, text="Premises Name", font=("Courier", 20), bg='white').grid(row=2, column=1)
        Label(self.frame, text="Locality", font=("Courier", 20), bg='white').grid(row=3, column=1)
        Label(self.frame, text="State", font=("Courier", 20), bg='white').grid(row=4, column=1)
        Label(self.frame, text="District", font=("Courier", 20), bg='white').grid(row=5, column=1)
        Label(self.frame, text="Pincode", font=("Courier", 20), bg='white').grid(row=6, column=1)
        Label(self.frame, text="Email Id", font=("Courier", 20), bg='white').grid(row=7, column=1)
        Label(self.frame, text="Contact Number", font=("Courier", 20), bg='white').grid(row=8, column=1)
  
        self.premises_name_field = Entry(self.frame) 
        self.locality_field = Entry(self.frame) 
        self.state_field = Entry(self.frame) 
        self.city_field = Entry(self.frame) 
        self.pincode_field = Entry(self.frame)
        self.email_field = Entry(self.frame) 
        self.phone_field = Entry(self.frame) 
        
        Button(self.frame, text="Next", fg="Black", padx=25, bg="skyblue", command=self.Frame2to3).grid(row=9, column=0, columnspan=4, pady=25) 
       

        # Using Grid Method
        w.grid(row=1, column=0, columnspan=4, sticky=N, pady=10)
        self.premises_name_field.grid(row=2, column=2, ipadx="100") 
        self.locality_field.grid(row=3, column=2, ipadx="100") 
        self.state_field.grid(row=4, column=2, ipadx="100") 
        self.city_field.grid(row=5, column=2, ipadx="100") 
        self.pincode_field.grid(row=6, column=2, ipadx="100") 
        self.email_field.grid(row=7, column=2, ipadx="100") 
        self.phone_field.grid(row=8, column=2, ipadx="100") 
    
        
    
    def Frame2to3(self):

        ## Taking input from Frame2
        self.Premises_Name = self.premises_name_field.get()
        self.Locality = self.locality_field.get()
        self.State = self.state_field.get()
        self.District = self.city_field.get()
        self.Pincode = self.pincode_field.get()
        self.Email = self.email_field.get()
        self.Mobile = self.phone_field.get()

        if self.Premises_Name == '' or self.State == '' or self.District == '' or self.Pincode == '' or self.Email == '' or self.Mobile == '':
            messagebox.showerror('Error', "Field can't be empty.")
        elif self.checkNumber(self.Pincode):
            messagebox.showerror('Error', "Invalid Pincode.")
        elif self.checkEmail(self.Email):
            messagebox.showerror('Error', "Invalid Email ID.")
        elif self.checkMob(self.Mobile):
            messagebox.showerror('Error', "Invalid Mobile Number.")
        else:
            ## Destroy Frame2
            self.frame.destroy()
            ## Calling Frame3
            self.Frame3()




    ## Education Details Frame #########
    def Frame3(self):
        
        ## Creating Frame
        self.frame = Frame(self.header, relief='solid', bg='white')
        self.frame.grid(row=1, column=0, columnspan=4, padx = 40, pady = 10, ipadx=25, sticky=E)

        ## Creating widgets for Taking Education Data Inputs
        Label(self.frame, text="Education Details", font=("Courier", 20), fg='red', bg='white').grid(row=0, column=0, padx=20, pady=10, sticky=S)

        w = Canvas(self.frame, width=1540, height=3)
        w.create_rectangle(0, 0, 1800, 3, fill="blue", outline = 'blue')

        Label(self.frame, text="Year of Passing", font=("Courier", 15), bg='white').grid(row=2, column=0) 
        Label(self.frame, text="Board", font=("Courier", 15), bg='white').grid(row=2, column=1) 
        Label(self.frame, text="Course", font=("Courier", 15), bg='white').grid(row=2, column=2)
        Label(self.frame, text="Total Marks", font=("Courier", 15), bg='white').grid(row=4, column=0) 
        Label(self.frame, text="Obtained Marks", font=("Courier", 15), bg='white').grid(row=4, column=1) 
        Label(self.frame, text="Marks(%)", font=("Courier", 15), bg='white').grid(row=4, column=2)

        Label(self.frame, text="Year of Passing", font=("Courier", 15), bg='white').grid(row=9, column=0) 
        Label(self.frame, text="Board", font=("Courier", 15), bg='white').grid(row=9, column=1) 
        Label(self.frame, text="Course", font=("Courier", 15), bg='white').grid(row=9, column=2) 
        Label(self.frame, text="Total Marks", font=("Courier", 15), bg='white').grid(row=11, column=0) 
        Label(self.frame, text="Obtained Marks", font=("Courier", 15), bg='white').grid(row=11, column=1)
        Label(self.frame, text="Marks(%)", font=("Courier", 15), bg='white').grid(row=11, column=2)

        self.yearofpassing_10_field = Entry(self.frame) 
        self.board_10_field = Entry(self.frame)
        self.course_10_field = Entry(self.frame, textvariable=self.temp_10, state="readonly")
        self.temp_10.set(10)
        self.total_10_field = Entry(self.frame) 
        self.obtainedmarks_10_field = Entry(self.frame) 
        self.markspercentage_10_field = Entry(self.frame)

        self. yearofpassing_12_field = Entry(self.frame) 
        self.board_12_field = Entry(self.frame)
        self.course_12_field = Entry(self.frame, textvariable=self.temp_12, state="readonly")
        self.temp_12.set("10+2")
        self.total_12_field = Entry(self.frame) 
        self.obtainedmarks_12_field = Entry(self.frame) 
        self.markspercentage_12_field = Entry(self.frame)


        
        Button(self.frame, text="Submit", fg="Black", padx=25, bg="skyblue", command=self.Frame3to4).grid(row=13, column=0, columnspan=4, pady=25)
       
        w1 = Canvas(self.frame, width=1540, height=3)
        w1.create_rectangle(0, 0, 1800, 3, fill="blue", outline = 'blue')
        
        
        ## Using Grid Method
        w.grid(row=1, column=0, columnspan=4, sticky=N, pady=10)
        w1.grid(row=6, column=0, columnspan=4, sticky=N, pady=10)
        
        self. yearofpassing_10_field.grid(row=3, column=0, ipadx="30") 
        self.board_10_field.grid(row=3, column=1, ipadx="30") 
        self.course_10_field.grid(row=3, column=2, ipadx="30") 
        self.total_10_field.grid(row=5, column=0, ipadx="30") 
        self.obtainedmarks_10_field.grid(row=5, column=1, ipadx="30") 
        self.markspercentage_10_field.grid(row=5, column=2, ipadx="30") 

        self.yearofpassing_12_field.grid(row=10, column=0, ipadx="30") 
        self.board_12_field.grid(row=10, column=1, ipadx="30") 
        self.course_12_field.grid(row=10, column=2, ipadx="30") 
        self.total_12_field.grid(row=12, column=0, ipadx="30") 
        self.obtainedmarks_12_field.grid(row=12, column=1, ipadx="30") 
        self.markspercentage_12_field.grid(row=12, column=2, ipadx="30") 
 


    def Frame3to4(self):

        ## Taking input from Frame3
        self.Year_of_Passing_12 = self.yearofpassing_12_field.get()
        self.Board_12 = self.board_12_field.get()
        self.Course_12 = self.course_12_field.get()
        self.Total_Marks_12 = self.total_12_field.get()
        self.Obtained_Marks_12 = self.obtainedmarks_12_field.get()
        self.Marks_percentage_12 = self.markspercentage_12_field.get()
        self.Year_of_Passing_10 = self. yearofpassing_10_field.get()
        self.Board_10 = self.board_10_field.get()
        self.Course_10 = self.course_10_field.get()
        self.Total_Marks_10 = self.total_10_field.get()
        self.Obtained_Marks_10 = self.obtainedmarks_10_field.get()
        self.Marks_percentage_10 = self.markspercentage_10_field.get()

        if self.Year_of_Passing_10 == '' or self.Board_10 == '' or self.Total_Marks_10 == '' or self.Obtained_Marks_10 == '' or self.Marks_percentage_10 == '' or self.Year_of_Passing_12 == '' or self.Board_12 == '' or self.Total_Marks_12 == '' or self.Obtained_Marks_12 == '' or self.Marks_percentage_12 == '':
            messagebox.showerror('Error', "Field can't be empty.")
        elif self.checkNumber(self.Year_of_Passing_10) or self.checkNumber(self.Year_of_Passing_12):
            messagebox.showerror('Error', "Invalid Year.")
        elif self.checkNumber(self.Total_Marks_10) or self.checkNumber(self.Total_Marks_12):
            messagebox.showerror('Error', "Invalid Total Marks.")
        elif self.checkNumber(self.Obtained_Marks_10) or self.checkNumber(self.Obtained_Marks_12):
            messagebox.showerror('Error', "Invalid Obtained Marks.")
        elif self.checkNumber(self.Marks_percentage_10) or self.checkNumber(self.Marks_percentage_12):
            messagebox.showerror('Error', "Invalid Marks Percentage.")
        else:
            ## Destroy Frame3
            self.frame.destroy()
            ## Calling Frame4
            self.Frame4()


    ## Display Login Id Frame #########
    def Frame4(self):

        self.is_successfully_submitted = True

        ##password maker
        password = f"{self.Candidates_Name[:3]}{self.Date_of_Birth[-4:]}"

        ##login credentials
        Label(self.header, text = f"Your College Roll Number: {self.College_Roll_Number}", font=("Courier", 20), bg='white').grid(row= 1, column=1, columnspan=2, sticky=N, pady = 10)
        Label(self.header, text = f"Your Password: {password}", font=("Courier", 20), bg='white').grid(row= 2, column=1, columnspan=2, sticky=N, pady = 10)
        Button(self.header, text="Close", fg="Black", padx=25, bg="skyblue", command=self.destroy).grid(row=3, column=1, columnspan=2, pady=25)

from tkinter import *

class RegisterationForm(Tk):

    def __init__(self, new_roll):
        super().__init__()

        ## Title
        self.title('Welcome to registeration Form')
        
        self.resizable(width=False, height=False)

        ## Intializing Variable
        self.University_Roll_Number = new_roll
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

        self.Header()

        self.Frame1()

        self.mainloop()


    ## Header #########
    def Header(self):
        ## Create Widget for Header
        self.img = PhotoImage(file="image/logo.png")
        canvas = Canvas(self, width = 300, height = 296)      
        label = Label(self, text="St. Thomas' College of Enginnering & Technology\nSTCET - 2021")
        canvas1 = Canvas(self, width = 300, height = 296)
        
        canvas.create_image(0,0, anchor=NW, image=self.img)
        label.config(font=("Courier", 30))
        canvas1.create_image(0,0, anchor=NW, image=self.img)

        ## Using Grid Method
        canvas.grid(row=0, column=0)
        label.grid(row=0, column=1, columnspan=2)
        canvas1.grid(row=0, column=3, pady=40)


    ## Personal Details Frame #########
    def Frame1(self):

        ## Creating Frame
        self.frame = Frame(self, relief='solid')
        self.frame.grid(row=1, column=0, columnspan=4, padx = 40, pady = 10, ipadx=25, sticky=E)


        ## Creating widgets for Taking Personal Data Inputs
        personal_details = Label(self.frame, text="Personal Details", font=("Courier", 20), fg='red')

        w = Canvas(self.frame, width=1540, height=3)
        w.create_rectangle(0, 0, 1800, 3, fill="blue", outline = 'blue')

        candidate_name = Label(self.frame, text="Candidate's Name", font=("Courier", 20))
        father_name = Label(self.frame, text="Father's Name", font=("Courier", 20)) 
        mother_name = Label(self.frame, text="Mother's Name", font=("Courier", 20)) 
        dob = Label(self.frame, text="Date of Birth (DD/MM/YYYY)", font=("Courier", 20))
        gender = Label(self.frame, text="Gender", font=("Courier", 20))
        identification_type = Label(self.frame, text="Identification Type", font=("Courier", 20))
        identification_num = Label(self.frame, text="Identification Number", font=("Courier", 20)) 

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

        submit = Button(self.frame, text="Next", fg="Black", padx=25, bg="skyblue", command=self.Frame1to2) 
       

        # Using Grid Method
        personal_details.grid(row=0, column=0, padx=20, pady=10, sticky=S)
        w.grid(row=1, column=0, columnspan=4, sticky=N, pady=10)

        candidate_name.grid(row=2, column=1) 
        father_name.grid(row=3, column=1) 
        mother_name.grid(row=4, column=1) 
        dob.grid(row=5, column=1) 
        gender.grid(row=6, column=1) 
        identification_type.grid(row=7, column=1) 
        identification_num.grid(row=8, column=1)

        self.candidate_name_field.grid(row=2, column=2, ipadx="100")
        self.father_name_field.grid(row=3, column=2, ipadx="100")
        self.mother_name_field.grid(row=4, column=2, ipadx="100")
        self.dob_field.grid(row=5, column=2, ipadx="100")
        self.gender_field.grid(row=6, column=2, ipadx="100")
        self.identification_type_field.grid(row=7, column=2, ipadx="100")
        self.identification_num_field.grid(row=8, column=2, ipadx="100")

        submit.grid(row=9, column=0, columnspan=4, pady=25)
    

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

        ## Destroy Frame1
        self.frame.destroy()

        ## Calling Frame2
        self.Frame2()

    def Frame2(self):

        ## Creating Frame
        self.frame = Frame(self, relief='solid')
        self.frame.grid(row=1, column=0, columnspan=4, padx = 40, pady = 10, ipadx=25, sticky=E)

        ## Creating widgets for Taking Address Data Inputs
        address_details = Label(self.frame, text="Present Address", font=("Courier", 20), fg='red')

        w = Canvas(self.frame, width=1540, height=3)
        w.create_rectangle(0, 0, 1800, 3, fill="blue", outline = 'blue')

        premises_name = Label(self.frame, text="Premises Name", font=("Courier", 20))
        locality = Label(self.frame, text="Locality", font=("Courier", 20)) 
        state = Label(self.frame, text="State", font=("Courier", 20)) 
        city = Label(self.frame, text="District", font=("Courier", 20))
        pincode = Label(self.frame, text="Pincode", font=("Courier", 20))
        email = Label(self.frame, text="Email Id", font=("Courier", 20))
        phone = Label(self.frame, text="Contact Number", font=("Courier", 20)) 
  
        self.premises_name_field = Entry(self.frame) 
        self.locality_field = Entry(self.frame) 
        self.state_field = Entry(self.frame) 
        self.city_field = Entry(self.frame) 
        self.pincode_field = Entry(self.frame)
        self.email_field = Entry(self.frame) 
        self.phone_field = Entry(self.frame) 
        
        submit = Button(self.frame, text="Next", fg="Black", padx=25, bg="skyblue", command=self.Frame2to3) 
       

        # Using Grid Method
        address_details.grid(row=0, column=0, padx=20, pady=10, sticky=S)
        w.grid(row=1, column=0, columnspan=4, sticky=N, pady=10)

        premises_name.grid(row=2, column=1) 
        locality.grid(row=3, column=1) 
        state.grid(row=4, column=1) 
        city.grid(row=5, column=1) 
        pincode.grid(row=6, column=1) 
        email.grid(row=7, column=1) 
        phone.grid(row=8, column=1) 

        self.premises_name_field.grid(row=2, column=2, ipadx="100") 
        self.locality_field.grid(row=3, column=2, ipadx="100") 
        self.state_field.grid(row=4, column=2, ipadx="100") 
        self.city_field.grid(row=5, column=2, ipadx="100") 
        self.pincode_field.grid(row=6, column=2, ipadx="100") 
        self.email_field.grid(row=7, column=2, ipadx="100") 
        self.phone_field.grid(row=8, column=2, ipadx="100") 
    
        submit.grid(row=9, column=0, columnspan=4, pady=25) 
        
    
    def Frame2to3(self):

        ## Taking input from Frame2
        self.Premises_Name = self.premises_name_field.get()
        self.Locality = self.locality_field.get()
        self.State = self.state_field.get()
        self.District = self.city_field.get()
        self.Pincode = self.pincode_field.get()
        self.Email = self.email_field.get()
        self.Mobile = self.phone_field.get()

        ## Destroy Frame2
        self.frame.destroy()

        ## Calling Frame3
        self.Frame3()



    ## Education Details Frame #########
    def Frame3(self):
        
        ## Creating Frame
        self.frame = Frame(self, relief='solid')
        self.frame.grid(row=1, column=0, columnspan=4, padx = 40, pady = 10, ipadx=25, sticky=E)

        ## Creating widgets for Taking Education Data Inputs
        education_details = Label(self.frame, text="Education Details", font=("Courier", 20), fg='red')

        w = Canvas(self.frame, width=1540, height=3)
        w.create_rectangle(0, 0, 1800, 3, fill="blue", outline = 'blue')

        yearofpassing_10 = Label(self.frame, text="Year of Passing", font=("Courier", 15))
        board_10 = Label(self.frame, text="Board", font=("Courier", 15)) 
        course_10 = Label(self.frame, text="Course", font=("Courier", 15)) 
        total_10 = Label(self.frame, text="Total Marks", font=("Courier", 15)) 
        obtainedmarks_10 = Label(self.frame, text="Obtained Marks", font=("Courier", 15))
        markspercentage_10 = Label(self.frame, text="Marks(%)", font=("Courier", 15))
        
        yearofpassing_12 = Label(self.frame, text="Year of Passing", font=("Courier", 15))
        board_12 = Label(self.frame, text="Board", font=("Courier", 15)) 
        course_12 = Label(self.frame, text="Course", font=("Courier", 15)) 
        total_12 = Label(self.frame, text="Total Marks", font=("Courier", 15)) 
        obtainedmarks_12 = Label(self.frame, text="Obtained Marks", font=("Courier", 15))
        markspercentage_12 = Label(self.frame, text="Marks(%)", font=("Courier", 15))

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


        
        submit = Button(self.frame, text="Submit", fg="Black", padx=25, bg="skyblue", command=self.Frame3to4) 
       
        w1 = Canvas(self.frame, width=1540, height=3)
        w1.create_rectangle(0, 0, 1800, 3, fill="blue", outline = 'blue')
        
        
        ## Using Grid Method
        education_details.grid(row=0, column=0, padx=20, pady=10, sticky=S)
        w.grid(row=1, column=0, columnspan=4, sticky=N, pady=10)
        w1.grid(row=6, column=0, columnspan=4, sticky=N, pady=10)

        yearofpassing_10.grid(row=2, column=0) 
        board_10.grid(row=2, column=1) 
        course_10.grid(row=2, column=2) 
        total_10.grid(row=4, column=0) 
        obtainedmarks_10.grid(row=4, column=1) 
        markspercentage_10.grid(row=4, column=2)

        yearofpassing_12.grid(row=9, column=0) 
        board_12.grid(row=9, column=1) 
        course_12.grid(row=9, column=2) 
        total_12.grid(row=11, column=0) 
        obtainedmarks_12.grid(row=11, column=1) 
        markspercentage_12.grid(row=11, column=2)
        
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

        submit.grid(row=13, column=0, columnspan=4, pady=25) 


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

        ## Destroy Frame3
        self.frame.destroy()

        ## Calling Frame4
        self.Frame4()


    ## Display Login Id Frame #########
    def Frame4(self):

        self.is_successfully_submitted = True

        ##password maker
        password = f"{self.Candidates_Name[:3]}{self.Date_of_Birth[-4:]}"
        # print(self.Date_of_Birth[-4:])

        ##login credentials
        URN = Label(self, text = f"Your University Roll Number: {self.University_Roll_Number}")
        PW = Label(self, text = f"Your Password: {password}")
        submit = Button(self, text="Close", fg="Black", padx=25, bg="skyblue", command=self.destroy) 

        URN.config(font=("Courier", 20))
        PW.config(font=("Courier", 20))

        ## Using Grid Method
        URN.grid(row= 1, column=1, columnspan=2, sticky=N, pady = 10)
        PW.grid(row= 2, column=1, columnspan=2, sticky=N, pady = 10)
        submit.grid(row=3, column=1, columnspan=2, pady=25)

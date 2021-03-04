from tkinter import *

class RegisterationForm(Tk):

    def __init__(self):
        super().__init__()

        self.title('Welcome to registeration Form')
        self.University_Roll_Number = 0
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
        self.Course_12 = 0
        self.Total_Marks_12 = 0
        self.Obtained_Marks_12 = 0
        self.Marks_percentage_12 = 0
        self.Year_of_Passing_10 = 0
        self.Board_10 = 0
        self.Course_10 = 0
        self.Total_Marks_10 = 0
        self.Obtained_Marks_10 = 0
        self.Marks_percentage_10 = 0
        img = PhotoImage(file="image/logo.png")
        canvas = Canvas(self, width = 300, height = 296)      
        label = Label(self, text="St. Thomas' College of Enginnering & Technology\nSTCET - 2021")
        canvas1 = Canvas(self, width = 300, height = 296)
        
        canvas.create_image(0,0, anchor=NW, image=img)
        label.config(font=("Courier", 30))
        canvas1.create_image(0,0, anchor=NW, image=img)

        canvas.grid(row=0, column=0)
        label.grid(row=0, column=1, columnspan=2)
        canvas1.grid(row=0, column=3, pady=40)

        self.Frame()

        self.mainloop()



    def Frame(self):
        self.frame = Frame(self, relief='solid')
        self.frame.grid(row=1, column=0, columnspan=4, padx = 40, pady = 10, ipadx=25, sticky=E)

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
  
        submit = Button(self.frame, text="Next", fg="Black", padx=25, bg="skyblue", command=self.Frame2) 
       
        # grid method

        personal_details.grid(row=0, column=0, padx=20, pady=10, sticky=S)
        w.grid(row=1, column=0, columnspan=4, sticky=N, pady=10)

        candidate_name.grid(row=2, column=1) 
        father_name.grid(row=3, column=1) 
        mother_name.grid(row=4, column=1) 
        dob.grid(row=5, column=1) 
        gender.grid(row=6, column=1) 
        identification_type.grid(row=7, column=1) 
        identification_num.grid(row=8, column=1) 
    

        candidate_name_field = Entry(self.frame) 
        father_name_field = Entry(self.frame) 
        mother_name_field = Entry(self.frame) 
        dob_field = Entry(self.frame) 
        gender_field = Entry(self.frame) 
        identification_type_field = Entry(self.frame) 
        identification_num_field = Entry(self.frame) 


        candidate_name_field.grid(row=2, column=2, ipadx="100") 
        father_name_field.grid(row=3, column=2, ipadx="100") 
        mother_name_field.grid(row=4, column=2, ipadx="100") 
        dob_field.grid(row=5, column=2, ipadx="100") 
        gender_field.grid(row=6, column=2, ipadx="100") 
        identification_type_field.grid(row=7, column=2, ipadx="100") 
        identification_num_field.grid(row=8, column=2, ipadx="100") 

        submit.grid(row=9, column=0, columnspan=4, pady=25) 


    def Frame2(self):
        self.frame.destroy()
        self.frame = Frame(self, relief='solid')
        self.frame.grid(row=1, column=0, columnspan=4, padx = 40, pady = 10, ipadx=25, sticky=E)

        personal_details = Label(self.frame, text="Present Address", font=("Courier", 20), fg='red')

        w = Canvas(self.frame, width=1540, height=3)
        w.create_rectangle(0, 0, 1800, 3, fill="blue", outline = 'blue')

        premises_name = Label(self.frame, text="Premises Name", font=("Courier", 20))
        locality = Label(self.frame, text="Locality", font=("Courier", 20)) 
        state = Label(self.frame, text="State", font=("Courier", 20)) 
        city = Label(self.frame, text="District", font=("Courier", 20))
        pincode = Label(self.frame, text="Pincode", font=("Courier", 20))
        email = Label(self.frame, text="Email Id", font=("Courier", 20))
        phone = Label(self.frame, text="Contact Number", font=("Courier", 20)) 
  
        
        submit = Button(self.frame, text="Next", fg="Black", padx=25, bg="skyblue", command=self.Frame3) 
       
        # grid method

        personal_details.grid(row=0, column=0, padx=20, pady=10, sticky=S)
        w.grid(row=1, column=0, columnspan=4, sticky=N, pady=10)

        premises_name.grid(row=2, column=1) 
        locality.grid(row=3, column=1) 
        state.grid(row=4, column=1) 
        city.grid(row=5, column=1) 
        pincode.grid(row=6, column=1) 
        email.grid(row=7, column=1) 
        phone.grid(row=8, column=1) 
        

        premises_name_field = Entry(self.frame) 
        locality_field = Entry(self.frame) 
        state_field = Entry(self.frame) 
        city_field = Entry(self.frame) 
        pincode_field = Entry(self.frame)
        email_field = Entry(self.frame) 
        phone_field = Entry(self.frame) 


        premises_name_field.grid(row=2, column=2, ipadx="100") 
        locality_field.grid(row=3, column=2, ipadx="100") 
        state_field.grid(row=4, column=2, ipadx="100") 
        city_field.grid(row=5, column=2, ipadx="100") 
        pincode_field.grid(row=6, column=2, ipadx="100") 
        email_field.grid(row=7, column=2, ipadx="100") 
        phone_field.grid(row=8, column=2, ipadx="100") 
    

        submit.grid(row=9, column=0, columnspan=4, pady=25) 
        

    def Frame3(self):
        self.frame.destroy()
        self.frame = Frame(self, relief='solid')
        self.frame.grid(row=1, column=0, columnspan=4, padx = 40, pady = 10, ipadx=25, sticky=E)

        personal_details = Label(self.frame, text="Education Details", font=("Courier", 20), fg='red')

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
  
        
        submit = Button(self.frame, text="Submit", fg="Black", padx=25, bg="skyblue", command=self.Frame4) 
       
        w1 = Canvas(self.frame, width=1540, height=3)
        w1.create_rectangle(0, 0, 1800, 3, fill="blue", outline = 'blue')
        # grid method

        personal_details.grid(row=0, column=0, padx=20, pady=10, sticky=S)
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
        

        yearofpassing_10_field = Entry(self.frame) 
        board_10_field = Entry(self.frame)
        course_10_field = Entry(self.frame) 
        total_10_field = Entry(self.frame) 
        obtainedmarks_10_field = Entry(self.frame) 
        markspercentage_10_field = Entry(self.frame)

        yearofpassing_12_field = Entry(self.frame) 
        board_12_field = Entry(self.frame)
        course_12_field = Entry(self.frame) 
        total_12_field = Entry(self.frame) 
        obtainedmarks_12_field = Entry(self.frame) 
        markspercentage_12_field = Entry(self.frame)


        yearofpassing_10_field.grid(row=3, column=0, ipadx="30") 
        board_10_field.grid(row=3, column=1, ipadx="30") 
        course_10_field.grid(row=3, column=2, ipadx="30") 
        total_10_field.grid(row=5, column=0, ipadx="30") 
        obtainedmarks_10_field.grid(row=5, column=1, ipadx="30") 
        markspercentage_10_field.grid(row=5, column=2, ipadx="30") 

        yearofpassing_12_field.grid(row=10, column=0, ipadx="30") 
        board_12_field.grid(row=10, column=1, ipadx="30") 
        course_12_field.grid(row=10, column=2, ipadx="30") 
        total_12_field.grid(row=12, column=0, ipadx="30") 
        obtainedmarks_12_field.grid(row=12, column=1, ipadx="30") 
        markspercentage_12_field.grid(row=12, column=2, ipadx="30") 

    

        submit.grid(row=13, column=0, columnspan=4, pady=25) 

    def Frame4(self):
        self.frame.destroy()

        URN = Label(self, text = f"Your University Roll Number: 12200119064")
        PW = Label(self, text = f"Your Password: 08012001")
        submit = Button(self, text="Close", fg="Black", padx=25, bg="skyblue", command=self.destroy) 

        URN.config(font=("Courier", 20))
        PW.config(font=("Courier", 20))

        URN.grid(row= 1, column=1, columnspan=2, sticky=N, pady = 10)
        PW.grid(row= 2, column=1, columnspan=2, sticky=N, pady = 10)
        submit.grid(row=3, column=1, columnspan=2, pady=25) 

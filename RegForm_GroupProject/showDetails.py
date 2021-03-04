from tkinter import *


class ShowDetails(Tk):
        
        def __init__(self, data):
                super().__init__()

                self.title(f'Welcome {data[1]}')
                self.resizable(width=False, height=False)
                self.C_Name = StringVar()
                self.F_Name = StringVar()
                self.M_Name = StringVar()
                self.DOB = StringVar()
                self.Gen = StringVar()
                self.Iden_Type = StringVar()
                self.Iden_Num = StringVar()

                self.P_Name = StringVar()
                self.L_Name = StringVar()
                self.S_Name = StringVar()
                self.D_Name = StringVar()
                self.P_Num = StringVar()
                self.Mail = StringVar()
                self.Phone_Num = StringVar()

                self.YOP10 = StringVar()
                self.B10 = StringVar()
                self.C10 = StringVar()
                self.T10 = StringVar()
                self.O10 = StringVar()
                self.MP10 = StringVar()

                self.YOP12 = StringVar()
                self.B12 = StringVar()
                self.C12 = StringVar()
                self.T12 = StringVar()
                self.O12 = StringVar()
                self.MP12 = StringVar()

                self.Header()
                self.FilledForm(data)
                self.mainloop()

        def Header(self):

                self.label = Label(self, text="St. Thomas' College of Enginnering & Technology\nSTCET - 2021")
                self.label.config(font=("Courier", 30))
                self.label.grid(row=0, column=0, columnspan=4, pady=10)

                self.w = Canvas(self, width=1540, height=3)
                self.w.create_rectangle(0, 0, 1800, 3, fill="blue", outline = 'blue')
                self.w.grid(row=1, column=0, columnspan=4, sticky=N, pady=10)

        def FilledForm(self, data):

                self.personal_details = Frame(self, relief='solid', bd=2)
                self.personal_details.grid(row=2, column=0, columnspan=2, padx = 40, pady = 10, ipadx=25)
                personal_details = Label(self.personal_details, text="Personal Details", font=("Courier", 20), fg='red')
                Candidates_Name = Label(self.personal_details, text="Candidate's Name", font=("Courier", 15)) 
                Father_Name = Label(self.personal_details, text="Father's Name", font=("Courier", 15)) 
                Mother_Name = Label(self.personal_details, text="Mother's Name", font=("Courier", 15)) 
                Date_of_Birth = Label(self.personal_details, text="Date of Birth", font=("Courier", 15)) 
                Gender = Label(self.personal_details, text="Gender", font=("Courier", 15))
                Identification_Type = Label(self.personal_details, text="Identification Type", font=("Courier", 15)) 
                Identification_Num = Label(self.personal_details, text="Identification Number", font=("Courier", 15)) 

                personal_details.grid(row=0, column=0, padx=20, pady=10, sticky=S)
                Candidates_Name.grid(row=1, column=0, sticky=NW, pady=10, padx=10)
                Father_Name.grid(row=2, column=0, sticky=NW, pady=10, padx=10)
                Mother_Name.grid(row=3, column=0, sticky=NW, pady=10, padx=10)
                Date_of_Birth.grid(row=4, column=0, sticky=NW, pady=10, padx=10)
                Gender.grid(row=5, column=0, sticky=NW, pady=10, padx=10)
                Identification_Type.grid(row=6, column=0, sticky=NW, pady=10, padx=10)
                Identification_Num.grid(row=7, column=0, sticky=NW, pady=10, padx=10)

                self.Candidates_Name_field = Entry(self.personal_details, textvariable=self.C_Name, state="readonly")
                self.Father_Name_field = Entry(self.personal_details, textvariable=self.F_Name, state="readonly")
                self.Mother_Name_field = Entry(self.personal_details, textvariable=self.M_Name, state="readonly")
                self.Date_of_Birth_field = Entry(self.personal_details, textvariable=self.DOB, state="readonly")
                self.Gender_field = Entry(self.personal_details, textvariable=self.Gen, state="readonly")
                self.Identification_Type_field = Entry(self.personal_details, textvariable=self.Iden_Type, state="readonly")
                self.Identification_Num_field = Entry(self.personal_details, textvariable=self.Iden_Num, state="readonly")

                self.Candidates_Name_field.grid(row=1, column=1, sticky=NE, pady=10, ipadx=50, padx=10)
                self.Father_Name_field.grid(row=2, column=1, sticky=NE, pady=10, ipadx=50, padx=10)
                self.Mother_Name_field.grid(row=3, column=1, sticky=NE, pady=10, ipadx=50, padx=10)
                self.Date_of_Birth_field.grid(row=4, column=1, sticky=NE, pady=10, ipadx=50, padx=10)
                self.Gender_field.grid(row=5, column=1, sticky=NE, pady=10, ipadx=50, padx=10)
                self.Identification_Type_field.grid(row=6, column=1, sticky=NE, pady=10, ipadx=50, padx=10)
                self.Identification_Num_field.grid(row=7, column=1, sticky=NE, pady=10, ipadx=50, padx=10)
                
                self.C_Name.set(data[1])
                self.F_Name.set(data[2])
                self.M_Name.set(data[3])
                self.DOB.set(data[4])
                self.Gen.set(data[5])
                self.Iden_Type.set(data[6])
                self.Iden_Num.set(data[7])               

######################################################################################

                self.personal_details = Frame(self, relief='solid', bd=2)
                self.personal_details.grid(row=2, column=2, columnspan=2, padx = 40, pady = 10, ipadx=25)
                address_details = Label(self.personal_details, text="Present Address", font=("Courier", 20), fg='red')
                Premises_Name = Label(self.personal_details, text="Premises Name", font=("Courier", 15)) 
                Locality = Label(self.personal_details, text="Locality", font=("Courier", 15)) 
                State = Label(self.personal_details, text="State", font=("Courier", 15)) 
                District = Label(self.personal_details, text="District", font=("Courier", 15)) 
                Pincode = Label(self.personal_details, text="Pincode", font=("Courier", 15))
                Email = Label(self.personal_details, text="Email ID", font=("Courier", 15)) 
                Phone = Label(self.personal_details, text="Contact No.", font=("Courier", 15)) 

                address_details.grid(row=0, column=0, padx=20, pady=10, sticky=S)
                Premises_Name.grid(row=1, column=0, sticky=NW, pady=10, padx=10)
                Locality.grid(row=2, column=0, sticky=NW, pady=10, padx=10)
                State.grid(row=3, column=0, sticky=NW, pady=10, padx=10)
                District.grid(row=4, column=0, sticky=NW, pady=10, padx=10)
                Pincode.grid(row=5, column=0, sticky=NW, pady=10, padx=10)
                Email.grid(row=6, column=0, sticky=NW, pady=10, padx=10)
                Phone.grid(row=7, column=0, sticky=NW, pady=10, padx=10)

                self.Premises_Name_field = Entry(self.personal_details, textvariable=self.P_Name, state="readonly")
                self.Locality_field = Entry(self.personal_details, textvariable=self.L_Name, state="readonly")
                self.State_field = Entry(self.personal_details, textvariable=self.S_Name, state="readonly")
                self.District_field = Entry(self.personal_details, textvariable=self.D_Name, state="readonly")
                self.Pincode_field = Entry(self.personal_details, textvariable=self.P_Num, state="readonly")
                self.Email_field = Entry(self.personal_details, textvariable=self.Mail, state="readonly")
                self.Phone_field = Entry(self.personal_details, textvariable=self.Phone_Num, state="readonly")

                self.Premises_Name_field.grid(row=1, column=1, sticky=NE, pady=10, ipadx=50, padx=10)
                self.Locality_field.grid(row=2, column=1, sticky=NE, pady=10, ipadx=50, padx=10)
                self.State_field.grid(row=3, column=1, sticky=NE, pady=10, ipadx=50, padx=10)
                self.District_field.grid(row=4, column=1, sticky=NE, pady=10, ipadx=50, padx=10)
                self.Pincode_field.grid(row=5, column=1, sticky=NE, pady=10, ipadx=50, padx=10)
                self.Email_field.grid(row=6, column=1, sticky=NE, pady=10, ipadx=50, padx=10)
                self.Phone_field.grid(row=7, column=1, sticky=NE, pady=10, ipadx=50, padx=10)
                
                self.P_Name.set(data[8])
                self.L_Name.set(data[9])
                self.S_Name.set(data[10])
                self.D_Name.set(data[11])
                self.P_Num.set(data[12])
                self.Mail.set(data[13])
                self.Phone_Num.set(data[14])               

######################################################################################

                self.education_details_10 = Frame(self, relief='solid', bd=2)
                self.education_details_10.grid(row=3, column=0, columnspan=2, padx = 40, pady = 10, ipadx=25)

                education_details_10 = Label(self.education_details_10, text="Standard 10", font=("Courier", 20), fg='red')
                yearofpassing_10 = Label(self.education_details_10, text="Year of Passing", font=("Courier", 15))
                board_10 = Label(self.education_details_10, text="Board", font=("Courier", 15)) 
                course_10 = Label(self.education_details_10, text="Course", font=("Courier", 15)) 
                total_10 = Label(self.education_details_10, text="Total Marks", font=("Courier", 15)) 
                obtainedmarks_10 = Label(self.education_details_10, text="Obtained Marks", font=("Courier", 15))
                markspercentage_10 = Label(self.education_details_10, text="Marks(%)", font=("Courier", 15))
                
                self.yearofpassing_10_field = Entry(self.education_details_10, textvariable=self.YOP10, state="readonly") 
                self.board_10_field = Entry(self.education_details_10, textvariable=self.B10, state="readonly")
                self.course_10_field = Entry(self.education_details_10, textvariable=self.C10, state="readonly")
                self.total_10_field = Entry(self.education_details_10, textvariable=self.T10, state="readonly") 
                self.obtainedmarks_10_field = Entry(self.education_details_10, textvariable=self.O10, state="readonly") 
                self.markspercentage_10_field = Entry(self.education_details_10, textvariable=self.MP10, state="readonly")    

                education_details_10.grid(row=0, column=0, padx=20, pady=10, sticky=S)
                yearofpassing_10.grid(row=1, column=0, sticky=NW, pady=10, padx=10) 
                board_10.grid(row=2, column=0, sticky=NW, pady=10, padx=10) 
                course_10.grid(row=3, column=0, sticky=NW, pady=10, padx=10) 
                total_10.grid(row=4, column=0, sticky=NW, pady=10, padx=10) 
                obtainedmarks_10.grid(row=5, column=0, sticky=NW, pady=10, padx=10) 
                markspercentage_10.grid(row=6, column=0, sticky=NW, pady=10, padx=10)
                
                self. yearofpassing_10_field.grid(row=1, column=1, sticky=NE, pady=10, ipadx=50, padx=10) 
                self.board_10_field.grid(row=2, column=1, sticky=NE, pady=10, ipadx=50, padx=10) 
                self.course_10_field.grid(row=3, column=1, sticky=NE, pady=10, ipadx=50, padx=10) 
                self.total_10_field.grid(row=4, column=1, sticky=NE, pady=10, ipadx=50, padx=10) 
                self.obtainedmarks_10_field.grid(row=5, column=1, sticky=NE, pady=10, ipadx=50, padx=10) 
                self.markspercentage_10_field.grid(row=6, column=1, sticky=NE, pady=10, ipadx=50, padx=10) 

                self.YOP10.set(data[15])
                self.B10.set(data[16])
                self.C10.set(data[17])
                self.T10.set(data[18])
                self.O10.set(data[19])
                self.MP10.set(data[20])


######################################################################################

                self.education_details_12 = Frame(self, relief='solid', bd=2)
                self.education_details_12.grid(row=3, column=2, columnspan=2, padx = 40, pady = 10, ipadx=25)

                education_details_12 = Label(self.education_details_12, text="Standard 12", font=("Courier", 20), fg='red')
                yearofpassing_12 = Label(self.education_details_12, text="Year of Passing", font=("Courier", 15))
                board_12 = Label(self.education_details_12, text="Board", font=("Courier", 15)) 
                course_12 = Label(self.education_details_12, text="Course", font=("Courier", 15)) 
                total_12 = Label(self.education_details_12, text="Total Marks", font=("Courier", 15)) 
                obtainedmarks_12 = Label(self.education_details_12, text="Obtained Marks", font=("Courier", 15))
                markspercentage_12 = Label(self.education_details_12, text="Marks(%)", font=("Courier", 15))
                
                self.yearofpassing_12_field = Entry(self.education_details_12, textvariable=self.YOP12, state="readonly") 
                self.board_12_field = Entry(self.education_details_12, textvariable=self.B12, state="readonly")
                self.course_12_field = Entry(self.education_details_12, textvariable=self.C12, state="readonly")
                self.total_12_field = Entry(self.education_details_12, textvariable=self.T12, state="readonly") 
                self.obtainedmarks_12_field = Entry(self.education_details_12, textvariable=self.O12, state="readonly") 
                self.markspercentage_12_field = Entry(self.education_details_12, textvariable=self.MP12, state="readonly")    

                education_details_12.grid(row=0, column=0, padx=20, pady=10, sticky=S)
                yearofpassing_12.grid(row=1, column=0, sticky=NW, pady=10, padx=10) 
                board_12.grid(row=2, column=0, sticky=NW, pady=10, padx=10) 
                course_12.grid(row=3, column=0, sticky=NW, pady=10, padx=10) 
                total_12.grid(row=4, column=0, sticky=NW, pady=10, padx=10) 
                obtainedmarks_12.grid(row=5, column=0, sticky=NW, pady=10, padx=10) 
                markspercentage_12.grid(row=6, column=0, sticky=NW, pady=10, padx=10)
                
                self. yearofpassing_12_field.grid(row=1, column=1, sticky=NE, pady=10, ipadx=50, padx=10) 
                self.board_12_field.grid(row=2, column=1, sticky=NE, pady=10, ipadx=50, padx=10) 
                self.course_12_field.grid(row=3, column=1, sticky=NE, pady=10, ipadx=50, padx=10) 
                self.total_12_field.grid(row=4, column=1, sticky=NE, pady=10, ipadx=50, padx=10) 
                self.obtainedmarks_12_field.grid(row=5, column=1, sticky=NE, pady=10, ipadx=50, padx=10) 
                self.markspercentage_12_field.grid(row=6, column=1, sticky=NE, pady=10, ipadx=50, padx=10) 

                self.YOP12.set(data[21])
                self.B12.set(data[22])
                self.C12.set(data[23])
                self.T12.set(data[24])
                self.O12.set(data[25])
                self.MP12.set(data[26])

                
                Button(self, text="Close", fg="Black", padx=25, bg="skyblue", command=self.destroy).grid(row=6, column=0, columnspan=4, pady=25)
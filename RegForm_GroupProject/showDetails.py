from tkinter import *
from checkBox import CheckBox
from tkinter import messagebox

class ShowDetails(Tk, CheckBox):
        
        def __init__(self, data, width, height):
                super().__init__()

                self.title(f'Welcome {data[1]}')
                self.data = data
                self.geometry(f'{width}x{height}')
                self.minsize(1600,950)
                self.state = "readonly"
                self.theme_color = '#ffe8a8'
                self.ReturnValue = False

                self.home_img = PhotoImage(file="image/home.png")
                home_canvas = Canvas(self, width=width, height=height)
                home_canvas.create_image(width/2, height/2, image=self.home_img, anchor="c")
                home_canvas.place(relx=0.5, rely=0.5, anchor="c")

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

                self.create()
                self.FilledForm(data)
                self.mainloop()

        def create(self):

                self.Header = Frame(self, bg='white')
                

                self.label = Label(self.Header, text="St. Thomas' College of Enginnering & Technology\nSTCET - 2021", bg='white')
                self.label.config(font=("Courier", 30))
                self.label.grid(row=0, column=0, columnspan=4, pady=10)

                self.w = Canvas(self.Header, width=1540, height=3)
                self.w.create_rectangle(0, 0, 1800, 3, fill="blue", outline = 'blue')
                self.w.grid(row=1, column=0, columnspan=4, sticky=N, pady=10)
                self.Header.place(relx=0.5, rely=0.5, anchor="c")

        def FilledForm(self, data):

                self.personal_details = Frame(self.Header, relief='solid', bd=2, bg=self.theme_color)
                self.personal_details.grid(row=2, column=0, columnspan=2, padx = 40, pady = 10, ipadx=25)
                
                Label(self.personal_details, text="Personal Details", font=("Courier", 20), fg='blue', bg=self.theme_color).grid(row=0, column=0, padx=20, pady=10, sticky=S)
                Label(self.personal_details, text="Candidate's Name", font=("Courier", 15), bg=self.theme_color).grid(row=1, column=0, sticky=NW, pady=10, padx=10)
                Label(self.personal_details, text="Father's Name", font=("Courier", 15), bg=self.theme_color).grid(row=2, column=0, sticky=NW, pady=10, padx=10)
                Label(self.personal_details, text="Mother's Name", font=("Courier", 15), bg=self.theme_color).grid(row=3, column=0, sticky=NW, pady=10, padx=10)
                Label(self.personal_details, text="Date of Birth", font=("Courier", 15), bg=self.theme_color).grid(row=4, column=0, sticky=NW, pady=10, padx=10)
                Label(self.personal_details, text="Gender", font=("Courier", 15), bg=self.theme_color).grid(row=5, column=0, sticky=NW, pady=10, padx=10)
                Label(self.personal_details, text="Identification Type", font=("Courier", 15), bg=self.theme_color).grid(row=6, column=0, sticky=NW, pady=10, padx=10)
                Label(self.personal_details, text="Identification Number", font=("Courier", 15), bg=self.theme_color).grid(row=7, column=0, sticky=NW, pady=10, padx=10)

                self.Candidates_Name_field = Entry(self.personal_details, textvariable=self.C_Name, state="readonly")
                self.Father_Name_field = Entry(self.personal_details, textvariable=self.F_Name, state=self.state)
                self.Mother_Name_field = Entry(self.personal_details, textvariable=self.M_Name, state=self.state)
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

                self.personal_details = Frame(self.Header, relief='solid', bd=2, bg=self.theme_color)
                self.personal_details.grid(row=2, column=2, columnspan=2, padx = 40, pady = 10, ipadx=25)
                
                Label(self.personal_details, text="Present Address", font=("Courier", 20), fg='blue', bg=self.theme_color).grid(row=0, column=0, padx=20, pady=10, sticky=S)
                Label(self.personal_details, text="Premises Name", font=("Courier", 15), bg=self.theme_color).grid(row=1, column=0, sticky=NW, pady=10, padx=10)
                Label(self.personal_details, text="Locality", font=("Courier", 15), bg=self.theme_color).grid(row=2, column=0, sticky=NW, pady=10, padx=10)
                Label(self.personal_details, text="State", font=("Courier", 15), bg=self.theme_color).grid(row=3, column=0, sticky=NW, pady=10, padx=10)
                Label(self.personal_details, text="District", font=("Courier", 15), bg=self.theme_color).grid(row=4, column=0, sticky=NW, pady=10, padx=10)
                Label(self.personal_details, text="Pincode", font=("Courier", 15), bg=self.theme_color).grid(row=5, column=0, sticky=NW, pady=10, padx=10)
                Label(self.personal_details, text="Email ID", font=("Courier", 15), bg=self.theme_color).grid(row=6, column=0, sticky=NW, pady=10, padx=10)
                Label(self.personal_details, text="Contact No.", font=("Courier", 15), bg=self.theme_color).grid(row=7, column=0, sticky=NW, pady=10, padx=10)

                self.Premises_Name_field = Entry(self.personal_details, textvariable=self.P_Name, state=self.state)
                self.Locality_field = Entry(self.personal_details, textvariable=self.L_Name, state=self.state)
                self.State_field = Entry(self.personal_details, textvariable=self.S_Name, state=self.state)
                self.District_field = Entry(self.personal_details, textvariable=self.D_Name, state=self.state)
                self.Pincode_field = Entry(self.personal_details, textvariable=self.P_Num, state=self.state)
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

                self.education_details_10 = Frame(self.Header, relief='solid', bd=2, bg=self.theme_color)
                self.education_details_10.grid(row=3, column=0, columnspan=2, padx = 40, pady = 10, ipadx=25)

                Label(self.education_details_10, text="Standard 10", font=("Courier", 20), fg='blue', bg=self.theme_color).grid(row=0, column=0, padx=20, pady=10, sticky=S)
                Label(self.education_details_10, text="Year of Passing", font=("Courier", 15), bg=self.theme_color).grid(row=1, column=0, sticky=NW, pady=10, padx=10) 
                Label(self.education_details_10, text="Board", font=("Courier", 15), bg=self.theme_color).grid(row=2, column=0, sticky=NW, pady=10, padx=10) 
                Label(self.education_details_10, text="Course", font=("Courier", 15), bg=self.theme_color).grid(row=3, column=0, sticky=NW, pady=10, padx=10) 
                Label(self.education_details_10, text="Total Marks", font=("Courier", 15), bg=self.theme_color).grid(row=4, column=0, sticky=NW, pady=10, padx=10) 
                Label(self.education_details_10, text="Obtained Marks", font=("Courier", 15), bg=self.theme_color).grid(row=5, column=0, sticky=NW, pady=10, padx=10) 
                Label(self.education_details_10, text="Marks(%)", font=("Courier", 15), bg=self.theme_color).grid(row=6, column=0, sticky=NW, pady=10, padx=10)
                
                self.yearofpassing_10_field = Entry(self.education_details_10, textvariable=self.YOP10, state=self.state) 
                self.board_10_field = Entry(self.education_details_10, textvariable=self.B10, state=self.state)
                self.course_10_field = Entry(self.education_details_10, textvariable=self.C10, state="readonly")
                self.total_10_field = Entry(self.education_details_10, textvariable=self.T10, state=self.state) 
                self.obtainedmarks_10_field = Entry(self.education_details_10, textvariable=self.O10, state=self.state) 
                self.markspercentage_10_field = Entry(self.education_details_10, textvariable=self.MP10, state=self.state)    
                
                self. yearofpassing_10_field.grid(row=1, column=1, sticky=NE, pady=10, ipadx=50, padx=10) 
                self.board_10_field.grid(row=2, column=1, sticky=NE, pady=10, ipadx=50, padx=10) 
                self.course_10_field.grid(row=3, column=1, sticky=NE, pady=10, ipadx=50, padx=10) 
                self.total_10_field.grid(row=4, column=1, sticky=NE, pady=10, ipadx=50, padx=10) 
                self.obtainedmarks_10_field.grid(row=5, column=1, sticky=NE, pady=10, ipadx=50, padx=10) 
                self.markspercentage_10_field.grid(row=6, column=1, sticky=NE, pady=10, ipadx=50, padx=10) 

                self.YOP10.set(data[21])
                self.B10.set(data[22])
                self.C10.set(data[23])
                self.T10.set(data[24])
                self.O10.set(data[25])
                self.MP10.set(data[26])


######################################################################################

                self.education_details_12 = Frame(self.Header, relief='solid', bd=2, bg=self.theme_color)
                self.education_details_12.grid(row=3, column=2, columnspan=2, padx = 40, pady = 10, ipadx=25)
                


                Label(self.education_details_12, text="Standard 12", font=("Courier", 20), fg='blue', bg=self.theme_color).grid(row=0, column=0, padx=20, pady=10, sticky=S)
                Label(self.education_details_12, text="Year of Passing", font=("Courier", 15), bg=self.theme_color).grid(row=1, column=0, sticky=NW, pady=10, padx=10) 
                Label(self.education_details_12, text="Board", font=("Courier", 15), bg=self.theme_color).grid(row=2, column=0, sticky=NW, pady=10, padx=10) 
                Label(self.education_details_12, text="Course", font=("Courier", 15), bg=self.theme_color).grid(row=3, column=0, sticky=NW, pady=10, padx=10) 
                Label(self.education_details_12, text="Total Marks", font=("Courier", 15), bg=self.theme_color).grid(row=4, column=0, sticky=NW, pady=10, padx=10) 
                Label(self.education_details_12, text="Obtained Marks", font=("Courier", 15), bg=self.theme_color).grid(row=5, column=0, sticky=NW, pady=10, padx=10) 
                Label(self.education_details_12, text="Marks(%)", font=("Courier", 15), bg=self.theme_color).grid(row=6, column=0, sticky=NW, pady=10, padx=10)
                
                self.yearofpassing_12_field = Entry(self.education_details_12, textvariable=self.YOP12, state=self.state) 
                self.board_12_field = Entry(self.education_details_12, textvariable=self.B12, state=self.state)
                self.course_12_field = Entry(self.education_details_12, textvariable=self.C12, state="readonly")
                self.total_12_field = Entry(self.education_details_12, textvariable=self.T12, state=self.state) 
                self.obtainedmarks_12_field = Entry(self.education_details_12, textvariable=self.O12, state=self.state) 
                self.markspercentage_12_field = Entry(self.education_details_12, textvariable=self.MP12, state=self.state)    


                
                self. yearofpassing_12_field.grid(row=1, column=1, sticky=NE, pady=10, ipadx=50, padx=10) 
                self.board_12_field.grid(row=2, column=1, sticky=NE, pady=10, ipadx=50, padx=10) 
                self.course_12_field.grid(row=3, column=1, sticky=NE, pady=10, ipadx=50, padx=10) 
                self.total_12_field.grid(row=4, column=1, sticky=NE, pady=10, ipadx=50, padx=10) 
                self.obtainedmarks_12_field.grid(row=5, column=1, sticky=NE, pady=10, ipadx=50, padx=10) 
                self.markspercentage_12_field.grid(row=6, column=1, sticky=NE, pady=10, ipadx=50, padx=10) 

                self.YOP12.set(data[15])
                self.B12.set(data[16])
                self.C12.set(data[17])
                self.T12.set(data[18])
                self.O12.set(data[19])
                self.MP12.set(data[20])

                if self.state == 'readonly':                
                        Button(self.Header, text="Edit", fg="Black", padx=25, bg="skyblue", command=self.edit).grid(row=6, column=0, columnspan=2, pady=25)
                else:
                        Button(self.Header, text="Sumbit", fg="Black", padx=25, bg="skyblue", command=self.update).grid(row=6, column=0, columnspan=2, pady=25)
                Button(self.Header, text="Close", fg="Black", padx=25, bg="skyblue", command=self.destroy).grid(row=6, column=2, columnspan=2, pady=25)


        def edit(self):
                self.state = "normal"
                self.Header.destroy()
                self.create()
                self.FilledForm(self.data)


        def update(self):
                self.C_Name = self.Candidates_Name_field.get()
                self.F_Name = self.Father_Name_field.get()
                self.M_Name = self.Mother_Name_field.get()
                self.DOB = self.Date_of_Birth_field.get()
                self.Gen = self.Gender_field.get()
                self.Iden_Type = self.Identification_Type_field.get()
                self.Iden_Num = self.Identification_Num_field.get()

                self.P_Name = self.Premises_Name_field.get()
                self.L_Name = self.Locality_field.get()
                self.S_Name = self.State_field.get()
                self.D_Name = self.District_field.get()
                self.P_Num = self.Pincode_field.get()
                self.Mail = self.Email_field.get()
                self.Phone_Num = self.Phone_field.get()

                self.YOP10 = self.yearofpassing_10_field.get()
                self.B10 = self.board_10_field.get()
                self.C10 = self.course_10_field.get()
                self.T10 = self.total_10_field.get()
                self.O10 = self.obtainedmarks_10_field.get()
                self.MP10 = self.markspercentage_10_field.get()

                self.YOP12 = self.yearofpassing_12_field.get()
                self.B12 = self.board_12_field.get()
                self.C12 = self.course_12_field.get()
                self.T12 = self.total_12_field.get()
                self.O12 = self.obtainedmarks_12_field.get()
                self.MP12 = self.markspercentage_12_field.get()

                if self.F_Name == '' or self.M_Name =='' or self.P_Name == '' or self.L_Name == '' or self.S_Name == '' or self. D_Name == '' or self.B10 == '' or self.B12 == '' or self.P_Num == '' or self.YOP10 == '' or self.YOP12 == '' or self.T10  == '' or self.T12 == '' or self.O10 == '' or self.O12 == '' or self.MP10 == '' or self.MP10 == '':
                        messagebox.showerror('Error', "Field Can't Be Empty.")
                elif self.checkNumber(self.P_Num):
                        messagebox.showerror('Error', "Invalid Pincode.")
                elif self.checkNumber(self.YOP10) or self.checkNumber(self.YOP12):
                        messagebox.showerror('Error', "Invalid Year.")
                elif self.checkNumber(self.T10) or  self.checkNumber(self.T12):
                        messagebox.showerror('Error', "Invalid Total Marks.")
                elif self.checkNumber(self.O10) or  self.checkNumber(self.O12):
                        messagebox.showerror('Error', "Invalid Obtained Marks.")
                elif self.checkNumber(self.MP10) or  self.checkNumber(self.MP10):
                        messagebox.showerror('Error', "Invalid Total Marks.")
                else:
                        self.destroy()
                        self.ReturnValue =  True

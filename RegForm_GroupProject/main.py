from loginPage import LoginPage
from registerationForm import RegisterationForm
from showDetails import ShowDetails
from screenResolution import screenSize
from tkinter import messagebox
from excelSheet import ExcelSheet

ScreenSize = screenSize()
excel_sheet = ExcelSheet()
screen_width = ScreenSize.width
screen_height = ScreenSize.height

data_sheety = excel_sheet.get_data()
roll_nos = len(data_sheety)
code_dict = {}
for i in range(0, len(data_sheety)):
    data = [data_sheety[i][key] for key in data_sheety[i]]
    temp = {i:data}
    code_dict.update(temp)

def start(condition = False):
    login_page = LoginPage(screen_width, screen_height, condition)
    if login_page.RETURNVALUE == 'FNR':
        try:
            registeration_form = RegisterationForm(roll_nos+1, screen_width, screen_height)
        except:
            registeration_form = RegisterationForm(1, screen_width, screen_height)
        if registeration_form.is_successfully_submitted:
            temp = [registeration_form.College_Roll_Number, registeration_form.Candidates_Name,  registeration_form.Father_Name,  registeration_form.Mothers_Name,  registeration_form.Date_of_Birth,  registeration_form.Gender,  registeration_form.Identification_Type,  registeration_form.Identification_Number,  registeration_form.Premises_Name,  registeration_form.Locality,  registeration_form.State,  registeration_form.District,  registeration_form.Pincode,  registeration_form.Email,  registeration_form.Mobile,  registeration_form.Year_of_Passing_12,  registeration_form.Board_12,  registeration_form.Course_12,  registeration_form.Total_Marks_12,  registeration_form.Obtained_Marks_12,  registeration_form.Marks_percentage_12,  registeration_form.Year_of_Passing_10,  registeration_form.Board_10,  registeration_form.Course_10,  registeration_form.Total_Marks_10, registeration_form.Obtained_Marks_10,  registeration_form.Marks_percentage_10]
            excel_sheet.add_data(temp)
    
    elif login_page.RETURNVALUE == 'LOGIN':
        condition = True
        for key in code_dict:
            if code_dict[key][0]==int(login_page.id) and code_dict[key][1][:3]+code_dict[key][4][-4:]==login_page.password:
                show_details = ShowDetails(code_dict[key], screen_width, screen_height)
                if show_details.ReturnValue:
                    temp = [int(login_page.id), show_details.C_Name,  show_details.F_Name,  show_details.M_Name,  show_details.DOB,  show_details.Gen,  show_details.Iden_Type,  show_details.Iden_Num,  show_details.P_Name,  show_details.L_Name,  show_details.S_Name,  show_details.D_Name,  show_details.P_Num,  show_details.Mail,  show_details.Phone_Num,  show_details.YOP12,  show_details.B12,  show_details.C12,  show_details.T12,  show_details.O12,  show_details.MP12,  show_details.YOP10,  show_details.B10,  show_details.C10,  show_details.T10, show_details.O10,  show_details.MP10]
                    excel_sheet.edit_data(temp)
                condition = False
                break
        if condition:
            start(condition)

start()


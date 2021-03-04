import pandas

data = pandas.read_csv('data/data.csv')
code_dict = {index:[row.University_Roll_Number, row.Candidates_Name,  row.Father_Name,  row.Mothers_Name,  row.Date_of_Birth,  row.Gender,  row.Identification_Type,  row.Identification_Number,  row.Premises_Name,  row.Locality,  row.State,  row.District,  row.Pincode,  row.Email,  row.Mobile,  row.Year_of_Passing_12,  row.Board_12,  row.Course_12,  row.Total_Marks_12,  row.Obtained_Marks_12,  row.Marks_percentage_12,  row.Year_of_Passing_10,  row.Board_10,  row.Course_10,  row.Total_Marks_10,  row.Obtained_Marks_10,  row.Marks_percentage_10] for (index, row) in data.iterrows()}


from loginPage import LoginPage
from registerationForm import RegisterationForm

login_page = LoginPage()
if login_page.RETURNVALUE == 'FNR':
    registeration_form = RegisterationForm()
    temp = [registeration_form.University_Roll_Number, registeration_form.Candidates_Name,  registeration_form.Father_Name,  registeration_form.Mothers_Name,  registeration_form.Date_of_Birth,  registeration_form.Gender,  registeration_form.Identification_Type,  registeration_form.Identification_Number,  registeration_form.Premises_Name,  registeration_form.Locality,  registeration_form.State,  registeration_form.District,  registeration_form.Pincode,  registeration_form.Email,  registeration_form.Mobile,  registeration_form.Year_of_Passing_12,  registeration_form.Board_12,  registeration_form.Course_12,  registeration_form.Total_Marks_12,  registeration_form.Obtained_Marks_12,  registeration_form.Marks_percentage_12,  registeration_form.Year_of_Passing_10,  registeration_form.Board_10,  registeration_form.Course_10,  registeration_form.Total_Marks_10,  registeration_form.Obtained_Marks_10,  registeration_form.Marks_percentage_10]
    code_dict[len(code_dict)] = temp
    
    pandas.DataFrame(code_dict).to_csv('data/data.csv')

elif login_page.RETURNVALUE == 'LOGIN':
    for key in code_dict:
        if code_dict[key][0]==12200119065:
            print('Yesssss')


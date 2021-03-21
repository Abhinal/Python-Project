from datetime import datetime

class CheckBox:

    def __init__(self):
        self.message = 'Hello! Welcome to Check BOX'


    def checkDOB(self, birthdate):
        try:
            DOB = birthdate.split('/')
            day = int(DOB[0])
            month = int(DOB[1])
            year = int(DOB[2])
            datetime(year=year,month=month, day=day)
            return False
        except:
            return True

    def checkMob(self, number):
        try:
            number = int(number)
            number /= 1000000000
            if number > 1 and number <10:
                return False
            else:
                return True
        except:
            return True

    def checkEmail(self, email):
        if '@' in email and '.com' in email:
            return False
        else:
            return True

    def checkNumber(self, number):
        try:
            int(number)
            return False
        except:
            return True



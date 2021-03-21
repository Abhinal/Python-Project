import requests

class ExcelSheet:
    
    def __init__(self):

        self.SHEETY_ENDPOINT = 'https://api.sheety.co/74cca3ba09f55ae517c7afc1ec82c0cd/stcetStudentData/data'
        self.AUTH = 'Bearer THISISSTCETDATA'
        self.TYPE = 'application/json'


        self.bearer_headers = {
            'Authorization' : self.AUTH,
            'Content-Type' : self.TYPE
        }

    def get_data(self):

        response = requests.get(self.SHEETY_ENDPOINT, headers=self.bearer_headers)
        return response.json()['data']


    def data_format(self, temp_data):

        data = {
            'datum': {
                'collegeRollNumber': temp_data[0], 
                'candidatesName': temp_data[1], 
                'fatherName': temp_data[2], 
                'mothersName': temp_data[3], 
                'dateOfBirth': temp_data[4], 
                'gender': temp_data[5], 
                'identificationType': temp_data[6], 
                'identificationNumber': temp_data[7], 
                'premisesName': temp_data[8],
                'locality': temp_data[9],
                'state': temp_data[10],
                'district': temp_data[11],
                'pincode': temp_data[12],
                'email': temp_data[13], 
                'mobile': temp_data[14],
                'yearOfPassing12': temp_data[15], 
                'board12': temp_data[16], 
                'course12': temp_data[17], 
                'totalMarks12': temp_data[18],
                'obtainedMarks12': temp_data[19], 
                'marksPercentage12': temp_data[20], 
                'yearOfPassing10': temp_data[21], 
                'board10': temp_data[22], 
                'course10': temp_data[23], 
                'totalMarks10': temp_data[24], 
                'obtainedMarks10': temp_data[25], 
                'marksPercentage10': temp_data[26]
            }
        }
        return data

    def add_data(self, temp_data):

        data = self.data_format(temp_data)
        requests.post(f'{self.SHEETY_ENDPOINT}', json=data, headers=self.bearer_headers)

    def edit_data(self, temp_data):

        data = self.data_format(temp_data)
        requests.put(f'{self.SHEETY_ENDPOINT}/{temp_data[0]+1}', json=data, headers=self.bearer_headers)
        
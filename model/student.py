import pandas as pd

class Student(object):
    def __init__(self, appid=None, name=None,admission_date=None):
        self.appid=appid
        self.name=name
        self.admission_date=admission_date

    def studentInfo(self):
        return("%s %s %s" %(self.appid,self.name,self.admission_date))

    @classmethod
    def getAll(self):
        database = pd.read_csv('/home/bibhuti/Documents/pet_projects/admissionpart2/data/student.csv')
        result = []
        for i in database.itertuples():
            student = Student(i.appid, i.name,i.admission_date)
            result.append(student)
        return result


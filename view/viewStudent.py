from model.student import Student
from flask import  render_template

def showAllView(list):
    for item in list:
        print (item.studentInfo())
    return render_template('index.html', list= list)
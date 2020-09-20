from model.student import Student
import view.viewStudent as view
from flask import Flask
app = Flask(__name__)

def showAll():
    student_in_db = Student.getAll()
    return view.showAllView(student_in_db)

@app.route('/')
def start():
    return showAll()

if __name__=='__main__':
    app.run()
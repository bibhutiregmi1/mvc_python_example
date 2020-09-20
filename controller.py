from model.student import Student
import view.viewStudent as view


def showAll():
    student_in_db = Student.getAll()
    return view.showAllView(student_in_db)

def start():
    return showAll()

if __name__=='__main__':
    start()
class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks

    def display(self):
        print(f"name:{self.name}")
        print(f"rollno:{self.rollno}")
        for subject,mark in self.marks.items():
            print(f"{subject}:{mark}")
    def update_marks(self,subject,mark):
        self.marks[subject]=mark
        print(self.marks[subject])

    # def average(self):
    #     total=sum(self.marks.values())
    #     print(total/len(self.marks))
    #     print(self.marks)

student1=Student("shashi",101,{"math":85,"science":90,"English":78})
student1.display()
student1.update_marks("math",99)
# student1.average()
class student:
    clg = 'xyz' # class variables

    def __init__(self,rollno,age):
        self.rollno = rollno # instance variables means object variables
        self.age = age

    def display(self):
        print("self.rollno",self.rollno)
        print("clg",student.clg) # accessing  varibale by class


st = student('gyf56',22)
st.display()

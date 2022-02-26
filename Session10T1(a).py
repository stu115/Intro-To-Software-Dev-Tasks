class Student():
    def _init_(self,lastName,surName,studentNumber,course):

         self.surname = surName
         self.firstname = firstName
         self.studentnumber = studentNumber
         self.course = course


       def getSurname(self):
           return self.surname

       def getFirstname(self):
           return self.firstname

       def getStudentID(self):
           return self.studentnumber
           
       def getCourse(self):
           return self.course
        

       def setSurname(self,newSurname):
           self.surname = newSurname


       def setFirstname(self,newFirstname):
           self.firstname = newFirstname

       def setStudentID(self,newStudentID):
           self.studentnumber = newStudentnumber

       def setCourse(self,newCourse):
           self.course = newCourse

       def printAll(self):
           print("The surname is:" + self.surname)
           print("The firstname is:" + self.firstname)
           print("The studentID is: " + self.studentnumber)
           print("The course id:" + self.course)
           

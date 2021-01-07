from Supporting_Programs.databaseSS import *

class Staff:
    '''
    a class to represent Students.
    ...
    Attributes
    ----------
    name : str
        To store the name of Students.
    department : str
        To store the Department(Branch) of the student.
    roll : str
        To store the Roll No. of the Student.
    year : str
        To store the year of the Student.
    cgpa : str
        To store the CGPA of the Student.
    hostel: bool
        To store whether the Student lives in Hostel or not.
        True = Yes
        False = No

    Methods
    -------
    add_student()
        To Add a Student name and roll no. in the Database.
    hostel()
	To choose if Student lives in Hostel.
    remove_student()
        To remove a Student from the Database.
    modify()
        To modify the details of a Student.
    display_cgpa()
        To display CGPA of a given Student.
    enter_courses()
        To enter courses taken by a Student.
    enter_grade()
        To enter the Grades of a Student.
    print_grade()
        To print Grades of a Student.
    display_details()
        To display the details of a Student.
    '''

    name = ""
    dept = ""
    collegeId = ""
    email = ""
    lastCollege = ""
    gender = ""
    address = ""
    
    def add_staff(self, inputList):
        '''
        Function to add name and Roll no. of New Student.
        '''

        self.name = inputList[0]
        self.dept = inputList[2]
        self.collegeId = inputList[1]
        self.email = inputList[3]
        self.lastCollege = inputList[4]
        self.gender = inputList[5]
        self.address = inputList[6]
        
        details = self.compress_to_dictionary()
        write_to_file(details, "Databases\\staff")

    def listCheck(self,a,b):
        '''
        function to check what is in a and b and return whichever is not empty
        '''

        if b == "":
            return a
        else:
            return b

    def modify_staff(self, inputList):
        '''
        Function to modify staff details.
        '''
        prevInput = search("Databases\\staff","roll number", inputList[1])
        self.name = self.listCheck(prevInput[0], inputList[0])
        self.dept = self.listCheck(prevInput[1], inputList[2])
        self.collegeId = inputList[1]
        self.email = self.listCheck(prevInput[2], inputList[3])
        self.lastCollege = self.listCheck(prevInput[3], inputList[4])
        self.gender = self.listCheck(prevInput[4], inputList[5])
        self.address = self.listCheck(prevInput[5], inputList[6])
        details = self.compress_to_dictionary()
        modify_details("Databases\\staff",inputList[1], details)

    def compress_to_dictionary(self):
        details = {
            'name' : [self.name],
            'dept' : [self.dept],
            'collegeId' : [self.collegeId],
            'email' : [self.email],
            'last college' : [self.lastCollege],
            'gender' : [self.gender],
            'address' : [self.address]
        }
        return details


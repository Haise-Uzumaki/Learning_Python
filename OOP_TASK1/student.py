class Student:
    def __init__(self, name = "", id = "", cgpa = 0.0):
        self.name = name
        self.id = id
        self.__cgpa = cgpa
        
        
    def set_name(self, name):
        self.name = name
        
    def set_id(self, id):
        self.id = id
        
    def set_cgpa(self, cgpa):
        if 0.0 <= cgpa <= 4.0:
            self.__cgpa = cgpa
        else:
            print("Invalid CGPA!!!!")
            self.__cgpa = 0.0
            
    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.id
    
    def get_cgpa(self):
        return self.__cgpa
    
    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Student id  : {self.id}")
        print(f"Student CGPA: {self.__cgpa}")
        
    def checkScholarship(self):
        if self.__cgpa >= 3.5:
            print("You are eligible for scholarship")
        else:
            print("You are not eligible for scholarship")
            
    
    
    
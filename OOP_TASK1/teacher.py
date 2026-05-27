class Teacher:
    def __init__(self, name = "", id = "", salary = 0.0):
        self.name = name
        self.id = id
        self.__salary = salary
        
    def set_name(self, name):
        self.name = name
        
    def set_id(self, id):
        self.id = id 
    
    def set_salary(self, salary):
        self.__salary = salary
        
    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.id
    
    def get_salary(self):
        return self.__salary
    
    
    
    def display(self):
        print(f"Teacher Name  : {self.name}")
        print(f"Teacher Id    : {self.id}")
        print(f"Teacher Salary: {self.__salary}")
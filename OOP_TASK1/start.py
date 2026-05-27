from student import Student
from teacher import Teacher


class Start:
    @staticmethod
    def main():
        students = []
        teachers = []

        print("=== Enter Details for 5 Students ===")
        for i in range(5):
            print(f"\nStudent {i+1}:")
            name = input("Enter Name: ").strip()
            id = input("Enter ID: ").strip()
            cgpa = float(input("Enter CGPA: ") or 0)

            student = Student(name, id, cgpa)
            students.append(student)
            
            

        print("\n=== Enter Details for 5 Teachers ===")
        for i in range(5):
            print(f"\nTeacher {i+1}:")
            name = input("Enter Name: ").strip()
            id = input("Enter ID: ").strip()
            salary = float(input("Enter Monthly Salary: ") or 0)
            
            teacher = Teacher(name, id, salary)
            
        
        print("/n" + "="*20)
        print("Student Details")
        print("="*20)
        for s in students:
            s.display()
            s.checkScholarship()
            print("="*20)
            
        print("/n" + "="*20)
        print("Teacher Details")
        print("="*20)
        for s in teachers:
            s.display()
            print("="*20)
            
            if __name__ == "__main__":
                Start.main()
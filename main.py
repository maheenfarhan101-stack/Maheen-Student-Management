
students = []

def add_student():

    name = input('Enter student name: ').title()
    try:
        age = int (input('Enter age: '))
        marks = float (input('Enter marks: '))

    except ValueError:
        print('Please enter valid number!')
        return
    
    student = {
        "name" : name,
        "age" : age,
        "marks" : marks
    }

    students.append(student)
    print("Student added successfully!")

def view_students():

    if not students:
        print('No Student Found!')

    else:
        for student in students:
            print("----------------") 
            print('Name:', student['name'])
            print('Age:', student['age'])
            print('Marks:', student['marks'])

def search_student():

    search_name = input('Enter student name for search: ').title()

    for student in students:
        if search_name == student['name']:
            print('Student Found!')
            print(student)
            return

    print('Student not found!')

def delete_student():
    delete_name = input('Enter name for deletion: ').title()

    for student in students:
        if delete_name == student['name']:
            students.remove(student) 
            print('Student deleted successfully!')

            return

    print("Student not found!")    

while True:
    
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")  

    choice = input('Enter your choice: ')

    if choice == '1':
        add_student()

    elif choice == '2':
        view_students()

    elif choice == '3':
        search_student()

    elif choice == '4':
        delete_student()

    elif choice == '5':
        print("Thank you!")
        break

    else:
        print('Invalid choice!')            

from abc import ABC


class Person(ABC):      # Abstract class, can't initialize Person objects
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class Teacher(Person):      # Inherited class Person
    def __init__(self, name, email, phone, subject, salary):
        super().__init__(name, email, phone)    # Delegates initialization of name, email and phone to parent class
        self.subject = subject
        self.salary = salary


class Student(Person):
    def __init__(self, name, email, phone, classes, grades):
        super().__init__(name, email, phone)
        self.classes = classes
        self.grades = grades


def main():
    teacher = Teacher("Alf", "alf@skola.se", "0012345", "Programming", "1000000")
    student1 = Student("Karl", "karl@student.skola.se", "0098765", ["Programming", "Math", "Biology"], ["A", "C", "F"])
    student2 = Student("Mia", "mai@student.skola.se", "0065432", ["Programming", "Math", "Music"], ["A", "C", "A"])
    print(teacher.name, teacher.email, teacher.phone, teacher.subject, teacher.salary)
    print(student1.name)
    print(student2.name)


if __name__ == "__main__":
    main()

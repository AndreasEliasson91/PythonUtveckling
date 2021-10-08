class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):     # Str method made for programmers, fail messages for programmers etc.
        return f"Person({self.name}, {self.age})"

    def __str__(self):      # Str method for the user
        return F"{self.name} is {self.age} years old."


def compare(person):
    return person.name


def main():
    p1 = Person("Aa", 9)
    p2 = Person("Bb", 8)
    p3 = Person("Cc", 7)
    p4 = Person("Dd", 6)
    p5 = Person("Ee", 5)
    p6 = Person("Ff", 4)
    p7 = Person("Gg", 3)
    p8 = Person("Hh", 2)
    p9 = Person("Ii", 1)

    persons = [p2, p4, p1, p7, p3, p5, p9, p8, p6]
    sorted_persons = sorted(persons, key=compare)

    print(sorted_persons)               # __repr__

    for person in sorted_persons:       # __str__
        print(person)


if __name__ == "__main__":
    main()

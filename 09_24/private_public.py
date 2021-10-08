class Person:
    def __init__(self, name, age):
        self.__name = name          # __ renames attribute to _Person__name, "private"
        self._age = age             # _ before variable name indicates protected

    # def get_name(self):
    #     return self.__name

    @property                       # Getter
    def name(self):
        return self.__name

    @name.setter                    # Setter
    def name(self, name: str):
        self.__name = name


def main():
    person = Person("Bo", 69)
    print(person.name)
    # print(person.get_name())        # Bo
    # person.__name = "Jonas"
    # print(person.__name)            # Jonas
    # print(person.get_name())        # Bo
    # print(dir(person))


if __name__ == "__main__":
    main()

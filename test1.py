# import  test2
#
# obj1 = test2.employee()
# obj2 = test2.person()
from utils.utils1 import person2

obj1 = person2('Mur','bin',1990)
print(obj1.yob)


class Person:
    def __init__(self, name, surname, yob):
        self._name = name
        self.__surname = surname
        self.yob = yob

sudh = Person('sudh','kumar',1990)

print(sudh._name)
print(sudh._Person__surname)
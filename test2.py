import test1
print(test1)

obj3 = test1.Person('vinnu','moni',2000)
print(obj3.yob)
print(obj3._name)
print(obj3._Person__surname)

class person:

    _name = "sudh"
    __surname = "kumar"
    yob = 1990

    def _age(self, current_year):
        return current_year - self.yob

    def __age1(self, current_year):
        return current_year - self.yob

obj = person()
print(obj)
print(obj._age(2022))
print(obj._person__age1(2022))

class employee(person):
    _name = 'murali'
    __surname = 'gummadidala'
    yob = 1993

obj1 = employee()
print(obj1._age(2022))
print(obj1._person__age1(2022))
print(obj1)
print(obj1.yob)
print(obj1._name)
print(obj1._person__surname)



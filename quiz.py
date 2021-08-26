class Student:
    def __init__(self,name,age):
        self.name = name
        self.__age = age

    def get_name(self):
        return self.name
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        self.__age = age


class ClassStudent(Student):
    def __init__(self, name, age, avg):
        super().__init__(name, age)
        self.__avg = avg

    def get_name(self):
        return self.name + "woo"

    @property
    def avg(self):
        return self.__avg
    @avg.getter
    def avg(self):
        return self.__avg
    @avg.setter
    def avg(self, avg):
        self.__avg = avg + 20
    def __int__(self):
        return self.__avg

def all_sum(some_list:list):
    if isinstance(some_list[0], int):
        return sum(some_list)
    else:
        for idx, x in enumerate(some_list):
            some_list[idx] = int(x)
        return sum(some_list)

test_a = ClassStudent("chan", 28, 95)
list_a = [test_a, ClassStudent("bob", 28, 90), ClassStudent("mo", 28, 80)]

print("1. test_a.get_name():", test_a.get_name())
print("2. test_a.age:", test_a.age)
print("3. test_a.avg():", test_a.avg)
print("4. all_sum(list_a):", all_sum(list_a))
test_a.age = 38
print("5. test_a.age:", test_a.age)
test_a.avg = 10
print("6. test_a.avg:", test_a.avg)
test_a.__avg = 20
print("7. test_a.avg:", test_a.avg)

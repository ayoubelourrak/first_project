class Person:
    def __init__(self, name, number):
        self._name = name
        self._number = number

    def print_hi(self):
        if self._number > 0:
            squares = [i**2 for i in range(0, self._number)]
            for elem in squares:
                print(elem)
        elif self._number == 0:
            print(f'What!!!! Just a Zero?!')
        else:
            print(f'my name is {self._name}')


class Student(Person):
    def print_hi(self):
        print(f'fuck off')

if __name__ == '__main__':
    p = Person("Luca", 5)
    p.print_hi()
    print(p._name)

    s = Student("Luca", -2)
    s.print_hi()
    print(s._name)
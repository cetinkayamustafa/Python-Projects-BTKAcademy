#inheritance (kalıtım ) : miras alma


# Person => name, lastname, age , eat(), run(),drink()

#student(Person),Teacher(Person)


class Person():
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname = lname
        print('person created')
    def who_am_i(self):
        print('I am a person ')

class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)

        print('student created')

class Teacher(Person):
    def __init__(self, fname, lname,branch):
        super().__init__(fname, lname)
        self.branch = branch

    def who_am_i(self):
        print('I am a Teacher')

p1 = Person('Mustafa', 'Çetinkaya')
s1 = Student('Musa' , 'Çetinkaya')
t1 = Teacher('Serkan ', ' Yılmaz', 'Math')

t1.who_am_i()
print(p1.fname + ' ' + p1.lname)
print(s1.fname + ' ' + s1.lname)
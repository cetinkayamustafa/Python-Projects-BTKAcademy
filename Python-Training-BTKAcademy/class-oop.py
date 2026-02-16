#class

class Person:
     #class attributes
    adress = 'no information'


     #object attributes 
     #methods
    #(pass #yer tutucu)
# # #constructor (yapıcı metod)

    def __init__(self, name, year):
        self.name = name
        self.birthYear = year
        print('init metodu çalıştı')

#object (instance)
# p1 =Person('ali', 1990)
# p2 =Person('Mustafa', 2000)
p1 =Person(name= 'ali', year= 1990)
p2 =Person(name= 'mustafa', year= 2000)
#updating 

p1.adress = 'Zonguldak'
#accessing obhect attributes
print(f'name : {p1.name} year : {p1.birthYear} address : {p1.adress}' )
# print(p1)
# print(p2)
# print(type(p1))
# print(type(p2))
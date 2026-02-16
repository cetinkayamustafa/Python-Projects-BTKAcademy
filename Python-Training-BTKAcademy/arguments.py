def changeName(n):
    n = ' ada'
name = 'mustafa'

changeName(name)
print(name)

def change(n):
    n[0] = 'Zonguldak'

sehirler =  ['Ankara, İstanbul']
change(sehirler)
print(sehirler)


def displayUser(**args):
    print(type(args))
    for key, value in args.items():
        print('{} is {}'.format(key,value))
displayUser(name = 'Mustafa', age = 26, city = 'zonguldak')
displayUser(name = 'Musa', age = 20, city = 'zonguldak')
displayUser(name = 'Sinan', age = 25, city = 'Adana')


def myFunc(a,b,*args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
myFunc(10,20,30,40,50, key1 = 'value 1 ', key2='value 2')
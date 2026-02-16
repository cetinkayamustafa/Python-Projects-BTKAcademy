# def sayHello():
#     print('Hello')

# sayHello()



# def sayHello(name):
#     print('Hello '+ name)

# sayHello('Çınar')


# def sayHello(name):
#     return 'Hello ' + name

# msg = sayHello('Çınar')
# print(msg)


# def total(num1, num2):
#     return num1 + num2

# result = total(10,20)
# print(result)


def yasHesapla(dogumYili):
    return 2026- dogumYili

ageMustafa = yasHesapla(2000)
ageMusa= yasHesapla(2006)

print(ageMusa,ageMustafa)


def emekliligeKacYilKaldi(dogumYili, isim):

    '''
    Docstring for emekliligeKacYilKaldi
    
    dogumYili: The day that you birth
    isim: Your name
    '''
    yas =yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik > 0 :
        print(f'{isim} bey, emekliliğinize {emeklilik} yıl kaldı')
    else:
        print('zaten emeklisin dayı')

emekliligeKacYilKaldi(2000, 'Mustafa')
print(help(emekliligeKacYilKaldi))

import random

sayi = random.randrange(1,100)
hak = int(input('kaç hak istiyorsunuz : '))


while hak > 0:
    hak -= 1
    girilenSayi = int(input('Tahmininiz : '))
    if sayi == girilenSayi:
        print('tebrikler bildiniz.')
        break
    elif sayi > girilenSayi:
        print('yukari')
    else :
        print('asaği')
    if hak == 0:
        print(f'hakkınız bitti tutulan sayi {sayi}' )

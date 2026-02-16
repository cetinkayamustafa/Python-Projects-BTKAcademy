mustafaHesap = {
    'ad' : 'Mustafa Çetinkaya',
    'hesap no ' : '123456789',
    'bakiye' : 3000,
    'ekHesap ' : 2000
}

musaHesap = {
    'ad' : 'Musa Çetinkaya',
    'hesap no ' : '01020301',
    'bakiye' :2000,
    'ekHesap ' : 1000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")
    if hesap['bakiye'] >= miktar:
        print('paranızı alabilirsiniz')
    else:
        toplam =hesap['bakiye'] + hesap['ekHesap ']
        if (toplam >= miktar):
            ekHesapKullanimi = input('Ek hesap kullanılsın mı (e/h)' )

            if ekHesapKullanimi == 'e':
                print('^paranızı alabilirsiniz')
            else:
                print(f"{hesap['hesap no']} nolu hesabınızda {hesap['bakiye']} var")
        else:
            print('paranız yetersiz')

paraCek(mustafaHesap,6000)
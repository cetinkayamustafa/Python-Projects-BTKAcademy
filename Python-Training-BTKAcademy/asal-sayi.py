girilenSayi = int(input('sayı giriniz: ' ))
asalMi= True
if girilenSayi == 1:
    asalMi = False
for i in range(2,girilenSayi):
    if girilenSayi % i == 0:
        asalMi = False
        break
if asalMi:
    print('sayı asaldır')
else:
    print('asal değildir.')
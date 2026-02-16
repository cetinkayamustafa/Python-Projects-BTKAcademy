
#q1

# name = str(input('Adınız : '))
# age= int(input('yaşınız : '))
# educationLevel = str(input('Eğitim bilgisi (ilkokul/ortaokul/lise/üni) : '))

# if age >= 18 :
#     if (educationLevel == 'lise' or educationLevel == 'üni'):
#         print(f'{name} ehliyet alabilirsin')
#     else: 
#         print(f'{name} ehliyet alamazsın eğitim durumunuz yetersiz')
# else:
#     print(f'{name} ehliyet alamazsınız yaşınız tutmuyor')

#-------------------------------------------------------------------------

#q2 : 


# yazili1 = float(input('1.yazılı : '))
# yazili2 = float(input('2.yazılı : '))
# sözlü = float(input('Sözlü : '))
# ortalama = (yazili1 + yazili2 + sözlü )/3
# if (ortalama >=0 ) and (ortalama < 25):
#     print(f'ortalamanız {ortalama} notunuz : 0')
# elif (ortalama >=25) and (ortalama < 45):
#     print(f'ortalamanız {ortalama} notunuz : 1')
# elif (ortalama >=45) and (ortalama < 55):
#     print(f'ortalamanız {ortalama} notunuz : 2')
# elif (ortalama >=55) and (ortalama < 70):
#     print(f'ortalamanız {ortalama} notunuz : 3')
# elif (ortalama >=70) and (ortalama < 85):
#     print(f'ortalamanız {ortalama} notunuz : 4')
# elif (ortalama >=85) and (ortalama <= 100):
#     print(f'ortalamanız {ortalama} notunuz : 5')
# else:
#     print('yanlıs bilgi')


#-------------------------------------------------------

#q3 :

# days = int(input('aracınız kac gundur trafikte : '))
# if days <= 365:
#     print('1.servis aralığı')
# elif days > 365 and days <= 365*2:
#     print('2.servis aralığı')
# elif days > 365*2 and days <= 365*3:
#     print('3.servis aralığı')
# else: 
#     print('Yanliş süre')


#--------------------------------------------------------------
import datetime

tarih =(input('aracınız hangi tarihte trafiğe cıktı (2019/8/9) : '))
tarih = tarih.split('/')
simdi = datetime.datetime.now()
cikisTarihi= datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
fark = simdi - cikisTarihi
days =fark.days
if days <= 365:
    print('1.servis aralığı')
elif days > 365 and days <= 365*2:
    print('2.servis aralığı')
elif days > 365*2 and days <= 365*3:
    print('3.servis aralığı')
else: 
    print('Yanliş süre')
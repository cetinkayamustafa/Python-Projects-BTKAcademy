# x = 5
# hak = 5
# result = 5 < x < 10
# devam = 'e'

# #and
# result = (x > 5) and (x < 10) #koşulun her iki tarafı da doğru olursa değer true olur biri yanlış olursa false olur
# result = (hak > 0 ) and (devam == 'e')
# #or 
# result = ( x > 0) or   (x % 2 == 0) #Bir tanesinin doğru olması bizim için yeterliyse or kullanılır.
# #not
# result = not(x > 0) #sordugum sorunun cevabı true ise not koyarak tam tersi değeri alabiliriz, false ise de true değeri alabiliriz.
# #x, 5-10 arasında olan bir çift sayı mı ?
# result = (( x > 5) or ( x < 10) and ( x % 2 == 0 ))  
# print(result)
#--------------------------------------------------------------------------------------------------------------------------------------------

#q1 : 
# girilenSayi=int(input("Bir Sayı Giriniz : "))
# answer = (girilenSayi > 0 ) and (girilenSayi <=100)
# print (f'Sayı 0 ile 100 arasında mı : {answer}')

#--------------------------------------------------------------------------------------------------------------------------------------------

#q2 : 
# girilenSayi=int(input("Bir Sayı Giriniz : "))
# answer = (girilenSayi > 0 ) and (girilenSayi % 2 == 0)
# print(f'Girilen sayı pozitif çift sayı mı : {answer}')

#--------------------------------------------------------------------------------------------------------------------------------------------

#q3 : 

# eMail = 'mutiefendi@gmail.com'
# password = '12345'
# girilenEmail = input ('Email: ')
# girilenPass = input ('Password : ')
# result = (eMail == girilenEmail) and (girilenPass == password)
# print (f'Giriş Başarılı mı : {result}')


#--------------------------------------------------------------------------------------------------------------------------------------------

#q4 : 

# a = int(input('a : '))
# b = int(input('b : '))
# c = int(input('c : '))
# result = (a > b) and (a > c)
# print (f'A en büyük sayıdır : {result}')
# result = (b > a) and (b > c)
# print (f'B en büyük sayıdır : {result}')
# result = (c > a) and (c > b)
# print (f'C en büyük sayıdır : {result}')

#--------------------------------------------------------------------------------------------------------------------------------------------

#q5 :

# vize1 = float(input('Vize 1 : '))
# vize2 = float(input('Vize 2 : '))
# final = float(input('final  : '))
# ortalama = ((( vize1 + vize2) / 2) *0.6 + (final * 0.4))
# result = (ortalama >= 50 ) and (final >= 50)
# print(f'Öğrencinin ortalaması : {ortalama} ve geçme durumu : {result}')


#--------------------------------------------------------------------------------------------------------------------------------------------

#q6 : 

# name= input ('adınız: ')
# kilo = float(input('kilo: '))
# boy = float(input('boy : '))
# index = (kilo) / ( boy ** 2 )
# zayif = (index >=0) and (index <= 18.4)
# normal = (index >18.4) and (index <= 24.9)
# kilolu = (index >24.9) and (index <= 29.9)
# obez = (index >29.9) and (index <= 34.9)

# print (f'{name} kilo indeksin : {index } ve kilo değerlendirmen zayıf: {zayif}' )
# print (f'{name} kilo indeksin : {index } ve kilo değerlendirmen normal: {normal}' )
# print (f'{name} kilo indeksin : {index } ve kilo değerlendirmen kilolu: {kilolu}' )
# print (f'{name} kilo indeksin : {index } ve kilo değerlendirmen obez: {obez}' )








 
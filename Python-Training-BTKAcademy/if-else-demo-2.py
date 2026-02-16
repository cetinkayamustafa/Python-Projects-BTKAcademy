 #q1 : 


# sayi = float(input('sayi : '))
# result = (sayi > 0) and (sayi <= 100)
# if result:
#     print(f'sayı 0-100 arasındadır')
# else:
#     print('sayı 0-100 arasında değildir.')


#----------------------------------------------------
#q2 : 

# sayi = int(input('sayı: '))
# if (sayi > 0 ):
#     if (sayi % 2 == 0 ):
#         print('Girilen sayı pozitif çift sayıdır')
#     else:
#         print('girilen sayı pozitif ancak sayı tek')
# else:
#     print('girilen sayı negatif')
#----------------------------------------------------

#q3 : 

# email = 'mutiefendi@gmail.com'
# password = 'abc123'
# girilenEmail = input('email : ')
# girilenPass= input('pass : ')
# if (girilenEmail == email):
#     if (girilenPass == password):
#         print('giriş başarılı')
#     else:
#         print('parola yanlıs')
# else:
#     print('e mail yanlıs' )

#----------------------------------------------------
#q4 : 
# a = input ('a : ')
# b = input ('b : ')
# c = input ('c : ')

# if (a > b) and (a > c) : 
#     print('a en büyük sayıdır')
# elif (b > a) and (b > c) :
#     print('b en büyük sayıdır')
# elif (c > a) and (c > b) :
#     print('c en büyük sayıdır')    
# else:
#     print('hatalı işlem')

#----------------------------------------------------

#q5 : 

# vize1 = float(input ('vize 1 : '))
# vize2 = float(input ('vize 2 : '))
# final = float(input ('final: '))

# ortalama = ((vize1+vize2)/2) * 0.6 +(final *0.4)
# if ortalama >= 50 :
#     if final >=50:
#         print (f'öğrencinin ortalaması : {ortalama} ve geçme durumu başarılı')
#     else:
#         print (f'öğrencinin ortalaması : {ortalama} ve geçme durumu başarısız, finalden en az 50 almalısınız.')
# else:
#     print (f'öğrencinin ortalaması : {ortalama} ve geçme durumu başarısız')

#----------------------------------------------------

#q6: 

# name = input('adınız : ')
# kg = float(input('kilo : '))
# hg = float(input('boyunuz: '))

# index = (kg) / (hg ** 2)
# if (index >=0 ) and (index <= 18.4):
#     print(f'{name} kilo indeksin {index} ve kilo değerlendirmen zayıf.')
# elif (index >18.4 ) and (index <= 24.9):
#     print(f'{name} kilo indeksin {index} ve kilo değerlendirmen normal.')
# elif (index >24.9 ) and (index <= 29.9):
#     print(f'{name} kilo indeksin {index} ve kilo değerlendirmen kilolu.')
# elif (index >29.9 ) and (index <= 34.9):
#     print(f'{name} kilo indeksin {index} ve kilo değerlendirmen obez.')
# else:
#     print('bir sıkıntı var') 
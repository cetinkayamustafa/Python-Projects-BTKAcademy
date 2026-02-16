#1- gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyon


# def yazdir(kelime, adet):
#     print(kelime * adet)

# yazdir('Mustafa\n ', 10) 


#2- kendisine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyon

# def listeyiCevir(*params):
#     liste = []

#     for param in params:
#         liste.append(param)

#     return liste

# result = listeyiCevir(10,20,30, 'mustafa')
# print(result)



#3-gönderilen 2 sayı arasındaki tüm asal sayıları bulun



# def asalSayilariBul(sayi1,sayi2):
#     for sayi in range(sayi1,sayi2+1):
#         if sayi > 1 :
#             for i in range(2, sayi):
#                 if (sayi % i == 0):
#                     break
#             else:
#                 print(sayi)

# sayi1=int(input('Sayi 1 : '))
# sayi2=int(input('Sayi 2 : '))

# asalSayilariBul(sayi1,sayi2)



#4- kendisine gönderilen bir sayının tam bölenlerini bir liste hazırlayan fonksiyon


# def tamBolenleriBul(sayi):
#     tamBolenler = []

#     for i in range(2,sayi):
#         if sayi % i == 0:
#             tamBolenler.append(i)
#     return tamBolenler

# print(tamBolenleriBul(20))


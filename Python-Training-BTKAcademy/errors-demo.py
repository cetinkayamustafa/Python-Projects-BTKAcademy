liste = ["1","2","5a","10b","abc","10","50"]

#liste elemanları içindeki sayısal değerleri bulunuz.
# for x in liste : 
#     try:
#         result = int(x)
#         print(result)
#     except ValueError:
#         continue

# 2 : kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayı olduğundan emin olunuz aksi halde hata mesajı yazın


# while True:
#     sayi = input('Sayı : ')
#     if sayi == 'q':
#         break


#     try:
#         result = float(sayi)
#         print("girdiğiniz sayı ",result)
#     except:
#         print('geçersiz sayı')
#         continue


# 3: girilen parola içinde türkçe karakter hatası veriniz
# def check_password(parola):

#     turkce_karakterler = 'şçğüöıİ'
    
  
#     for i in parola:
#         if i in turkce_karakterler:
#             raise TypeError ('parola türkçe karakterler içeremez.')
#         else:
#             pass
#     print('geçerli parola')
# parola = input('parola : ')
# try:
#     check_password(parola)
# except TypeError as err:
#     print(err)
 #4 : faktöriyel fonsiyonu oluşturup fonksiyona gelen değer için hata mesajı verin

def faktöriyel(x):
    x = int(x)

    if x < 0 :
        raise ValueError('negatif değer')
    
    result = 1


    for i in range(1,x+1):
        result *=i
    return result

for x in [5,10,20,-3,'10a']:
    try:
        y = faktöriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)
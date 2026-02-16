# def usalma(number):
#     #two = usalma(2)
#     #three = usalma(3)

#     def inner(power):
#         return number ** power
    
#     return inner



# two = usalma(2)
# print(two(3))



# def yetki_sorgula(page):
#     def inner(role):
#         if role == 'Admin':
#             return "{0} rolünün {1} sayfasına ulaşabilir".format(role,page)
#         else:
#             return "{0} rolü {1} sayfasına ulaşamaz".format(role,page)
#     return inner
# admin_user = yetki_sorgula("Product Edit")
# print(admin_user("Admin"))
# print(admin_user("User"))



def islem(islem_adi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam +=1
        return toplam
    
    def carpma(*args):
        carpim = 1 
        for i in args:
            carpim*=i
        return carpim
    if islem_adi == "toplama":
        return toplam
    else:
        return carpma
    
toplama = islem("toplama")
print(toplama(1,2,3,4,5,6))
carpma = islem("Carpma")
print(carpma(1,2,3,4,5))
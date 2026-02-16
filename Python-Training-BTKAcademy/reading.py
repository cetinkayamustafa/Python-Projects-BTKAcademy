
# try:

#     file = open("mutiefendi.txt","r")
# except FileNotFoundError:
#     print("dosya okuma hatası")

# finally:
#     print("dosya kapandı")
#     file.close()


file =open("mutiefendi.txt","r",encoding='utf-8')

#for döngüsü

# for i in file:
#     print(i,end="")

#read()fonksiyonu

icerik = file.read()
print(icerik)


#readline() fonksiyonu
print(file.readline(),end="")


liste = file.readline()
print(liste)

file.close()
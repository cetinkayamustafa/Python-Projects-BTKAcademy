#dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
#kullanımı: open(dosya_adi,dosya_erişme_modu)
#dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.


# " w ": (Write) yazma modu. Dosyayı konumda oluşturur. işi bittiğinde siler
# "a" : (append) ekleme. Dosya konumda yoksa oluşturur. kalıcı olarak ekler
# "x" : (Create) oluşturma. Dosya zaten varsa hata verir
# "r ": (read) okuma varsayılan. dosya konumda yoksa hata verir.


#file = open("C:/users/mutiefendii/desktop/deneme.txt","w")
# file.close()




# file = open("newfile.txt", "w",encoding='utf-8')
# file.write("mutiefendi")

# file.close()

# file = open("mutiefendi.txt","a",encoding='utf-8')

# file.write("Mutiefendi\n")
# file.close()

# file = open("mutiefendi.txt","x",encoding='utf-8')
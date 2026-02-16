sayilar = [1,3,5,7,9,12,19,21]


# for sayi in sayilar:
#     if sayi % 3 == 0:
#         print(sayi)

# toplam = 0
# for sayi in sayilar:
#     toplam  = toplam + sayi # toplam +=sayi da yazılabilir.
# print ('toplam',toplam)


# for sayi in sayilar:
#     if sayi % 2 == 1:
#         print(sayi ** 2)


# sehirler = ['kocaeli', 'istanbul', 'ankara', 'izmir', 'zonguldak']

# for sehir in sehirler:
#     if(len(sehir) <= 5):
#         print(sehir)


urunler = [{'name' : 'iphone11', 'price': '10000'} ,
           {'name' : 'iphone12', 'price': '15000'} ,
           {'name' : 'iphone13', 'price': '20000'} ,
           {'name' : 'iphone14', 'price': '25000' },
           {'name' : 'iphone 4', 'price': '4999'}]
# toplam = 0
# for urun in urunler:
#     fiyat = int(urun['price'])
#     toplam += fiyat
# print(f'Ürünlerin toplam fiyatı : {toplam}')


for urun in urunler:
    if int(urun['price']) <= 5000:
        print(urun['name'])

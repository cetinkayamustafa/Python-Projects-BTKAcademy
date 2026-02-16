# # # # Cars = ["Bmw", "Mercedes", "Opel", "Mazda"]
# # # # # print(Cars)
# # # # # elemanSayisi=len(Cars)
# # # # # print(elemanSayisi)
# # # # # print(Cars[0])
# # # # # print(Cars[-1])
# # # # #Cars[-1]='Toyota'
# # # # Cars.remove("Mazda")
# # # # Cars.append("Toyota")
# # # # # print(Cars)
# # # # # #VAR MI SORUSUNA VAR ÖRNEĞİ ;
# # # # # result ='Mercedes' in Cars
# # # # # print(result)
# # # # # #VAR MI SORUSUNA YOK ÖRNEĞİ ;
# # # # # result ='mustafa' in Cars
# # # # # print(result)
# # # # # print(Cars[-2])
# # # # # print(Cars[0:3])
# # # # Cars.remove("Toyota")
# # # # Cars.append("Renault")
# # # # print(Cars)
# # # # #result=Cars + ['Audi','Nissan']
# # # # Cars.append("Audi")
# # # # Cars.append("Nissan")
# # # # # del Cars[-1]
# # # # # result = Cars
# # # # print(Cars)
# # # # Cars.pop(-1)
# # # # print(Cars)
# # # # # result = Cars[::-1]
# # # # Cars.reverse()
# # # # print(Cars)
# # # studentA = ['Yiğit', 'Bilgi',2010,[70,60,70]]
# # # studentB = ['Sena', 'Turan',1999,[80,80,70]]
# # # studentC = ['Ahmet', 'Turan',1998,[80,70,90]]
# # # # result=studentA[0]
# # # # result=studentB[1]
# # # # result=studentC[3][1]
# # # # print(result)
# # # result =f"{studentA[0]} {studentA[1]} {2026-studentA[2]} yaşında ve not ortalaması {studentA[3][0] + studentA[3][0] + studentA[3][1] + studentA[3][2]/3}"
# # # print(result)

# # #-------------------------------------------------------------------------------------

# # numbers = [1, 10, 5, 16, 4, 9, 10]
# # letters = ['a', 'g', 's', 'b', 'y', 'a', 's']

# # # val=min(numbers)
# # # val=max(numbers)
# # # val=min(letters)
# # # val=max(letters)
# # # val = numbers[3:6]
# # # val = numbers[:3]
# # # val = numbers[4:]
# # # print(val)
# # # numbers[4]=40
# # numbers.append(23)
# # numbers.insert(3, 78)
# # numbers.insert(-1, 51)
# # print(len(numbers))
# # print(len(letters))
# # print(numbers.count(10))
# # print(letters.count('a'))
# # print(numbers)
# #----------------------------------------------------------------

# names = ['Ali', 'Yağmur', 'Hakan', 'Deniz']
# years = [1998,2000,1998,1987]

# # names.append('Cenk')
# # names.insert(0, 'Sena')
# # names.remove('Deniz')
# # #result= 'Ali' in names
# # names.reverse()
# # #print(result)
# # #names.sort()
# # years.sort()
# # str = "Chervolet,Dacia"
# # result=str.split(',')
# # print(result)
# # min = min(years)
# # max=max(years)
# # print(min,max)
# # result=years.count(1998)
# # print(result)
# # # print(years)
# # # print(names)
# # years.clear()
# # print(years)
# markalar = []
# marka=input("Marka: ")
# markalar.append(marka)
# marka=input("Marka: ")
# markalar.append(marka)
# marka=input("Marka: ")
# markalar.append(marka)
# print(markalar)
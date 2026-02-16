#error handling => hata yönetimi
while True :
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)
    except ZeroDivisionError:
        print('Y için 0 girilemez')
    except ValueError:
        print('x ve y için sayısal değer girmelisiniz')
        #except ZeroDivisionError,ValueError as e:
            #print ('yanlıs bir değer girdiniz')
            #print(e) 
    else:
        break
    finally:
        print('try except sonlandı.')
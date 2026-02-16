def toplaam(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b

def islem(f1,f2,f3,f4, islem_adi):
    if islem_adi == "toplama":
        print(f1(2,3))
    elif islem_adi == "çıkarma":
        print(f2(5,3))
    elif islem_adi == "carpma":
        print(f3(3,4))
    elif islem_adi == "bölme":
        print(f4(10,2))
    else:
        print("geçersiz işlem")

islem(toplaam,cikarma,carpma,bolme,"toplama")
islem(toplaam,cikarma,carpma,bolme,"çıkarma")
islem(toplaam,cikarma,carpma,bolme,"carpma")
islem(toplaam,cikarma,carpma,bolme,"bölme")
islem(toplaam,cikarma,carpma,bolme,"deneme")
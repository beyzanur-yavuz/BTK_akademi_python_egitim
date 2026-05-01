
# def selamlama(isim):
#     print(f"Merhaba {isim}")
# selamlama("beyza")    

# del selamlama #fonksiyonu silmek için kullanılır 
#selamlama("beyza") #hata verir çünkü fonksiyon silindi

#iç içe fonksiyonlar:bu bize kapsüllemeyi sağlıyor.
# def outer():
#     def inner():
#         print("merhaba")
#     inner()   
# inner() #iç fonksiyona doğrudan erişilmez bu dorğu bir kullanım değil
# outer()

#faktöriyel örnek:

# def factorialrec(number):
#     def inner(number):
#         if number<=1:
#             return 1
#         return number*inner(number-1)
#     return inner(number)

# print(factorialrec(3))

# def factorial(number):
#     def inner():
#         sonuc=1
#         for i in range(1,number+1):
#             sonuc*=i
#         return sonuc
#     return inner()

# print(factorial(3))

# def usAlma(taban):
#     def inner(us):
#         return taban**us
#     return inner

# sonuc=usAlma(2)(3)#(taban)(us)

# def yetki_sorgulama(sayfa):
#     def inner(rol):
#         if rol=="Admin":
#             return  f"{rol} {sayfa} sayfasına erişebilir"
#         else:
#             return f"{rol} {sayfa} sayfasına erişemez"
#     return inner



# def hesapMakinesi(islem):
#     def topla(*args): 
#         toplam=0
#         for i in args:
#             toplam+=i 
#         return toplam
#     def carp(*args):
#         carpim=1
#         for i in args:
#             carpim*=i
#         return carpim
#     if islem=="topla":
#         return topla
#     else:
#         return carp
            

# def kare_al(sayi):
#     return sayi**2
# def kup_al(sayi):
#     return sayi**3

# def islem(fnc,liste):
#     sonuc=[]
#     for i in liste:
#         sonuc.append(fnc(i))
#     return sonuc
# sayilar=[1,2,3]
# sonuc=islem(kare_al,sayilar)
# print(sonuc)    













    
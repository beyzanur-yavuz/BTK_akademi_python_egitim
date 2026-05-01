             # LIST COMPREHENSION
# sayilar=[]
# for i in range(6):
#     sayilar.append(i**2)
# print(sayilar)   

#liste=[işlem(item) for item in iterable]  -->list comprehension.
# sayilar=[i**2 for i in range(6)]
# print(sayilar)

# isimler=["ebru","ali","beyza"]
# print(isimler)
# isimler2=[]

# for i in isimler:
#     isimler2.append(i.upper())
# print(isimler2)

# isimler2=[i.upper() for i in isimler] #upper hepsini büyük harfe dönüştürür.
# print(isimler2)

# metin="BTK AKADEMİ"
# harfler=[i for i in metin]
# print(harfler)

                 #FİLTRELEME comprehension

# [expression for item in liste if condition]
# sayilar=[2, 5 , 8 , 14 , 17]
# sayilar2=[i for i in sayilar if i%2==0]
# print(sayilar2)

# sehirler=  ["Ankara", "antalya","denizli","Afyon"]
# a_olanlar= [sehir for sehir in sehirler if "a" in sehir.lower()]
# print(a_olanlar)

# notlar=[50,60,40,85]
# sonuc=[ "gecti" if i>=50  else "kaldı" for i in notlar]
# print(sonuc)

         









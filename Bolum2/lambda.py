 #lambda:anonim fonksiyonlar oluşturmak içi kullanılır.
 #lambda arguments: expression

 # print ((lambda x,y: x+y)(5,10))

 # text="btk akademi"
 # sonuc= lambda x:x.upper()
 # print(sonuc(text))

 #iç içe lambda:
 # katlayici=lambda x:lambda y:x*y
 # ikikatinial=katlayici(2)
 # print(ikikatinial(5))

 # map fonksiyonu:dönüştürücü.

# sayilar=[1,2,3,4,5]
# def kareHesapla(i):
#     return i**2
# sonuc=map(lambda x:x**2,sayilar) map ile listeye fırlatıyoruz ve kareHesapla fonksiyonu ile her bir elemanı karesini alıyoruz. Sonuç map objesi olarak döner, bunu listeye çevirmek için list() fonksiyonunu kullanırız.
# print(list(sonuc))

# filter fonksiyonu:filtreleme yapar.

# def pozitifMi(x):
#      return x > 0
# sonuc=filter(pozitifMi,sayilar) #filter ile listeye fırlatıyoruz ve pozitifMi fonksiyonu ile her bir elemanı pozitif olanları filtreliyoruz. Sonuç filter objesi olarak döner, bunu listeye çevirmek için list() fonksiyonunu kullanırız.
# print(list(sonuc))

#sonuc=filter(lambda x:x>0,sayilar) #lambdalı hali.
# print(list(sonuc))


#all fonksiyonu:hepsi doğru mu diye bakıyor listedeki koşullardan.
# liste=[True,True,False]
# print(all(liste))

#any fonksiyonu:en az bir tanesi doğru mu diye bakıyor.
# print(any(liste))

#sorted fonksiyonu: sıralama yapar.
# sayilar=[5,2,9,1,3]
# print(sorted(sayilar))
# sayilar.sort()#bu şekilde de kullanım vardır.
# print(sayilar)
# print(sorted(sayilar,reverse=True)) #ters sıralama



















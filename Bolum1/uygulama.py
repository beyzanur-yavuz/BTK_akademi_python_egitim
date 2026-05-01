
# 1.örnek: 1-100 arasındaki sayılardan 12'ye tam bölünenleri listeleyen bir kod yazınız.

# liste=[i for i in range(1,100) if i%12==0]
# print(liste)

# 2.örnek: "BTK 2026 egitim yili 5.donem" metnindeki rakamları listeleyen bir kod yazınız.

# metin="BTK 2026 egitim yili 5.donem"
# rakamlar=[i for i in metin if i.isdigit()]
# print(rakamlar)

# 3.örnek: sicakliklar=[10,2,-3,5,0] listesinde 4'ten küçük olanlara "Buzlanma tehlikesi" diğerlerine "normal" yazan bir kod yazınız.

# sicakliklar=[10,2,-3,5,0]
# sonuc=["Buzlanma tehlikesi" if i<4 else "normal" for i in sicakliklar]
# print(sonuc)

# 4.örnek: ogrenciler=["Ali","Ayşe"] notlar=[40,70] listelerinde notu 50'den büyük olan öğrencilerin adını ve notunu sözlük olarak listeleyen bir kod yazınız.

# ogrenciler=["Ali","Ayşe"]
# notlar=[40,70]
# sonuc=[ {ogrenciler[i]:notlar[i]} if notlar[i]>=50 else None for i in range(len(notlar))]
# print(sonuc)

# 5.örnek: list1=[1,2,3] list2=[10,20] list1'deki her bir eleman ile list2'deki her bir elemanın çarpımını listeleyen bir kod yazınız.

# list1=[1,2,3]
# list2=[10,20]
# carpimlar=[i*j for i in list1 for j in list2]
# print(carpimlar)

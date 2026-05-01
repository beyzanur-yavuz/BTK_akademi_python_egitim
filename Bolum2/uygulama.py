
# 1.örnek
# ham_veriler = ["Ahmet", " ", "Meryem", None, "Ali", " ", "Selin"]
# temiz_isimler=list(filter(lambda x: x and x.strip(), ham_veriler)) 
# print(temiz_isimler) 
# 2.örnek: 

# ogrenciler = [
# {"ad": "Lale", "notlar": [70, 80, 90]},
# {"ad": "Deniz", "notlar": [40, 50, 30]},
# {"ad": "Arda", "notlar": [90, 95, 100]},
# {"ad": "Zeynep", "notlar": [60, 60, 70]} ]

# ortalama_hesapla=list(map(lambda ogrenci: {"ad": ogrenci["ad"],"notlar": ogrenci["notlar"], "ortalama": sum(ogrenci["notlar"])/len(ogrenci["notlar"])}, ogrenciler))
# print(ortalama_hesapla)
# filtrelenmis_ogrenciler=list(filter(lambda ogrenci:ogrenci["ortalama"]>=70,ortalama_hesapla))
# print(filtrelenmis_ogrenciler)
# print(sorted(ortalama_hesapla,key=lambda ogrenci:ogrenci["ortalama"],reverse=True))
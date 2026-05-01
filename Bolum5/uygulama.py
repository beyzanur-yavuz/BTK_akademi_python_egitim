class Ogrenci:
    def __init__(self,ad,soyad,ders_notu):
        self.ad=ad
        self.soyad=soyad
        self.ders_notu=ders_notu
    def durum_sorgula(self):
        if self.ders_notu >=50:
            return "Başarili"
        else:
            return "Başarisiz"
ogrenci1=Ogrenci("Beyza","Yavuz",89)
ogrenci2=Ogrenci("Ayse","Demir",45)
print(ogrenci1.durum_sorgula())
print(ogrenci2.durum_sorgula())
       

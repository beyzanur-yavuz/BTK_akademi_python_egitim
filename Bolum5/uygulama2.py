class Urun:
    urun_adet=0

    def __init__(self,ad,fiyat):
        self.ad=ad
        self.fiyat=fiyat
        Urun.urun_adet+=1
    @classmethod
    def toplam_urun_sayisi_getir(cls):
        print(f"Toplam urun sayisi: {cls.urun_adet}")

urun1=Urun("Telefon",1000)
urun2=Urun("Tablet",1500)
urun3=Urun("Laptop",8000)
Urun.toplam_urun_sayisi_getir()
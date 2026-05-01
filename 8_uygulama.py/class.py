class BaseProduct:
    def __init__(self, stok_kodu, fiyat, agirlik, stok_miktari):
        
        self.stok_kodu = stok_kodu
        self.fiyat = fiyat
        self.agirlik = agirlik
        self.stok_miktari = stok_miktari

    @property
    def stok_kodu(self):
        return self._stok_kodu

    @stok_kodu.setter
    def stok_kodu(self, value):
        if not value or len(str(value)) < 3:
            raise ValueError("Stok kodu en az 3 karakter olmalıdır.")
        self._stok_kodu = value

    @property
    def fiyat(self):
        return self._fiyat

    @fiyat.setter
    def fiyat(self, value):
        if value < 0:
            raise ValueError("Fiyat negatif olamaz.")
        self._fiyat = value

    @property
    def agirlik(self):
        return self._agirlik

    @agirlik.setter
    def agirlik(self, value):
        if value <= 0:
            raise ValueError("Ağırlık 0'dan büyük olmalıdır.")
        self._agirlik = value

    @property
    def stok_miktari(self):
        return self._stok_miktari

    @stok_miktari.setter
    def stok_miktari(self, value):
        if value < 0:
            raise ValueError("Stok miktarı negatif olamaz.")
        self._stok_miktari = value

    def calculate_shipping(self):
        
        return 100 + (self.agirlik * 10)

    def __str__(self):
        return f"[{self.stok_kodu}] Fiyat: {self.fiyat} ₺ | Ağırlık: {self.agirlik}kg | Stok: {self.stok_miktari}"

class ElectronicProduct(BaseProduct):
    def __init__(self, stok_kodu, fiyat, agirlik, stok_miktari, garanti_suresi):
        super().__init__(stok_kodu, fiyat, agirlik, stok_miktari)
        self.garanti_suresi = garanti_suresi

    @property
    def garanti_suresi(self):
        return self._garanti_suresi
        
    @garanti_suresi.setter
    def garanti_suresi(self, value):
        self._garanti_suresi = value

    def calculate_shipping(self):
        
        return super().calculate_shipping() * 1.2

    def __str__(self):
        return super().__str__() + f" | Garanti: {self.garanti_suresi} Ay (Elektronik)"

class FoodProduct(BaseProduct):
    def __init__(self, stok_kodu, fiyat, agirlik, stok_miktari, expiry_date):
        super().__init__(stok_kodu, fiyat, agirlik, stok_miktari)
        self.expiry_date = expiry_date

    @property
    def expiry_date(self):
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, value):
        self._expiry_date = value

    def calculate_shipping(self):
        
        return super().calculate_shipping() * 1.1

    def __str__(self):
        return super().__str__() + f" | SKT: {self.expiry_date} (Gıda)"

class HazardousProduct(BaseProduct):
    def __init__(self, stok_kodu, fiyat, agirlik, stok_miktari, safety_level):
        super().__init__(stok_kodu, fiyat, agirlik, stok_miktari)
        self.safety_level = safety_level

    @property
    def safety_level(self):
        return self._safety_level

    @safety_level.setter
    def safety_level(self, value):
        self._safety_level = value

    def calculate_shipping(self):
        
        return super().calculate_shipping() * 1.5

    def __str__(self):
        return super().__str__() + f" | Tehlike Seviyesi: {self.safety_level} (Tehlikeli Madde)"

class InventoryManager:
    def __init__(self):
        self._products = []
        self._index = 0

    def add_product(self, product):
        self._products.append(product)

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self._products):
            current = self._products[self._index]
            self._index += 1
            return current
        raise StopIteration
        
class LogisticsProcessor:
    def process_shipping(self, product):
        """Çok biçimlilik (Polymorphism) örneği."""
        print(f"{product.stok_kodu} kodlu ürünün kargo maliyeti: {product.calculate_shipping()} ₺")

    def critical_stock_generator(self, inventory_manager, threshold=5):
        """Stok miktarı kritik seviyede olanları generator ile döner."""
        for product in inventory_manager:
            if product.stok_miktari <= threshold:
                yield product

def main():
    manager = InventoryManager()
    processor = LogisticsProcessor()
    
    while True:
        print("\n=== Akıllı Depo Yönetim Sistemi ===")
        print("1. Ürün Ekle")
        print("2. Ürünleri Listele")
        print("3. Kargo Maliyetlerini Hesapla")
        print("4. Kritik Stok Uyarıları (Generator)")
        print("5. Çıkış")
        
        secim = input("Seçiminiz: ")
        
        if secim == "1":
            try:
                tur = input("Ürün Türü (E: Elektronik, G: Gıda, T: Tehlikeli Madde): ").upper()
                kodu = input("Stok Kodu (Örn: A10, PRO200): ")
                fiyat = float(input("Fiyat: "))
                agirlik = float(input("Ağırlık (kg): "))
                stok = int(input("Stok Miktarı: "))
                
                if tur == 'E':
                    garanti = input("Garanti Süresi (Ay): ")
                    urun = ElectronicProduct(kodu, fiyat, agirlik, stok, garanti)
                elif tur == 'G':
                    skt = input("Son Kullanma Tarihi: ")
                    urun = FoodProduct(kodu, fiyat, agirlik, stok, skt)
                elif tur == 'T':
                    seviye = input("Tehlike Seviyesi: ")
                    urun = HazardousProduct(kodu, fiyat, agirlik, stok, seviye)
                else:
                    print("Hatalı ürün türü!")
                    continue
                    
                manager.add_product(urun)
                print("Ürün başarıyla eklendi!")
                
            except ValueError as e:
                print(f"\nHATA: Geçersiz değer girdiniz -> {e}")
                
        elif secim == "2":
            print("\n--- Depodaki Ürünler ---")
            for urun in manager:
                print(urun)
                
        elif secim == "3":
            print("\n--- Kargo Maliyetleri ---")
            for urun in manager:
                processor.process_shipping(urun)
                
        elif secim == "4":
            try:
                limit = int(input("Kritik Stok Sınırı (Varsayılan 5): ") or 5)
                print(f"\n--- {limit} Adet ve Altındaki Kritik Ürünler ---")
                generator = processor.critical_stock_generator(manager, threshold=limit)
                for kritik in generator:
                    print(kritik)
            except ValueError as e:
                print("Hata, sadece sayısal bir limit belirtebilirsiniz.")
                
        elif secim == "5":
            print("Çıkış yapılıyor...")
            break
            
        else:
            print("Geçersiz seçim, lütfen 1-5 arası bir değer girin.")

if __name__ == '__main__':
    main()




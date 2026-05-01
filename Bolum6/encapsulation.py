class Product:
    def __init__(self,name,price):
        self.name=name
        if price > 0:
             self._price=price
        else:
            raise ValueError("urun fiyati sıfırdan düşük olamaz")
        #self.price=self.price(price)
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,value):
        if value > 0:
             self._price=value
        else:
            raise ValueError("urun fiyati sıfırdan düşük olamaz")
    
    # def set_price(self,value):
    #     if value > 0:
    #          self._price=value
    #     else:
    #         raise ValueError("urun fiyati sıfırdan düşük olamaz")
        
    # def get_price(self):
    #     return self._price

p1=Product("Laptop",5000)
p1.price = 9000 
print(p1.name,p1.price)

# Public (name): Herkes erişebilir, herkes değiştirebilir.
# Protected (_name): "Lütfen dışarıdan erişme, sadece sınıf ve alt sınıflar
# için" mesajı verir. (Tek alt çizgi).
# Private (__name): "Buna kesinlikle dışarıdan erişme!" mesajı verir. (Çift
# alt çizgi). Python burada Name Mangling yaparak ismi değiştirir, erişimi
# zorlaştırır.





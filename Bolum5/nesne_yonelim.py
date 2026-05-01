#class anahtar kelimesi ile sınıf tanımlarız.
# self: "Benim (nesnenin) verilerimle uğraşıyorum."
# cls: "Sınıfın (şablonun) ortak verileriyle uğraşıyorum."

class CartItem:
    discount_rate=0.2 #class attribute oluyor bu.
    item_count=0

    @classmethod
    def display_count(cls):
        return f"{cls.item_count} adet ürün var."
    
    @classmethod
    def create_item(cls,data_str):
        name,price,quantity=data_str.split(",")
        return cls(name,price,quantity)
    

    def __init__(self, name, price, quantity):
    #constructor methodu, sınıfın bir nesnesi oluşturulduğunda otomatik olarak çağrılır. Nesnenin özelliklerini tanımlamak için kullanılır.
        #instances 
        self.name = name #this kelimesi yerine burada self kullanılır.
        self.price = price
        self.quantity = quantity
        CartItem.item_count += 1
      #instance method:  
    def calculate_total_price(self):
        total_price = self.price * self.quantity
        return total_price
    def apply_discount(self):
        self.price=self.price *(1-self.discount_rate)
        

item1 = CartItem("Telefon", 1000, 2) #sınıfın bir nesnesini oluşturduk.


print(item1.name,item1.price,item1.quantity)
#Çıktı: Telefon 1000 2

total = item1.calculate_total_price()
print("Toplam Fiyat:", total)
print(item1.apply_discount())
print(item1.price)
print(CartItem.display_count())


CartItem.create_item("Laptop,2000,1")
print(CartItem.display_count())


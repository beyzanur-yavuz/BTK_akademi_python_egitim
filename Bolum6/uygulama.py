class Product:

    def __init__(self,name,price):
        self.name=name
        self.price=price


    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,value):
        if value>0:
            self._price=value
        else:
            print("urun fiyati sıfırdan dusuk olamaz")

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.name == other.name and self.price == other.price
    
p1=Product("Laptop",5000)

print(p1.price)


class ShoppingCart:
    def __init__(self):
        self.products=[]
    def add_product(self,product):
        if isinstance(product,Product):
            self.products.append(product)
        else:
            print("sadece Product nesneleri eklenebilir")     
    def kontrol(self,product):
        if product in self.products:
            print("urun sepette var")
        else:
            print("urun sepette yok")

    def total_price(self):
        return sum(product.price for product in self.products)

    def __str__(self):
        return f"ShoppingCart with {len(self.products)} products and total price: {self.total_price()}"
    
    def __len__(self):
        return len(self.products)


cart=ShoppingCart()
cart.add_product(p1)
print(cart)
print(len(cart))
cart2=ShoppingCart()
cart2.add_product(Product("Phone",3000))
print(cart2)
print(cart2.total_price())

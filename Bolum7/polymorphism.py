# hayvanlar=["kedi","köpek","kuş"]

# for h in hayvanlar:
#     if isinstance(h,Kedi):
#         print("miyav")
#     elif isinstance(h,Köpek):
#         print("hav hav")
#     elif isinstance(h,Kuş):
#         print("cik cik")


# class Animal():
#     def speak(self):
#         print("hayvanlar ses çıkarırır")


# class Dog(Animal):
#     def speak(self):
#         print("hav hav")

# class Cat(Animal):
#     def speak(self):
#         print("miyav miyav")


# d1=Dog()
# d1.speak()
# c1=Cat()
# c1.speak()

class Sekil():
    def __init__(self,kenar1):
        self.kenar1=kenar1
    def alanHesapla(self):
        return self.kenar1*self.kenar1    

class Kare(Sekil):
    pass

class Daire(Sekil):
    def alanHesapla(self):
        return 3.14*self.kenar1*self.kenar1

class Dıkdortgen(Sekil):
    def __init__(self,kenar1,kenar2):
        super().__init__(kenar1)
        self.kenar2=kenar2
    def alanHesapla(self):
        return self.kenar1*self.kenar2

    
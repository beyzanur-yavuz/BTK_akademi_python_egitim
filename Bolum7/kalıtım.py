class person:
    def __init__(self,name,surname,age):
        self.name=name
        self.surname=surname
        self.age=age
        print("person sinifi olusturuldu.")

    def intro(self):
        print("merhaba",self.name)




class student(person):#kalıtımı yaparken böyle yaparız.
    def __init__(self,name,surname,age,number):
        super().__init__(name,surname,age)
        self.number=number
        print("student sinifi türetildi.")

    def study(self):
        print(self.name,"ders çalışıyor.")

    def intro(self):#overriding yaptık.
        print("merhabe ben",self.name)    
            



class teacher(person):#kalıtımı yaparken böyle yaparız.
    def __init__(self,name,surname,age,branch):
        super().__init__(name,surname,age)
        self.branch=branch
        print("teacher sinifi türetildi.")

    def teach(self):
        print(self.name,"öğretmenlik yapıyor.")
        

student1=student("Ali","Veli",20,123)
print(student1.name)
print(student1.number)
student1.intro()






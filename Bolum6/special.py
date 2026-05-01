class movie:
    def __init__(self,title,year,diractor,duration):
        self.title=title
        self.year=year
        self.diractor=diractor
        self.duration=duration
    def __repr__(self):
        return f"{self.title}({self.year}) director{self.diractor} and duration is {self.duration} minutes"

    def __len__(self):
        return self.duration





m1=movie("titanic",1997,"nolan",190)
#print(m1)#bellekte nerede tutuldugunu gösteriyor
print(m1.__repr__())
print(m1.__len__())




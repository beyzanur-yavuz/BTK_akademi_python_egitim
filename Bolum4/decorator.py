
# def selamlama(fn):
#     def inner(isim):
#         print("hoş geldiniz")
#         fn(isim)
#         print("gorusmek uzere")
#     return inner   


# @selamlama #decorator
# def gunaydin(isim):
#     print(f"günaydin {isim}")

# @selamlama #decorator
# def iyi_gunler(isim):
#    print(f"iyi günler {isim}")
    
# gunaydin("Ahmet")
# iyi_gunler("Mehmet")

# *args, **kwargs: 

# def double_func(fn):
#      def inner(*args,**kwargs):
#           fn(*args,**kwargs)
#           fn(*args,**kwargs)
#      return inner 

# @double_func
# def merhaba(isim): #paremetreli fonksiyon
#      print(f"merhaba {isim}")

# @double_func
# def selam(): #parametresiz fonksiyon
#      print("selam")


# merhaba("beyza")
# selam()

#decoratora parametre gondermek.
# def selamlama_dec(count):
#    def selamlama(fn):
#       def inner(isim):
#           for i in range(count):
#               fn(isim)
#       return inner 
#    return selamlama



# @selamlama_dec(8)
# def merhaba(isim): #paremetreli fonksiyon
#       print(f"merhaba {isim}")

# merhaba("beyza")




















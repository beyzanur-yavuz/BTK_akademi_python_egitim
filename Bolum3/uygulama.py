
# 1.örnek:
# def islem_merkezi(sayi1,sayi2):
#     def topla():
#         return sayi1+sayi2
#     def cıkar():
#         return sayi1-sayi2
#     def bol():
#         return sayi1/sayi2
#     return {"toplam": topla(), "fark": cıkar(), "bolum": bol()} 

# islem=islem_merkezi(4,2)
# print(islem)

#2.örnek:
# def logger(seviye):
#    def mesaj_yaz():
#       if seviye=="info":
#          return f"sistem çalışıyor"
#       elif seviye=="error":
#          return f"bağlantı kesildi"
#       elif seviye=="debug":
#          return f"hata oluştu"  
         
#    return mesaj_yaz()

# print(logger("info"))     

#3.örnek:
# def hesap_makinesi(liste,islem_fonksiyonu):
#    if islem_fonksiyonu=="kare_alma":
#       def kare_al(liste):
#             sonuc=[]
#             for i in liste:
#                 sonuc.append(i**2)
#             return sonuc
#       return kare_al(liste)
#    elif islem_fonksiyonu=="kok_alma":
#         def kok_al(liste):
#                 sonuc=[]
#                 for i in liste:
#                     sonuc.append(i**0.5)
#                 return sonuc
#         return kok_al(liste)
   
# print(hesap_makinesi([4,9,16],"kare_alma"))



       
# import re #re modülü kullanılıyor.

# text="BTK AKADEMİ PYTHON KURSU"
# sonuc=re.search("BTK",text)
# print(sonuc)
# nerede=sonuc.span() #hangi aralıkta olduğunu gösteririr.
# print(nerede)

# #sub ile istediğimiz ifadeyi değiştiriyoruz.
# yeni_text=re.sub("PYTHON","JAVA",text)

# import re
# text="ABC 123 983 1A3 1_2"
# pattern=r"\d\d\d"    #\d rakamları temsil eder. \d\d\d ise 3 tane rakamı temsil eder.    
# pattern=r"\d{3}"     #\d{3} ifadesi de 3 tane rakamı temsil eder.
# pattern=r"\d+"       #\d+ ifadesi ise 1 veya daha fazla rakamı temsil eder.
# pattern=r"\s"       #\s ifadesi boşluk karakterini temsil eder.
# sonuc=re.findall(pattern,text)
# print(sonuc)

# email_text="beyza@btk.gov.tr"
# email_pattern=r"\w+@\w+\.\w+" #\w harfleri ve rakamları temsil eder. @ ve . karakterlerini de ekledik.
# e_match=re.findall(email_pattern,email_text)
# print(e_match)

#gereksiz şeyleri temizleme
# import re 
# data="Fiyat: $1,200.00 | İndirim: %10"
# pattern=r"[^0-9.,]"
# clean_data=re.sub(pattern,"",data)
# print(clean_data)








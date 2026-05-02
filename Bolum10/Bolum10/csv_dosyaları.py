import csv
#csv.reader() ile csv dosyasını okuyabiliriz

# with open('test.csv','r', encoding='utf-8') as file:
#     reader =csv.reader(file)
#     next(reader) # başlık satırını atlamak için
#     for satir in reader:
#         print(f"Ürün Adı: {satir[1]}, Fiyat:{satir[2]}")


#csv.DictReader() ile csv dosyasını okuyabiliriz.

# with open('test.csv','r', encoding='utf-8') as file:
#     dict_reader=csv.DictReader(file)
#     for satir in dict_reader:
#         print(f"Ürün Adı: {satir['Urun']}, Fiyat:{satir['Fiyat']}")

#csv.writer() ile csv dosyasına yazabiliriz.

# with open('yeni_test.csv','w',encoding='utf-8',newline='') as file:
#     writer=csv.writer(file)
#     writer.writerow(['ID','Urun','Fiyat'])
#     writer.writerow([1,'Laptop',5000])
#     writer.writerow([2,'Telefon',3000])


#csv.DictWriter() ile csv dosyasına yazabiliriz.
# fieldnames=['ID','Urun','Fiyat']
# urunler=[
#     {'ID':1,'Urun':'Laptop','Fiyat':8000},
#     {'ID':2,'Urun':'Telefon','Fiyat':3000}
# ]
# with open('yeni_test.csv','w',encoding='utf-8',newline='') as file:
#     dict_writer=csv.DictWriter(file,fieldnames=fieldnames)
#     dict_writer.writeheader() # başlık satırını yazmak için
#     dict_writer.writerows(urunler) # birden fazla satır yazmak için




    

















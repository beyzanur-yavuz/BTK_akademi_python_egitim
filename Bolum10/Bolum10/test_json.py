import json


# JSON (JavaScript Object Notation) verileri depolamak ve iletmek için kullanılan hafif bir veri formatıdır.
# Python'da JSON verilerini işlemek için json modülünü kullanabilirsiniz.

# with open('products.json', 'r', encoding='utf-8') as file:
#     data=json.load(file)
#     print(data)

# print(data[0]["productName"])
# print(data[0]["price"])


#json.loads() 

# json_string= """{
#         "id": 1,
#         "productName": "Iphone 14",
#         "price": 15000,
#         "kategory": "Telefon",
#         "isPublished": "true"
#     }"""

# result=json.loads(json_string)
# print(result)


#json.dumps()

# person_dict={"name":"ali","language":"python"}
# result=json.dumps(person_dict)
# print(result)

# person_dict={"name":"ali",
#              "language":["python"],
#              }
# with open('person.json','w',encoding='utf-8') as file:
#     json.dump(person_dict,file)










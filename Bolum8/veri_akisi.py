# liste=[1,2,3,4,5]
# iterator=iter(liste)

# # while True:
# #     try:
# #         sayi=next(iterator)
# #         print(sayi)
# #     except StopIteration:
# #         break


# print(next(iterator))

#custom iterator:
# class MyNumber:
#     def __init__(self,start,stop):
#         self.start=start
#         self.stop=stop
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.start<self.stop:
#             x=self.start
#             self.start+=1
#             return x
#         else:
#             raise StopIteration

# for i in MyNumber(1,10):
#     print(i)

#generators:
# def count(max):
#     sayilar=[]
#     sayi=0
#     while sayi<= max:
#         sayilar.append(sayi)
#         sayi+=1
#     return sayilar
# print(count(15))



# def count_gen(max):
#     for i in range(max):
#         yield i #return değil yield kullanarak generator oluşturuyoruz


# gen=count_gen(15)
# for x in gen:
#     print(x)

# #fibonacci serisi gensiz
# liste=[]
# sayi1,sayi2=0,1
# while len(liste)<=max:
#     liste.append(sayi2)
#     sayi1 ,sayi2 = sayi2 ,sayi1+sayi2

#fibonacci serisi generator ile
# def fib_gen(max):
#     sayi1,sayi2=0,1
#     while sayi2<max:
#          yield sayi2
#          sayi1,sayi2=sayi2,sayi1+sayi2
#         


# for i in fib_gen(10):
#     print(i)



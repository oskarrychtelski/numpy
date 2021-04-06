import numpy as np

#zad.1
# b=3**np.arange(15)
# print(b)

#zad.2
# a=np.arange(1.2,100,3.23)
# b=(a.astype('int64'))
# print(b.dtype)


#zad.3
# n=int(input("podaj liczbę całkowita: "))
# x, y=np.mgrid[0:n,0:n]
# print(y)

#zad.4
# def potegowanko(podstawa,ile):
#     print(np.logspace(0,ile,base=podstawa,num=ile+1,dtype='int'))
# potegowanko(3,4)

#zad.5
# def przekatna(dlugosc):
#     wektor=np.diag([a for a in reversed(range(dlugosc))])
#     print(wektor)
# przekatna(5)


#zad.6
# b=np.array([['m','a','l','p','a'],['h','a','l','z','p'],['x','a','m','a','t'],['d','f','g','a','j']])
# print(b)


#zad.7
# def symetryczna(n):
#     dwojki_diag=np.diag([2 for a in range(n)])
#     dwojki=np.array([2 for a in range(n)])
#     for a in range(n):
#         np.fill_diagonal(dwojki_diag[a+1:],dwojki+2*a+2)
#         np.fill_diagonal(dwojki_diag[:,a+1:], dwojki +2*a+2)
#     print(dwojki_diag)
#
# symetryczna(6)


#zad8
# def dzielenie(mat,kierunek):
#     if kierunek=='poziom':
#         if len(mat)%2==0:
#             print(mat[:int(len(mat)/2)])
#             print(mat[int(len(mat)/2):])
#         else:
#             print("tablica nie pozwala na podzial na pol")
#     if kierunek == 'pion':
#         if len(mat[0]) % 2 == 0:
#             print(mat[:,0:int(len(mat[0])/2)])
#             print(mat[:,int(len(mat[0])/ 2):])
#         else:
#             print("tablica nie pozwala na podzial na pol")
# x=np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]])
# dzielenie(x,'pion')


#zad.9 chcialem przykozaczyc robiąc funkcję, ale to jednak nie był dobry pomysł
# def fibonacci(rozmiar):
#     x=[]
#     for a in range(rozmiar):
#         if a==0:
#             x.append(0)
#         elif a==1:
#             x.append(1)
#         else:
#             x.append(x[a-1]+x[a-2])
#     x=np.array(x)
#     x = x.reshape(5,5)
#     print(x)
# fibonacci(25)
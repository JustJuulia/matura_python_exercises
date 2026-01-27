# slicing start:stop:step tablica dwuymiarowa [0:3} => wypisze mi o idx 0, 1, 2
#10x10 [y][x] iloczyn
'''
tabliczka = [[x*y for x in range(10)] for y in range(10)]
# print(tabliczka)
from copy import deepcopy
lista1 = [1,2,3,4]
lista2 = lista1
lista2[0] = "ashjdasd"
# print(lista1,lista2) ashjdasd jest w obu listach
# zeby temu zapobiec
lista3 = deepcopy(lista1)
lista3[1] = "asdasdasd"
# print(lista1,lista2,lista3) asdasdsadasd jest tylko w 3
'''
# dla kazdego wiersza średnia
zagadka = [
  [56, 18, 76, 56, 97],
  [31, 20, 72, 59, 39],
  [74, 76, 82, 92, 74],
  [44, 16, 62, 27, 43],
  [88, 48, 64, 12, 58]
]
for wiersz in zagadka:
    suma = 0
    ilosc = 0
    for element in wiersz:
        suma = suma + element
        ilosc += 1
    print(suma/ilosc)

'''
ZADANIE 3.2
def nieparzysty_skrot(n_poczatkowe, tab):
    n = n_poczatkowe
    m = 0
    counter = 0
    while n>0:
        if n % 2 == 0:
            n = n//10
        else:
            if counter != 0:
                a = 1
                for i in range(counter):
                    a = a * 10
                m = m + (n % 10)*(a)
            else:
                m = m + (n % 10)
            counter = counter + 1
            n = n//10
    if m == 0:
        tab.append(n_poczatkowe)
    return tab
def najwieksza(tab):
    tab.sort()
    return tab[-1]
f = open("skrot.txt", "r")
tab = []
for line in f:
    tab = nieparzysty_skrot(int(line), tab)
print("ilosc: ", len(tab), "najwieksza: ",najwieksza(tab))
f.close()
'''

''' ZADANIE 3.3 
def nieparzysty_skrot_2(n_poczatkowe, slownik):
    n = n_poczatkowe
    m = 0
    counter = 0
    while n>0:
        if n % 2 == 0:
            n = n//10
        else:
            if counter != 0:
                a = 1
                for i in range(counter):
                    a = a * 10
                m = m + (n % 10)*(a)
            else:
                m = m + (n % 10)
            counter = counter + 1
            n = n//10
    slownik.update({n_poczatkowe:m})
    return slownik
def nwd(a,b):

    dziel_a = []
    dziel_b = []
    dziel_a.append(a)
    dziel_b.append(b)
    if a ==1:
        dziel_a.append(1)
    if b ==1:
        dziel_b.append(1)
    for x in range(round((a/2))):
        if x != 0:
            if a % x ==0:
                dziel_a.append(x)
    for x in range(round(b/2)):
        if x!= 0:
            if b % x ==0:
                dziel_b.append(x)
    dziel_a.sort(reverse=True)
    dziel_b.sort(reverse=True)
    wspolne_dz = []
    if len(dziel_b) > len(dziel_a):
        for i in range(len(dziel_b)):
            for j in range(len(dziel_a)):
                if dziel_b[i] == dziel_a[j]:
                    wspolne_dz.append(dziel_a[j])
    else:
        for i in range(len(dziel_a)):
            for j in range(len(dziel_b)):
                if dziel_b[j] == dziel_a[i]:
                    wspolne_dz.append(dziel_a[i])
    wspolne_dz.sort(reverse=True)
    return wspolne_dz[0]
f = open("skrot2.txt", "r")
tab = {}
for line in f:
    tab = nieparzysty_skrot_2(int(line), tab)
    dzielnik = nwd(list(tab)[-1], tab[list(tab)[-1]])
    if dzielnik == 7:
        print(list(tab)[-1])
f.close()
'''

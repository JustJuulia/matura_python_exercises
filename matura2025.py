# 1. 84 500 10712 1.2 10 1.3 1 10
def f(a,b, counter):
    counter += 1
    def ostatnia(x):
        xs = str(x)
        return int(xs[-1])
    def skroc(x):
        string_x = str(x)
        if len(string_x) > 1:
            x = int(string_x[0:-1])
        elif len(string_x) == 1:
            x = 0
        return x
    def dopisz(x):
        if x == 0:
            return 0
        stx = str(x)
        stx = stx + '0'
        x = int(stx)
        return x
    if b == 0:
        return 0
    k = ostatnia(b)
    w = f(a, skroc(b), counter)
    w = dopisz(w)
    while k > 0:
        w = w + a
        print("w+wa wykonane!!!")
        k = k - 1
    return w

# print(f(2024, 1234, 1))
#2.
def ciecie_2(k):
    k = int(k)
    def nwd(q,w):
       while w != 0:
            q = q % w
            q, w = w, q
       if q != 1:
            return 0
       else:
            return 1
    l = 0
    k_count = k
    while k_count > 0:
        k_count = int(k_count / 10)
        l+=1
    mnoznik = 1
    for i in range(int(l/2)):
        mnoznik = mnoznik * 10
    a, b = int(k/mnoznik), int(k - int(k/mnoznik)*mnoznik)
    if nwd(int(a), int(b)) == 1:
        return 1
    else:
        return 0
zad2 = open('liczby1.txt', "r")
polowiczniewzgledne = 0
for line in zad2:
    liczba = int(line)
    polowiczniewzgledne += ciecie_2(liczba)
odpzad2 = open("wyniki2_2.txt", "w")
odpzad2.write("Ilość połowicznie względnych liczb wynosi: " + str(polowiczniewzgledne))
zad2.close()
odpzad2.close()

#2.3
def ciecie_3(k):
    k = int(k)
    przed_potega = k
    k = k*k
    l = 0
    k_count = k
    while k_count > 0:
        k_count = int(k_count / 10)
        l+=1
    mnoznik = 1
    counter = 1
    zliczacz_kapera = 0
    while counter < l:
        mnoznik = mnoznik * 10
        a, b = int(k / mnoznik), int(k - int(k / mnoznik) * mnoznik)
        if a + b <= przed_potega:
            zliczacz_kapera+=1
        counter += 1
    return zliczacz_kapera

zad2 = open('liczby2.txt', "r")
max_zliczacz = 0
linijka_z_zliczacza = 0
linijka = 0
najw_liczba = 0
for line in zad2:
    liczba = int(line)
    karper = ciecie_3(liczba)
    if karper > max_zliczacz:
        max_zliczacz = karper
        linijka_z_zliczacza = linijka
        najw_liczba = liczba
    linijka+=1
odpzad2 = open("wyniki2_3.txt", "w")
odpzad2.write("wysokość karpera: "+str(max_zliczacz)+" liczba do niego rpzypisana: "+str(najw_liczba))
zad2.close()
odpzad2.close()

#ZADANIE 3_1
def ile_liczb_1(c):
    moje_liczby = []
    idx_konczacy = 0
    for i in range (0,len(c)):
        if i >= idx_konczacy:
            if i == 0:
                if c[i] == '5':
                    if c[i + 1] == '0':
                        podciag = c[i + 2:]
                        liczba = '50'
                        idx_konczacy = i + 2
                        for j in range(0, len(podciag)):
                            try:
                                int(podciag[j])
                                idx_konczacy += 1
                                liczba = liczba + podciag[j]
                            except:
                                moje_liczby.append(liczba)
                                break
            elif c[i-1] != '1' and c[i-1] != '2' and c[i-1] != '3' and c[i-1] != '4' and c[i-1] != '5' and c[i-1] != '6' and c[i-1] != '7' and c[i-1] != '8' and c[i-1] != '9' and c[i-1] != '0':
                if c[i] == '5':
                    if c[i + 1] == '0':
                        podciag = c[i + 2:]
                        liczba = '50'
                        idx_konczacy = i + 2
                        for j in range(0, len(podciag)):
                            try:
                                int(podciag[j])
                                idx_konczacy += 1
                                liczba = liczba + podciag[j]
                            except:
                                moje_liczby.append(liczba)
                                break
    return len(moje_liczby)

plik = open("dane.txt","r")
ilosc = 0
for line in plik:
    ilosc += ile_liczb_1(line)
plik.close()
wyniki = open("wyniki3_1.txt", "w")
wyniki.write("zadanie 3.1: " + str(ilosc))
plik.close()
wyniki.close()

#ZADANIE 3_2
def ile_liczb_2(c, pl):
    moje_liczby = []
    idx_konczacy = 0
    for i in range (0,len(c)):
        if i >= idx_konczacy:
            if c[i].isdigit():
                liczb = c[i]
                podciag = c[i + 1:]
                idx_konczacy = i + 1
                for j in range(0, len(podciag)):
                    try:
                        int(podciag[j])
                        idx_konczacy += 1
                        liczb = liczb + podciag[j]
                    except:
                        moje_liczby.append(liczb)
                        break
    for l in moje_liczby:
        for z in l:
            if z in pl:
                pl[z] += 1
            else:
                pl[z] = 1

    return len(moje_liczby), pl

plik = open("dane.txt","r")
liczba = 0
ilosc = 0
powtorzenia_lib = {}
for line in plik:
    liczba, powtorzenia_lib = ile_liczb_2(line, powtorzenia_lib)
plik.close()
wyniki = open("wyniki3_2.txt", "w")
max_powtorzona_liczba = 0
ilosc_powtorzen_max = 0
max_powtorzona_liczba = max(powtorzenia_lib, key=powtorzenia_lib.get)
ilosc_powtorzen_max = powtorzenia_lib[max_powtorzona_liczba]
wyniki.write("zadanie 3.2, liczba: " + str(max_powtorzona_liczba)+" ilość: "+str(ilosc_powtorzen_max))
plik.close()
wyniki.close()
#ZADANIE 3.3
def ile_liczb_3(c):
    moje_liczby = []
    idx_konczacy = 0
    for i in range (0,len(c)):
        if i >= idx_konczacy:
            if i == 0:
                if c[i] == '5':
                    podciag = c[i + 1:]
                    liczba = '5'
                    idx_konczacy = i + 1
                    for j in range(0, len(podciag)):
                        try:
                            int(podciag[j])
                            idx_konczacy += 1
                            liczba = liczba + podciag[j]
                        except:
                            moje_liczby.append(liczba)
                            break
            elif c[i-1].isdigit() == False:
                if c[i] == '5':
                    podciag = c[i + 1:]
                    liczba = '5'
                    idx_konczacy = i + 2
                    for j in range(0, len(podciag)):
                        try:
                            int(podciag[j])
                            idx_konczacy += 1
                            liczba = liczba + podciag[j]
                        except:
                            if len(liczba) == 9:
                                moje_liczby.append(liczba)
                            break
    return moje_liczby

plik = open("dane.txt","r")
ilosc = []
for line in plik:
    for licz in ile_liczb_3(line):
        ilosc.append(licz)
plik.close()
wyniki = open("wyniki3_3.txt", "w")
wyniki.write("zadanie 3.3: " + str(ilosc))
plik.close()
wyniki.close()

#ZADANIE 3.4
def ile_liczb_4(c):
    moje_liczby = []
    idx_konczacy = 0
    for i in range (0,len(c)):
        if i >= idx_konczacy:
            if i == 0:
                if c[i].isdigit():
                    podciag = c[i + 1:]
                    liczba = c[i]
                    idx_konczacy = i + 1
                    for j in range(0, len(podciag)):
                        try:
                            int(podciag[j])
                            idx_konczacy += 1
                            liczba = liczba + podciag[j]
                        except:
                            moje_liczby.append(liczba)
                            break
            elif c[i-1].isdigit() == False:
                if c[i].isdigit():
                    podciag = c[i + 1:]
                    liczba = c[i]
                    idx_konczacy = i + 1
                    for j in range(0, len(podciag)):
                        try:
                            int(podciag[j])
                            idx_konczacy += 1
                            liczba = liczba + podciag[j]
                        except:
                            if len(liczba) == 9:
                                moje_liczby.append(liczba)
                            break
    return moje_liczby
def zlicz_ilosc_cyfr(tab):
    liczba_ilosc = {}
    for liczba in tab:
        poj_liczba_ilosc = {}
        for poj in liczba:
            if poj in poj_liczba_ilosc:
                poj_liczba_ilosc[poj] += 1
            else:
                poj_liczba_ilosc[poj] = 1
        liczba_ilosc[liczba] = len(poj_liczba_ilosc)
    a = 0
    powtorzenie = 0
    pow_liczba = []
    for war in liczba_ilosc:
        if a == 0:
            powtorzenie = liczba_ilosc[war]
            pow_liczba.append(war)
        else:
            if powtorzenie > liczba_ilosc[war]:
                powtorzenie = liczba_ilosc[war]
                pow_liczba = []
                pow_liczba.append(war)
            elif powtorzenie == liczba_ilosc[war]:
                powtorzenie = liczba_ilosc[war]
                pow_liczba.append(war)
        a += 1
    return pow_liczba


plik = open("dane.txt","r")
ilosc = []
for line in plik:
    for licz in ile_liczb_4(line):
        ilosc.append(licz)
najmn_ilosci_r_cyfr = zlicz_ilosc_cyfr(ilosc)
plik.close()
wyniki = open("wyniki3_4.txt", "w")
wyniki.write("zadanie 3.4: " + str(najmn_ilosci_r_cyfr))
plik.close()
wyniki.close()
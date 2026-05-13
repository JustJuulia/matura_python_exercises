''' ZADANIE 4.1
f = open("liczby.txt", "r")
liczby = f.readline()
pierwsza_linia = liczby.split(' ')
for i in range(len(pierwsza_linia)):
    pierwsza_linia[i] = int(pierwsza_linia[i])
do_podz = f.readline()
druga_linia = do_podz.split(' ')
for i in range(len(druga_linia)):
    druga_linia[i] = int(druga_linia[i])
counter = 0
for i in range(len(pierwsza_linia)):
    for j in range(len(druga_linia)):
        if druga_linia[j] % pierwsza_linia[i] == 0:
            counter += 1
            break
        else:
            continue
f.close()
print(counter)
'''

''' ZADANIE 4.2
f = open("liczby.txt", "r")
liczby = f.readline()
pierwsza_linia = liczby.split(' ')
for i in range(len(pierwsza_linia)):
    pierwsza_linia[i] = int(pierwsza_linia[i])
pierwsza_linia.sort(reverse = True)
print(pierwsza_linia[100])
f.close()
'''

'''  ZADANIE 4.3 
f = open("liczby.txt", "r")
def dzielniki_fun(cyfra):
    dzielniki = {}
    if cyfra == 1:
        dzielniki.update({1 : 1})
    else:
        i = 0
        while cyfra > 1:
            if i > 1:
                while cyfra%i==0:
                    ilosc = 0
                    try:
                        ilosc = dzielniki[i]
                        dzielniki.update({i: ilosc + 1})
                        cyfra = cyfra / i
                    except Exception:
                        dzielniki.update({i: ilosc + 1})
                        cyfra = cyfra / i
            i+=1
    return dzielniki
def sprawdzenie_dziel_zp(druga_linia, pier_linia):
    checker = 0
    for klucz, wart in druga_linia.items():
        try:
            if pier_linia[klucz] >= wart:
                continue
            else:
                checker = -1
                break
        except Exception:
            checker = -1
            break
    return checker
liczby = f.readline()
pierwsza_linia = liczby.split(' ')
for i in range(len(pierwsza_linia)):
    pierwsza_linia[i] = int(pierwsza_linia[i])
liczby = f.readline()
druga_linia = liczby.split(' ')
for i in range(len(druga_linia)):
    druga_linia[i] = int(druga_linia[i])
ilosc_cyfr_z_pierw = {}
for i in range(len(pierwsza_linia)):
        ilosc = 0
        try:
            ilosc = ilosc_cyfr_z_pierw[pierwsza_linia[i]]
        except Exception:
            ilosc = 0
        ilosc_cyfr_z_pierw.update({pierwsza_linia[i] : ilosc+1})
koncowe_liczby = []
for i in range(len(druga_linia)):
    ilosc_dzielnych = dzielniki_fun(druga_linia[i])
    sprawdzacz = sprawdzenie_dziel_zp(ilosc_dzielnych, ilosc_cyfr_z_pierw)
    if sprawdzacz == 0:
        koncowe_liczby.append(druga_linia[i])
print(koncowe_liczby)
f.close()
'''

# zadanie 4.4
f = open("liczby.txt", "r")
liczby = f.readline()
pierwsza_linia = liczby.split(' ')
for i in range(len(pierwsza_linia)):
    pierwsza_linia[i] = int(pierwsza_linia[i])
najw_srd = 0
ilosc_znakow = 0
licz = 0

for i in range(len(pierwsza_linia)):
    czyciag_git = True
    ilosc_elementow = 0
    suma = 0
    j = 0
    sublinia = pierwsza_linia[i:]
    for a in range(len(sublinia)):
        ilosc_elementow += 1
        suma = (suma + pierwsza_linia[i+j])
        if ilosc_elementow >= 50:
            if suma/ilosc_elementow > najw_srd:
                najw_srd = suma/ilosc_elementow
                ilosc_znakow = ilosc_elementow
                licz = pierwsza_linia[i]
        j += 1

print("najwieksza srednia: ",najw_srd," ilosc znaków: ", ilosc_znakow," zaczyna sie od liczby: ", licz)
f.close()
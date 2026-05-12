'''
góra dół n lewo prawo m
a[i][j] = 0 gdy pole jest czarne, pola w lewym górnym i prawym dolnym rogu są zawsze białe, A[1][1] = 1 = A[n][m]
'''
n = 5
m = 5
A = [[0],[0],[0],[0],[0],[0]]
P = [[True],[True],[True],[True],[True],[True]]
for a in range(1, n+1):
    for b in range(1,m+1):
        do_wlozenia= int(input(f"Podaj wartosc dla pola o wymiarach {a,b}: "))
        A[a].append(do_wlozenia)
for a in range(1, n+1):
    for b in range(1,m+1):
        P[a].append(True)
for i in range(1, n+1):
    for j in range(1, m+1):
        if A[i][j] == 0:
            P[i][j] = False
        else:
            if i == 1 and j != 1:
                P[i][j] = P[i][j - 1]
            if i != 1 and j == 1:
                P[i][j] = P[i - 1][j]
            if i!= 1 and j != 1:
               P[i][j] = P[i][j-1] or P[i - 1][j]
print(P[n][m])


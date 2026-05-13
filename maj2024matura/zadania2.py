n = 333333666666999999
b = 1
c = 0
counter = 0
while n > 0:
    a = n % 10
    n = n//10
    if a % 2 == 0:
        c = c+b * a//2
    else:
        c = c+b
        counter = counter +1
    b = b * 10
print(c)
print("counter: ",counter)
n =  0
while (n != -1):
    nfactors = 0
    n = int(input("Enter a number or -1 to exit: "))
    for i in range(1, n+1):
        if n % i  == 0:
            nfactors = nfactors + 1
            if i != 1 and i != n:
                print(i, 'is a factor')
    if nfactors == 2:
        print(n, 'is a prime number')
    else:
        print(n, 'is not a prime number')



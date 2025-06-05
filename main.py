n = 7
m = 435
CLOSED_KEY = [1, 3, 5, 12, 25, 52, 115, 220]

def CreateOpenKey(closed_key, n, m):
    open_key = []
    for el in closed_key:
        open_key.append(el*n%m)
    return open_key

def FindN1(n, m):
    n1 = 1
    success = False
    while success is False:
        if (n*n1)%m == 1:
            success = True
        else:
            n1+=1
    return n1

OPEN_KEY = CreateOpenKey(CLOSED_KEY, n, m)
print(OPEN_KEY)
n1 = FindN1(n, m)
print(n1)

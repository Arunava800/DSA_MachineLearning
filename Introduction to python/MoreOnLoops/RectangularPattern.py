n = int(input())

for i in range(1, 2*n):
    if i <= n:
        iLim = i
    else:
        iLim = 2*n-i
    for j in range(1, iLim+1):
        print(n - min(j, iLim)+1, end="")
    for j in range(iLim+1, n+1):
        print(n-iLim+1, end="")
    for j in range(iLim+1, n+1):
        print(n-iLim+1, end="")
    for j in range(iLim-1, 0, -1):
        print(n-min(j, iLim)+1, end="")
    print()


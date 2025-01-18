n = int(input())
rows = 1
count = 0
while rows <= n:
    p_end = n * rows
    p_start = p_end - (n-1)
    cols = 1
    while cols <= n:
        print(p_start, end=" ")
        p_start += 1
        cols += 1
    print()
    rows += 2
    count += 1

r_rows = n - count
if n % 2 == 0:
    i_value = n
else:
    i_value = n-1
while r_rows > 0:
    cols = 1
    p_end = n * i_value
    p_start = p_end - (n-1)
    while cols <= n:
        print(p_start, end=" ")
        p_start += 1
        cols += 1
    print()
    r_rows -= 1
    i_value -= 2

def fibanocci(n):
    if n == 0:
        return n
    elif n == 1:
        return n
    else:
        return fibanocci(n-1) + fibanocci(n-2)
    
for i in range(10):  # range(10) → 0 to 9
    print(fibanocci(i), end=" ")



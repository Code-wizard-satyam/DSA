# Fibonicci

def fibonicci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    last = fibonicci(n-1)
    second_last = fibonicci(n-2)

    ans = last + second_last
    return ans

a = fibonicci(10)
print(a)
# sum of digit of a number

def sumOFdigit(n):
    if n//10 == 0:
        return n
    
    return sumOFdigit(n//10) + n % 10

print(sumOFdigit(555))


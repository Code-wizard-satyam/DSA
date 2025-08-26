# Head Recursion
def factHead(n):
    if n == 0:
        return 1
    smallAnswer = factHead(n - 1)
    finalAnswer = n * smallAnswer
    return finalAnswer

print("Head Recursion:", factHead(5))


# Wrong Tail Recursion
def factTailWrong(n):
    if n == 0:
        return 1
    return n * factTailWrong(n - 1) 


# Correct Tail Recursion
def factTail(n, accumulator=1):
    if n == 0:
        return accumulator
    return factTail(n - 1, accumulator * n)

print("Tail Recursion:", factTail(5))
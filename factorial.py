# Python program to find the factorial of a number
# using "recursion" and "for loop"

def fact(n):
    if n == 0:
        return 1
    elif n < 0:
        return f'Sorry, factorial does not exist for negative numbers'
    return n*fact(n-1)


def factorial(n):
    factori = 1
    if n == 0:
        return 1
    elif n < 0:
        return f'Sorry, factorial does not exist for negative numbers'
    for i in range (1, n+1):
        factori = factori*i
    return factori


n = int(input('Enter a number: '))
print(f'Using recursion: {fact(n)}')
print(f'Using for loop: {factorial(n)}')
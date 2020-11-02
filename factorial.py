# Python program to find the factorial of a number
# using "recursion" and "for loop"

def recursive_factorial(n):
    if n == 0:
        return 1
    return n*recursive_factorial(n-1)


def loop_factorial(n):
    fact = 1
    if n == 0:
        return 1
    for i in range (1, n+1):
        fact = fact*i
    return fact

def run():
    n = int(input('Enter a number: '))
    if n < 0:
        print('Sorry, factorial does not exist for negative numbers')
    else: 
        print(f'Using recursion: {recursive_factorial(n)}')
        print(f'Using for loop: {loop_factorial(n)}')

if __name__ == "__main__":
    run()

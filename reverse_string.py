# Reverse string using recursion, for loop and slicing

def recursion_reverse(str): 
    if len(str) == 0: 
        return str
    else: 
        return recursion_reverse(str[1:]) + str[0]

def loop_reverse(str):
    s = ""
    for i in str:
        s = i + s
    return s

def slicing_reverse(str):
    return str[ : : -1]

def run():
    str = input('Enter a word: ')
    print(f'Reverse string using recursion: {recursion_reverse(str)}')
    print(f'Reverse string using for loop: {loop_reverse(str)}')
    print(f'Reverse string using slicing: {slicing_reverse(str)}')

if __name__ == "__main__":
    run()
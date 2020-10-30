# Bubble Sort algorithm in Python
# From highest to lowest

def bubble_sort(list, n):
    for i in range(n-1):
        for j in range(0, n-i-1):
            if list[j] < list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                print(f"Round {i}: {list}")
    
    
def run():
    list = [60, 30, 20, 10, 50, 1, 90] 
    n = len(list)
    bubble_sort(list, n)
    print(list)


if __name__ == "__main__":
    run()
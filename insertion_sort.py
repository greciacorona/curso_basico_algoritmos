# Insertion sort algorithm in Python
# From lowest to highest

def insertion_sort(list, n):

    for i in range(1, len(list)):
        current_value = list[i]
        j = i
        while j > 0 and list[j - 1] > current_value:
            list[j] = list[j -1]
            j = j - 1
        list[j] = current_value
        print(f"Round {i}: {list}")

def run():
    list = [60, 30, 20, 10, 50, 1, 90] 
    print(list)
    n = len(list)
    insertion_sort(list, n)
    print(list)

if __name__ == "__main__":
    run()
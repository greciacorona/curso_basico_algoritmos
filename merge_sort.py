# Merge sort algorithm in Python

def mergeSort(alist):

    print("Splitting ", alist)

    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        #recursion
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = j = k = 0
        
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k +=1
        # print("while1", alist)

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1
        # print("while2 ", alist)

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1
        # print("while3 ", alist)

    print("Merging ", alist)

if __name__ == "__main__":
    # alist = [2,1]
    # alist = [3, 94, 86, 82, 90, 10, 87, 36, 61, 8, 17, 15, 
    #     22, 10, 23, 78, 25, 2, 30, 45, 98, 43, 98, 59, 53, 57, 
    #     2, 64, 1, 41, 32, 58, 19, 99, 60, 74, 48, 80, 44, 25, 
    #     68, 1, 89, 77, 60, 25, 99, 30, 76, 32, 57, 82, 52, 44, 
    #     72, 87, 34, 87, 65, 30, 54, 6, 31, 33, 44, 44, 42, 82, 
    #     90, 17, 9, 98, 28, 86, 69, 3, 17, 8, 45, 98, 12, 47, 95, 
    #     43, 72, 39, 41, 82, 74, 56, 65, 79, 50, 26, 67, 100, 24, 
    #     67, 38, 57]
    mergeSort(alist)
    print(alist)

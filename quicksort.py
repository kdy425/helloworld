import random
array = [i for i in range(50)]
random.shuffle(array)
def quickSort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[len(array) // 2]
        left = []
        right = []
        equal = []
        for i in array:
            if i < pivot:
                left.append(i)
            elif i > pivot:
                right.append(i)
            else:
                equal.append(i)
    return quickSort(left)+ equal + quickSort(right)

print(quickSort(array))
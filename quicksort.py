import random
array = [i for i in range(50)]
random.shuffle(array)
def quickSort(array):
    if len(array) <= 1:
        return array
    else:
        #pivot = array[len(array) // 2]
        pivot = array.pop()
        left = []
        right = []
        for i in array:
            if i < pivot:
                left.append(i)
            else:
                right.append(i)
    return quickSort(left)+ [pivot] + quickSort(right)
print(quickSort(array))

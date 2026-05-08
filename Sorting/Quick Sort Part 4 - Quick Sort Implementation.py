a = [10, 50, 40, 20, 15, 16, 2, 3, 8, 9, 99, 34, 43, 100, 121, 104, 132]

def quickSort(left, right):
    if (left < right):
        partitionPoint = partition(left, right)
        quickSort(left, partitionPoint - 1)
        quickSort(partitionPoint + 1, right)

def partition(start, end):
    left = start - 1
    pivot = a[end]
    for i in range(start, end):
        if (a[i] <= pivot):
            left += 1
            a[left], a[i] = a[i], a[left]
    
    left += 1
    a[end], a[left] = a[left], a[end]
    
    return left

print("Before sorting " + str(a))
quickSort(0, len(a) - 1)
print("After sorting " + str(a))

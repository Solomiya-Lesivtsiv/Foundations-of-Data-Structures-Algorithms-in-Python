li = [15, 25, 20, 50, 45, 10, 40]

print("Before sorting " + str(li))
n = len(li)

for i in range(n):
    smallIndex = i
    for j in range(i, n):
        if (li[j] < li[smallIndex]):
            smallIndex = j

    print("Putting " + str(li[smallIndex]) + " at index " + str(i))
    li[i], li[smallIndex] = li[smallIndex], li[i]
print("After sorting " + str(li))
# N + N - 1 + N - 2 + N - 3 + .... 1
# Total = O(N^2)

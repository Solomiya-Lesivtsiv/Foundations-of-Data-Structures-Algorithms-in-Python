a = [1, 5, 2, 6, 0, 4, 3]

n = len(a)
print("Before partitioning " + str(a))
key = a[n-1]
left = -1

for i in range(n-1):
    if (a[i] <= key):
        left += 1
        a[i], a[left] = a[left], a[i]

left += 1
a[n-1], a[left] = a[left], a[n-1]

print("After partitioning " + str(a))

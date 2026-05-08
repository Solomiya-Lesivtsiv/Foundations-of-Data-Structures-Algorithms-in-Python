li = [10, 25, 20, 50, 45, 15, 40]

print("Before Sorting " + str(li))
n = len(li)

for i in range(n):
    for j in range(n - i - 1):
        if li[j] > li[j + 1]:
            li[j], li[j + 1] = li[j + 1], li[j]

print("After Sorting " + str(li))

# O(N*(N - i)) = O(N^2)

# N + N - 1 + N - 2 + N - 3 + ... 1 = ~ O(N^2)
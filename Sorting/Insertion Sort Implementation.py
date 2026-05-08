li = [15, 25, 20, 50, 45, 10, 40]

print("Before full sorting " + str(li))
n = len(li)

for i in range(1, n):
    j = i - 1
    key = li[i]
    while (j >= 0 and li[j] > key):
        li[j + 1] = li[j]
        j -= 1

    li[j + 1] = key
    print(li[:i + 1])

print("After full sorting " + str(li))

# Worst Case : 1 + 2 + 3 +. ... N = N(N+1)/2 = O(N^2)
# Best Case: 1 + 1 + 1 + 1 + ... 1 (N times) = O(N)

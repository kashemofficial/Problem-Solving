n = int(input())
arr = [int(x) for x in input().split()]
odd_number = sum(x&1 for x in arr)
for i,j in enumerate(arr):
    if (odd_number != 1 and ~j & 1) or (odd_number == 1 and j & 1):
        print(i+1)




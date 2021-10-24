for _ in range(int(input())):
    a = int(input())
    nums = list(map(int, input().split()))
    d = {}
    m = float("inf")
    for i in nums:
        m = min(i, m)
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    print(len(nums) - d[m])

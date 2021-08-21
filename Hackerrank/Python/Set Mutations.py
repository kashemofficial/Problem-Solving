a = int(input())
_set1 = set(map(int,input().split()))
N = int(input())
for _ in range(N):
    a1,a2 = input().split()
    _set2 = set(map(int,input().split()))
    if (a1 == 'intersection_update'):
        _set1.intersection_update(_set2)
    elif (a1 == 'update'):
        _set1.update(_set2)
    elif (a1 == 'symmetric_difference_update'):
        _set1.symmetric_difference_update(_set2)
    elif (a1 == 'difference_update'):
        _set1.difference_update(_set2)
print(sum(_set1))
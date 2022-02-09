class Solution:
    def sortEvenOdd(self, arr: List[int]) -> List[int]:
        arr[::2],arr[1::2] = sorted(arr[::2]),sorted(arr[1::2])[::-1]
        return arr

'''arr = list(map(int,input().split()))
arr[::2],arr[1::2] = sorted(arr[::2]),sorted(arr[1::2])[::-1]
print(arr)'''


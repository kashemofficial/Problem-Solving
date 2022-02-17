class Solution:
    def intersect(self, a: List[int], b: List[int]) -> List[int]:
        l = []
        if len(a) > len(b):
            for i in b:
                if i in a:
                    a.remove(i)
                    l.append(i)
        else:
            for i in a:
                if i in b:
                    b.remove(i)
                    l.append(i)
        return l


'''a = list(map(int,input().split()))
b = list(map(int,input().split()))
l = []
if len(a) > len(b):
    for i in b:
        if i in a:
            a.remove(i)
            l.append(i)
else:
    for i in a:
        if i in b:
            b.remove(i)
            l.append(i)
print(l)'''












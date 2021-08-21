N,X = map(int,input().split())
li = []
for i in range(X):
    li.append(map(float,input().split()))
for a in zip(*li):
    print(sum(a)/len(a))


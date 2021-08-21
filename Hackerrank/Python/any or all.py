N = int(input())
li = input().split(" ")
print(all(int(i)>=0 for i in li) and any(i == i[::-1]for i in li))



li = list(map(int,input().split(' ')))
x = sum(li) # list sum kora 1 2 3 4 5 = 15
_max = x - (max(li)) # x = 15 - 5 = 10 ...max diya list a boro sonka nawa
_min = x - (min(li))# x = 15 - 1 = 14 .. min diya list a coto sonka nawa
print(_max,_min)
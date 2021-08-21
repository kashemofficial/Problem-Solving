class big_Sorting:
    def __init__(self,unsorted):
        self.unsorted = unsorted
        for i in sorted(unsorted,key=int):
            print(i)
if __name__ == '__main__':
    n = int(input())
    un_sorted = []
    for _ in range(n):
        unsorted_item = input()
        un_sorted.append(unsorted_item)
    big_Sorting(un_sorted)

'''
t = int(input())
li = []
for i in range(t):
    li.append(input())
li.sort(key= int)
#print(*li,sep='\n')
for __ in li:
    print(__)'''
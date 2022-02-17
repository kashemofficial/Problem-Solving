class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ara = list()
        for i in range(len(grid)):
            ara.extend(grid[i])
            c = 0
            for j in ara:
                if j<0:
                    c+=1
        return c


'''ara = list()
for i in range(len(grid)):
    ara.extend(grid[i])
    c = 0
    for j in ara:
        if j<0:
            c+=1
print(c)'''









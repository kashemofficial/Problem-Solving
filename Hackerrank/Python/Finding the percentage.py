n = int(input())
student_marks = {}
for _ in range(n):
    name,*li = input().split()
    score = list(map(float,li))
    student_marks[name] = score
query_name = input()
a,b,c = student_marks[query_name]
print('%.2f'%((a+b+c)/3))
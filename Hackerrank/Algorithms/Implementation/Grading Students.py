def solve(grade):
    if grade >= 38:
        if grade % 5 == 3:
            grade += 2
        elif grade % 5 == 4:
            grade += 1
    print(grade)
if __name__ == '__main__':
    for _ in range(int(input())):
        grade = int(input())
        solve(grade)
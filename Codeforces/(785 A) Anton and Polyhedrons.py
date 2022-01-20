res = 0
n = int(input())
for i in range(n):
    s = input()
    if s == "Tetrahedron":
        res += 4
    elif s == "Cube":
        res += 6
    elif s == "Octahedron":
        res += 8
    elif s == "Dodecahedron":
        res += 12
    elif s == "Icosahedron":
        res += 20
if __name__ == '__main__':
    print(res)

def merge_the_tools(string, k):
    n = len(string)
    for i in range(0, n, k):
        slicedStr = string[i: i+k]
        li = []
        for j in slicedStr:
            if j not in li:
                li.append(j)
        print(''.join(li))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
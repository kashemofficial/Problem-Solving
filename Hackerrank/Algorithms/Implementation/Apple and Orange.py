def apples_orange(s,t,a,b,apples,orange):
    print(sum([1 for x in apples if (x+a)>=s and (x+a) <= t]))
    print(sum([1 for x in orange if (x+b)>=s and (x+b) <= t]))
if __name__ == '__main__':
    first_input = input().rstrip().split()
    s = int(first_input[0])
    t = int(first_input[1])
    second_input = input().rstrip().split()
    a = int(second_input[0])
    b = int(second_input[1])
    third_input = input().rstrip().split()
    m = int(third_input[0])
    n = int(third_input[1])
    apples = list(map(int,input().rstrip().split()))
    orange = list(map(int,input().rstrip().split()))
    apples_orange(s,t,a,b,apples,orange)
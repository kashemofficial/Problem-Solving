t = int(input())
x,y,z = map(int,input().split())
if ((t-x>=10) or (t-y>=10) or (t-z>=10)):
    print('Yes :-D')
else:
    print('No :-(')
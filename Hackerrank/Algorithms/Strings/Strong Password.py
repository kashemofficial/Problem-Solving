def Strong_Password(num,st):
    __digit=0
    __lower=0
    __upper=0
    __spec=0
    count=0
    spec="!@#$%^&*()-+"
    for c in st:
        if c.isupper():
            __upper=__upper+1
        elif c.islower():
            __lower=__lower+1
        elif c.isdigit():
            __digit = __digit+1
        elif c in spec:
            __spec=__spec+1
    if ( __upper==0 ):
        count=count+1
    if ( __lower==0 ):
        count=count+1
    if ( __digit==0 ):
        count=count+1
    if ( __spec==0 ):
        count=count+1
    if((__upper+__lower+__spec+__digit+count) < 6 ):
        count=count+(6-(__upper+__lower+__spec+__digit+count))
    print(count)

if __name__ == '__main__':
    num = int(input())
    st = input()
    Strong_Password(num,st)
    
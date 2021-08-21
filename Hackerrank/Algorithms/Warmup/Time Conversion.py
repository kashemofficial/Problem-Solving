from time import strftime,strptime
s = strftime("%H:%M:%S",strptime(input(),"%I:%M:%S%p"))
print(s)

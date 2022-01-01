from datetime import datetime
n = str(input())
dt = datetime.strptime(n,"%I:%M:%S%p")
print(dt.strftime("%H:%M:%S"))


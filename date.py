import datetime

data = datetime.date(*map(int, input().split()))
day = datetime.timedelta(days=int(input()))
print((data + day).strftime('%Y %#m %#d'))

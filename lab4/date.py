from datetime import datetime, timedelta
today = datetime.now()

# 1st task

day5_ago = today - timedelta(5)
print('5 days ago was ' + day5_ago.strftime('%B %d' + ' of ' + '%Y'))

#2nd task 

yesterday = today - timedelta(1)
tomorrow = today + timedelta(1)

print('Yesterday: ' + yesterday.strftime('%d %B, %Y'))
print('Today: ' + today.strftime('%d %B, %Y'))
print('Tomorrow: ' + tomorrow.strftime('%d %B, %Y'))

# 3rd task

print(today)

dropmicrosec = today.replace(microsecond= 0)
print(dropmicrosec)

# 4th task

date1inp = input('Date 1. YYYY-MM-DD HH:MM:SS : ')
date2inp = input('Date 2. YYYY-MM-DD HH:MM:SS : ')
date1 = datetime.strptime(date1inp, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date2inp, "%Y-%m-%d %H:%M:%S")

timedif = date2 - date1

seconds = timedif.total_seconds()
print(seconds, ' seconds')
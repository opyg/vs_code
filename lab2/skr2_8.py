

from datetime import datetime

str_date1 = '2022-10-11'
str_date2 = '2023-6-15'
day1 = datetime.strptime(str_date1, "%Y-%m-%d")
day2 = datetime.strptime(str_date2, "%Y-%m-%d")
diff = day2 - day1
print('Roznica to',diff.days,' dni')
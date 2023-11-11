
from datetime import datetime
import calendar as cal
y , m = input("Podaj rok i miesiac: ").split()

print(f'{y} {m}')
print(cal.month(int(y),int(m)))

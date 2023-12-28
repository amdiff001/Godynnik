import datetime
import sys

print("Вітаю! Поточний час:")
print(datetime.datetime.now().strftime("%H:%M:%S"))

while False:
  pass
  
input("Натисніть Enter для виходу")  
sys.exit()

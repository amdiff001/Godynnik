import time
import datetime
import sys

while True:

  current_time = datetime.datetime.now().strftime("%H:%M:%S")
  
  print(f'Зараз {current_time}')

  time.sleep(1)

  if datetime.datetime.now().minute == 0:
    sys.exit()

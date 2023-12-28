import datetime

def get_current_time():
  print("Вітаю! Поточний час:") 
  print(datetime.datetime.now().strftime("%H:%M:%S"))

get_current_time()

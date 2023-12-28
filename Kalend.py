import datetime

print('Вітаю! '
      'Поточний час:')

while True:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f'Зараз {current_time}')

    user_input = input("Щоб вийти, введіть 'вихід': ")
    if user_input.lower() == 'вихід':
        break

print('До побачення!')


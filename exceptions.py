print("*"*100)

try:
    1/0
except ZeroDivisionError as er:
    print(f"{er}")
except Exception as ex:
    print(f"{ex}")
else:
    print('Сработает только в случае ошибок в блоке "try"')
finally:
    print("finally сработает всегда")


print("*"*100)

try:
    int('asdf')
except ValueError as ve:
    print(f"{ve}")
    raise
else:
    print('Сработает только в случае ошибок в блоке "try"')
finally:
    print("finally сработает всегда")


print("*"*100)

try:
    int('asdf')
except ValueError as ve:
    print(f"{ve}")
    raise TypeError("ошибка") from None  # выбросит только одно исключение (последнее)
else:
    print('Сработает только в случае ошибок в блоке "try"')
finally:
    print("finally сработает всегда")

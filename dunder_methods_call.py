from time import perf_counter


class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = perf_counter()
        print(f"Вызывается функция {self.func.__name__}")
        result = self.func(*args, **kwargs)
        finish = perf_counter()
        print(f"Функция отработала за {finish - start, 4}")
        return result


def fib(n: int) -> int:
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


def fact(n: int) -> int:
    pr = 1
    for i in range(pr, n+1):
        pr *= i
    return pr


fact = Timer(fact)
print(fact(7))

Timer(fib)(7)
print(fib(10))

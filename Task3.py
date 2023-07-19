class FibonacciError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

try:

    fibonacci = fibonacci_generator()
    
    for _ in range(10):
        print(next(fibonacci))
except FibonacciError as e:
    print("Ошибка в генераторе чисел Фибоначчи:", e.message)
# Generators & Iterators

def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
        
# Example usage:
for num in fibonacci_generator(10):
    print(num)

# prime iterator class
class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.current = 2

    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.current <= self.n:
            num = self.current
            self.current += 1
            if self.is_prime(num):
                return num
        raise StopIteration
    
    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
# Example usage:
for prime in PrimeIterator(30):
    print(prime)
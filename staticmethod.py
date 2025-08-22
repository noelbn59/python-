class Math:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y
    
    @staticmethod
    def multiply(x, y):
        return x * y
    
    @staticmethod
    def square(x):
        return x * x
    
print(Math.add(5, 3))
print(Math.subtract(10, 4))
print(Math.multiply(2, 6))
print(Math.square(4))
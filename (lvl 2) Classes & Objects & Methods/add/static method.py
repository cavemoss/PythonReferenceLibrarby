class Math:

    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def sub(a, b):
        return a - b
    
    @staticmethod
    def mult(a, b):
        return a * b
    
    @staticmethod
    def div(a, b):
        return int(a / b)
        
    @staticmethod
    def say_it():
        print('math is cool')


Math.say_it()
print(Math.add(3,2))
print(Math.sub(4,3))
print(Math.mult(3,3))
print(Math.div(8,2))

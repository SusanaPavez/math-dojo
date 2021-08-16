class MathDojo:
    
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        for x in nums:
            self.result += x
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for x in nums:
                self.result -= x
        return self 

# crear una instruccion:
md = MathDojo()
# para probar:
x = md.add(2).add(16,18,20).subtract(3,2).result
x = md.add(2).add(7,9,11).result
x = md.add(2).add(2,4,6).result
x = md.add(2).add(22,24,26).result
x = md.add(2).subtract(2,6,2).result
x = md.add(2).subtract(8,10,12).result
x = md.add(2).subtract(1,3,5).result
print(x)	
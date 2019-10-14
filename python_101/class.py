class Calculator:
    def __init__(self, num1, num2 ):
      self.num1 = num1
      self.num2 = num2

    def add(self):
        print (self.num1 + self.num2)

    def subtract(self):
        print (n1 - n2)

    def divide(self):
        print (n1/n2)

    def multiply(self):
        print (n1 * n2)


cal = Calculator(1,2)

cal.add()
setattr(cal, 'num1', 8)
cal.add()


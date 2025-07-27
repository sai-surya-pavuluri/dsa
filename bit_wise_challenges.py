### Even or Odd number

def isEven(num):
    return (num&1) == 0

### Swap two numbers
def swap(a,b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
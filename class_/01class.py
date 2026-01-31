class calculator:
       def __init__(self,n):
              self.n=n
       def square(self):
              print(f"The square of number={self.n*self.n}")
       def cube(self):
              print(f"The cube of number={self.n*self.n*self.n}")
       def square_root(self):
              print(f"The square root of the number={self.n**(1/2)}")
try:
       userint=int(input(">>>"))
except ValueError:
       print("Invalid Input!!")
a=calculator(userint)
a.square()
a.cube()
a.square_root()
       


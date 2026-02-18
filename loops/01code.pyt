'''Write a program to input n numbers and find the sum of all even & odd
numbers separately.'''
while True:
     try:
          sun=0
          su=0
          ra=int(input("Enter range:"))
          for i in range(ra):
               if i%2==0:
                    sun+=i
               else:
                    su+=i
          print(f"The sum of even numbers in Range {ra} is {sun}")  
          print(f"The sum of odd numbers in Range {ra} is {su}")  
     
     except ValueError:
          print("Ivalid Input !!!")
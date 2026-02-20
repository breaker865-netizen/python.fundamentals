#Take a number n and calculate its factorial using a loop.
while True:
     irt=input("Enter your choice:").lower()
     if irt=='check':
          try:
               n=int(input("Enter a number:"))
               factorial=1
               for i in range(1,n+1):
                    if n==1 or n==0:
                         print(1)
                    elif n<0:
                         print("factoial is not defined for negative numbers")
                    else:
                         factorial*=i # main 

               print(f"the factorial of the number:{factorial}")        

          except ValueError:
               print("Invalid input!!!")
     else:
          print("_________")
          break
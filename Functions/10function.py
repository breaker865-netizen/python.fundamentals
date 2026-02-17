print("1. To print the table of the number")
print("2. To print the factors of a number")
print("3. To print the factorial of the number")
er=int(input("Enter you choice btw [1,2,3]=$"))
if er>3 or er<0:
     print("$invalid")
else:
     if er==1:
          n=int(input("$number:"))
          for i in range(1,10+1):
               print(f"{n} X {i} = {n*i}")
     elif er==2:
          n1=int(input("$"))
          for i in range(1,n1+1):
              if n1%i==0:
                   print(i,end=" ")
     elif er==3:
          def factorial(n3):
               if n3==1 or n3==0:
                    return 1
               else:
                    return n3*factorial(n3-1)
          n3=int(input("$"))
          print(f"The factorial of the number is $ {factorial(n3)}")
     else:
          print("$Invalid!!")


#Find the sum of digits of a number.
while True:
     irt=input("Enter your choice:").lower()
     if irt=='check':
          try:
               num=int(input("Enter a number:"))
               su=0
               while num>0:
                    rem=num%10
                    su+=rem
                    num=num//10
               print(f"The sum of digits:{su}")
          except ValueError:
               print("Invalid Input!")
     else:
          print("------")
          break

                    
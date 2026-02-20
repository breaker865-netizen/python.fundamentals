#Reverse a number using a while loop.
while True:
     irt=input("Enter your choice:").lower()
     if irt=='check':
          try:
               num=int(input("Enter a number:"))
               reverse=0
               while num>0:
                digit = num % 10
                reverse = reverse * 10 + digit
                num = num // 10
               print(reverse)
          except ValueError:
              print("Invalid!!")
     else:
          print("-------")
          break

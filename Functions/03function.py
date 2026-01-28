def find_sum_number():
       try:
              n=int(input("Enter limit:"))
              sum=0
              for i in range(n):
                     i=int(input("Enter number:"))
                     sum+=i
              print(sum)
       except ValueError:
              print("Invalid Input!!")
find_sum_number()
       
       
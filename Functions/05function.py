# Function 
#Print the table of the given number
def table_number():
       while True:
              try:
                     n=int(input("Enter the number:"))
                    
                     for i in range(1,11):
                            print(f"{n} x {i}={i*n}")
              except ValueError:
                     print("Invalid input")
table_number()
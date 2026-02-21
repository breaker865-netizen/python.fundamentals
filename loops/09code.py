# Print all numbers between 1 and 500 that are not divisible by 2 and not divisible by 3.
r=500
list1=[]
list2=[]
for i in range(1,r+1):
       if i%2!=0 and i%3!=0:
              print(f"The number not divisible by 2 and 3 = {i}")
              print()
              list1.append(i)
       elif i%2==0:
              print(f"The number divisible by 2 = {i}")
              print()
              list2.append(i)
print(f"  List of All numbers between 1 and 500 that are not divisible by 2 and 3::{list1} ")
print()
print(f" List of All numbers divisible by 2::{list2}")




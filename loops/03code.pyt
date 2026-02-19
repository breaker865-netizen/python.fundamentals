# Print Fibonacci series
a=0
b=1
n=int(input("Enter the limit: "))
if(n==1):
 print(a)
elif(n==2):
 print(a, " ",b)
elif(n>2):
  print(a, " ",b, end=" ")
  for i in range(1,n-1):
    c=a+b
print(c, end=" ")
a=b
b=c
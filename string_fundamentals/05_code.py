# This code input all three angle of triangle
'''Sum of all angles in a triangle = 180° 
a,b,c as all angles
sum of a,b,c=180°,means triangle exists '''
while True:
     print("Check the tringle \nType check to process\nType any key to terminate")
     irt=input("Enter your choice:").lower()
     if irt=='check':
          try:
               a=float(input("Enter First angle:"))
               b=float(input("Enter second  angle:"))
               c=float(input("Enter third angle:"))
               if a<=0 or b<=0 or c<=0:
                    print("Invalid$")
               else:
                    sum_of_angle=a+b+c
                    if (sum_of_angle-180.00)< 0.0001:
                         print("--The Triangle exists--")
                         print()
                    else:
                         print("---The Triangle cannot exists---")
                         print()
          except ValueError:
                    print("---Input valid things" \
                    "please !!!!!")
     else:
          print("---Trminated---")
          print()
          break

               

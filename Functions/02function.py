# This is a basic python function that convert °C to °F
def temprature():
       try:
              c=float(input("Enter temprature in °C:"))
              far=c*(9/5)+32   #(°C × 9⁄5) + 32 
              print(f"{far:.2f}","°F"," is equal to ",c,"°C")
       except ValueError:
              print("Invalid Input!!!")
temprature()


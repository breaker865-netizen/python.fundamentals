d={}
for i in range(5):
    name=input("Enter the name:")
    salary=float(input("Enter the salary:"))
    alo=float(input("Enter allowance:"))
    deduction=float(input("Enter Deduction:"))
    d[name]=[salary,alo,deduction]
cho=0
while True:
    print('''
          1.Display the total salary
          2.Display the total allowance and deduction
          3.Search an employee
          4.Exit''')
    cho=int(input("Enter your choice:"))
    if cho==1:
        for Key,value in d.items():
            gross=value[0]+value[1]
            net=gross-value[2]
            print(Key,gross,net)
    elif cho==2:
        total_allowance=0
        total_deduction=0
        for Key,value in d.items():
            total_allowance+=value[1]
            total_deduction+=value[2]
            print("Total allowance:",total_allowance)
            print(f"Total dedection:{total_deduction}")
    elif cho==3:
        n=input("Enter employee name to be search:")
        print("Write first letter of the name capital")
        for Key ,value in d.items():
            if Key==n:
                print(Key,value[0],value[1],value[2])
            else:
                print("Not found...")
    elif cho==4:
        break
    else:
        print("INVALID CHOICE")

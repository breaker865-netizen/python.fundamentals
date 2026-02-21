#Menu driven program to do various list functions
list1=[]
n=int(input("enter the number of elements:"))
for i in range(n):
    i=int(input("enter the element:"))
    list1.append(i)
print(f"Current list={list1}")
choice=0
while True:
    print("L I S T   O P E R A T I O N S")
    print("1.Append an element")
    print("2.Insert an element at a desired position")
    print("3.Append a list to the given list")
    print("4.modify the existing element")
    print("5.Delete the existing element by its position")
    print("6.Delete an existing element by its value")
    print("7.Sort the list in assending order")
    print("8.Sort the list in decending order")
    print("9.Display the list")
    print("10.Exit")
    choice=int(input("ENTER YOUR CHOICE(1-10):"))
    #Append an element
    if choice==1:
        e=int(input("Enter the element:"))
        list1.append(i)
        print("the element has been added in list")
    #Insert an element at a desired position
    elif choice==2:
        e=int(input("Enter the element:"))
        po=int(input("Enter the position:"))
        list1.insert(po,e)
        print("The element has been added")
    #Append a list to the given list
    elif choice==3:
        list2=[]
        n= int(input("Number of elements:"))
        for i in range (n):
            i= int(input("Enter the element:"))
            list2.append(i)
        list1.extend(list2)
    #modify the existing element
    elif choice==4:
        i=int(input("Enter the position of the element to be modified:"))
        if i< len(list1):
            new=int(input("enter the new element:"))
            old=list1[i]
            list1[i]=new
            print(f"The old element {old} has been modified")
        else:
            print("The position of the element is invalid")
    #Delete the existing element by its position
    elif choice==5:
        i=int(input("Enter the position of the element to bve deleted:"))
        if i <len(list1):
            ele=list1.pop(i)
            print(F"The element {ele} has been removed")
        else:
            print("The position enterd is invalid")
    #Delete an existing element by its value
    elif choice==6:
        elee=int(input("The element to be deleted:"))
        if elee in (list1):
            list1.remove(elee)
            print(f"The element {elee} is removed")
        else:
            print("The element entered is not in the list")
    #Sort the list in assending order
    elif choice==7:
        list1.sort()
        print("The list has been sorted")
    #Sort the list in decending order
    elif choice==8:
        list1.sort(reverse=True)
        print("The list has been sorted in reverse order")
    #Display the list
    elif choice==9:
        print("The list is:",list1)
    #.Exit
    elif choice==10:
        break
    else:
        print("The choice is not valid ")
        print("\n\n Press any key to continue..........")
        ch=input()
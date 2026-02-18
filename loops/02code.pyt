while True:
    sst = input("--Enter start to begin and exit to terminate: ").lower()

    if sst == 'start':
        try:
            n = int(input("How many numbers do you want to enter: "))

            sum5 = 0
            sum7 = 0
            sum11 = 0

            for  num in range(n):
                num = int(input("Enter the number: "))

                if num % 5 == 0:
                    sum5 += num
                if num % 7 == 0:
                    sum7 += num
                if num % 11 == 0:
                    sum11 += num

            print(f"Sum of multiples of 5 = {sum5}")
            print(f"Sum of multiples of 7 = {sum7}")
            print(f"Sum of multiples of 11 = {sum11}")

        except ValueError:
            print("Enter valid integer values only!")

    elif sst == 'exit':
        print("-----------Terminated-----------------")
        break

    else:
        print("Invalid input! Type 'start' or 'exit'.")

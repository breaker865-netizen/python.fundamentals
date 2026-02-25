"""
Mini Linux Quiz
"""

def ask_question():
    print("Answer the following question:")
    print("Is Linux a full operating system by itself? (yes/no)")
    
    ans = input("Your answer: ").strip().lower()

    if ans == "no":
        print("Correct.")
        print("Linux is a kernel. A complete operating system is typically built using the Linux kernel along with tools like GNU.")
    
    elif ans == "yes":
        print("Incorrect.")
        print("Linux by itself is only a kernel, not a complete operating system.")
    
    else:
        print("Invalid input. Please answer with 'yes' or 'no'.")

def bonus_question():
    print("\nBonus Question:")
    print("What does the kernel primarily manage?")
    print("1. Hardware resources")
    print("2. Web browsing")
    print("3. Text editing")

    choice = input("Enter 1, 2, or 3: ").strip()

    if choice == "1":
        print("Correct. The kernel manages hardware resources like CPU, memory, and devices.")
    elif choice in ["2", "3"]:
        print("Incorrect. The kernel is responsible for managing hardware resources.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    ask_question()
    bonus_question()
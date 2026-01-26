# Initialize an empty dictionary
student_records = {}

print("--- Data Entry Mode ---")
while True:
    name = input("Enter child's name (or type 'done' to stop): ").strip()
    
    # Check if the user wants to stop entering data
    if name.lower() == 'done':
        break
        
    marks = input(f"Enter marks for {name}: ")
    
    # Store the data in the dictionary
    student_records[name] = marks
    print(f"Added: {name} with {marks} marks.\n")

print("\n--- Search Mode ---")
while True:
    search_query = input("Enter name to search (or type 'exit' to quit): ").strip()
    
    if search_query.lower() == 'exit':
        break
        
    # Check if the name exists in our dictionary
    if search_query in student_records:
        print(f"Result: {search_query} has {student_records[search_query]} marks.")
    else:
        print(f"Error: '{search_query}' not found in records.")
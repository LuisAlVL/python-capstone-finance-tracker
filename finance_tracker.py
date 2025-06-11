# Displays all categories and their respective expenses
def view_expenses(data):
    for category in data:
        print(f"Category: {category}")
        for description, amount in data[category]:
            print(f"- {description}: ${amount}")


# Displays the amount spent per category
def view_summary(data):
    print("Summary:")
    for category in data:
        total = sum(amount for _, amount in data[category])
        print(f"{category}: ${total}")


# Display the menu and get the user selection
def show_menu():
    print("\nSelect an option:")
    print("1.Add expense")
    print("2.View all expenses")
    print("3.View amount spent by category")
    print("4.Exit")
    # Loop until a valid action is selected
    action = 0
    while True:
        try:
            action = int(input("Enter the option you want (1-4): "))
        except ValueError:
            print("Invalid action. Please select a valid option.")
        else:
            # If a valid option is selected break out of the loop
            if 0 < action and action < 5:
                break
            # The last if statement didn't execute, so an invalid option was selected
            print(f"{action} is an invalid action. Please select a valid option.")


    return action 


# Add expense
def add_expense(data):
    
    description = "" 
    # Loop until description is not empty
    while True:
        # Using strip to remove leading/trailing spaces
        description = input("Enter expense description: ").strip()
        # If description is not empty, break out of the loop
        if description:
            break
        print("Description cannot be empty. Please enter a valid description.")


    category = "" 
    # Loop until category is not empty
    while True:
        # Using strip to remove leading/trailing spaces
        category = input("Enter expense category: ").strip()
        # If category is not empty, break out of the loop
        if category:
            break
        print("Category cannot be empty. Please enter a valid category.")

    
    # Loop until a non-negative amount is provided
    while True:
        try:
            amount = float(input("Enter the expense amount: "))
        except ValueError:
            print("Invalid amount. Please enter a number.")
        else:
            if amount >= 0:
                break
            # The last if statement didn't execute, so a negative amount was selected.
            print("Negative amount detected. Please enter a positive amount.")

    if category in data:
            data[category].append((description, amount))
    else:
        data[category] = [(description,amount)]
    print("Expense added succesfully!")


# Dictionary of expenses, with categories as keys and a list of (description, amount) as values.
expenses = {}

print("Welcome to the Personal Finance Tracker!")
while True:
    
    action = show_menu()

    if action == 1:
        add_expense(expenses)
    elif action == 2:
        view_expenses(expenses)
    elif action == 3:
        view_summary(expenses)
    elif action == 4:
        break
    
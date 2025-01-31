# Ask for monthly allowance and expenses in different categories
# Calculate total expenses and remaining balance
# Display results
# Conditional message based on balance (depending on whether you overspent or underspent or spent just the right amount, write a specific message - try to be kind!)

# Finance tracker program

# Make a list
finance_list = []

while True:
   
    # Greet the user
    name = input("What is your name?").strip().lower()
    print(f"Hello {name}!\nThis is an finace tracker")

    invalid = True
   
    while invalid:
        try:
            # Ask user for how many monthly allowances
            num_expenses = int(input("How many different expenses? ").strip())
        except ValueError:
            print("Only type integers!")
        else: # When there is no error
            invalid = False
           
            # Loop as many items needed to add each item
            # Append each item to the list
            for i in range(num_expenses):
                grade = int(float(input(f"Grade for the assignment {i+1}: ")))
                finance_list.append(grade)

            # Find average for the assignment grades
            grades_sum = sum(finance_list)
            remaining_balance = grades_sum / num_expenses

            print(f"Your total expenses are {round(remaining_balance,1)}")


    # Ask user if they want to play again
    play_again = input("Do You Wish To Calculate Agian? [y] or [n]").strip().lower()
    if play_again != "y":
        break

    print("Thank you for calculating with this finance tracker program.")
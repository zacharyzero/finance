#This script is used to track my budget for different monthly expenses 

#Import time module
import time

#This is a list of my monthly budget expenses and their monetary costs
expenses = [
  ("Monthly Credit Card Payments", 1000),
  ("Monthly 403b Loan Payments", 400),
  ("Monthly Solar Loan Payments", 163),
  ("Monthly Car Loan Payments", 438),
  ("Monthly Car Insurance Payments", 136.99),
  ("Monthly Gasoline Costs", 250),
  ("Monthly Automotive Costs", 100),
  ("Monthly Cell Phone Payments", 150),
  ("Monthly Internet Payments", 70),
  ("Monthly Utilities Payments", 150),
  ("Monthly Grocery Costs", 800),
  ("Monthly Pet Costs", 300),
  ("Monthly Health Costs", 100),
  ("Monthly Financial Planning Costs", 300),
  ("Monthly Eating Out Costs", 800),
  ("Monthly Coffee Costs", 100),
  ("Monthly Subscription Costs", 67),
  ("Monthly Travel Costs", 400),
  ("Monthly Emergency Fund", 200),
]

#This function is used to view the list of expenses. 
def view_expenses():
  print("Here is a list of Zach's monthly expenses:")
  for category, amount in expenses:
    print(f"{category}: ${amount}")
  print()

#This function is used to add monthly expenses to the list
def add_expenses():
  category = input("Please enter the category of the new expense:\n")
  try:
    amount = float(input("\nPlease enter the dollar cost of the new expense (without '$'):\n"))
    amount = int(amount)
    if not category.lower().startswith("monthly"):
      category = f"Monthly {category}"
    for expense in expenses:
      if expense[0].casefold() == category:
        print(f"An expense with the category '{category}' already exists. Please update it instead.")
        return
    expenses.append((category, amount))
    print(f"\nYour new expense, ${amount} for {category}, has been added successfully!\n")
  except ValueError:
    print("Invalid option. Please try again.")

#This function is used to update monthly expenses in the list
def update_expenses():
  existing_expense_category = input('What is the existing expense category you want to update? (Remember to include "Monthly"\n').casefold()
  for i, expense in enumerate(expenses):
    if expense[0].casefold() == existing_expense_category:
      new_amount = float(input("\nPlease enter the new amount for this expense:\n"))
      new_amount = int(new_amount)
      expenses[i] = (expense[0], new_amount)
      print(f"Your expense for {existing_expense_category} has been updated to ${new_amount}.\n")
      return
  print("Invalid option. Try again.")

#This function is used to remove monthly expenses from the list      
def remove_expenses(): 
  old_expense_category = input("What is the category of the expense you want to remove?\n").casefold()
  for i, expense in enumerate(expenses):
    if expense[0].casefold() == old_expense_category:
      expenses.pop(i)
      print(f"The expense for {old_expense_category} has been removed.")
      return
  print(f"No expense found for category: {old_expense_category}")

#This function is used to add the total cost of expenses in the list
def total_expenses():
  total = sum(amount for category, amount in expenses)
  print(f"\nTotal Monthly Expenses: ${total}")

#Use a while loop to call the functions and start the script
while True:
  print("Use the options below to view or update your current expenses:")
  print("\n1. View Expenses")
  print("2. Add Monthly Expenses")
  print("3. Update Monthly Expenses")
  print("4. Remove Monthly Expenses")
  print("5. View Total Monthly Cost")
  print("6. Exit\n")
  choice = input("Enter your choice:\n")
  if choice == "1":
    view_expenses()
  elif choice == "2":
    add_expenses()
  elif choice == "3":
    update_expenses()
  elif choice == "4":
    remove_expenses()
  elif choice == "5":
    total_expenses()
  elif choice == "6":
    print("Goodbye!")
    break
  else:
    print("Invalid option. Try again.")
    time.sleep(1)

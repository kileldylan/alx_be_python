# Calculate the user's monthly savings based on inputted monthly income and expenses
monthly_income = int(input("Enter your monthly income: "))
total_monthly_expenses = int(input("Enter your total monthly expenses: "))

# Calculating monthly savings
monthly_savings = monthly_income - total_monthly_expenses

# Calculating the projected savings after one year with interest (5%)
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Printing the results
print("Your monthly savings are: ", monthly_savings)
print("Projected savings after one year, with interest, is: ", projected_savings)

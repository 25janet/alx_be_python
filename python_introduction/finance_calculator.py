monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

print("Your monthly savings are: $", round(monthly_savings, 2))
print("Projected savings after one year, with interest, is: $", round(projected_savings, 2))

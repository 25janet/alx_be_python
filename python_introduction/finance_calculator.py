monthlyIncome = input("Enter your monthly income: ")
monthlyExpenses = input("Enter your total monthly expenses: ")
monthlyIncome = float(monthlyIncome)
monthlyExpenses = float(monthlyExpenses)
monthlySavings = monthlyIncome - monthlyExpenses
projectedSavings = monthlySavings * 12 + (monthlySavings * 12 * 0.05)
print(f"Your monthly savings are ${monthlySavings}")
print(f"Projected savings after one year, with interest, is: ${projectedSavings}")

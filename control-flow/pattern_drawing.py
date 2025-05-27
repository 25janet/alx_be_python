size = int(input("Enter the size of the pattern:"))
while size <= 0:
    print("Please enter a positive number.")
    size = int(input("Enter the size of the pattern: "))
row = 0
while row < size:
    # For loop to print asterisks in the row
    for col in range(size):
        print("*", end="")  # Print without newline
    print()  # Move to the next line after each row
    row += 1
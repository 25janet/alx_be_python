def safe_divide(numerator, denominator):
    """
    Safely divide two numbers, handling invalid input and division by zero.

    Args:
        numerator (str): The numerator as a string (to be converted to float).
        denominator (str): The denominator as a string (to be converted to float).

    Returns:
        str: The result message or error message.
    """
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    return f"The result of the division is {result}"

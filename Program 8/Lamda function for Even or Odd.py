# Lambda function to check if a number is even or odd
even_or_odd = lambda x: "even" if x % 2 == 0 else "odd"

# Test the lambda function
number = 7
print(f"The number {number} is {even_or_odd(number)}.")

def gcd(a, b):
    # Base case: if b is 0, return a as the GCD
    if b == 0:
        return a
    # Recursive case: call gcd with b and the remainder of a divided by b
    return gcd(b, a % b)

# Test the function
num1 = 48
num2 = 18
print(f"The GCD of {num1} and {num2} is: {gcd(num1, num2)}")

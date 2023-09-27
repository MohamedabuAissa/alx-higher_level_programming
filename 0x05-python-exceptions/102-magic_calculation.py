def magic_calculation(a, b):
    result = 0
    
    for i in range(1, 3):
        if i > a:
            raise ValueError('Too far')  # Use a more specific exception type
        result += a ** b / i
    
    return result

# Example usage:
try:
    result = magic_calculation(2, 3)
    print("Result:", result)
except ValueError as e:
    print("Error:", e)

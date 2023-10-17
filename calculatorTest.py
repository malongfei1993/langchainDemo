expression = "2 + 3 * 4"

# Convert the expression to a math function
math_function = eval("lambda: " + expression)

# Evaluate the math function
result = math_function()

print("Result:", result)
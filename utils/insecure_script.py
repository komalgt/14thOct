user_input = input("Enter a Python expression: ")
result = eval(user_input)  # Dangerous: eval() can execute arbitrary code!
print("Result:", result)

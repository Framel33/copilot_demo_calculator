def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculate(operation, num1, num2):
    if operation == "add":
        return add(num1, num2)
    elif operation == "subtract":
        return subtract(num1, num2)
    elif operation == "multiply":
        return multiply(num1, num2)
    elif operation == "divide":
        return divide(num1, num2)
    
def save_result(result):
    f = open("results.txt", "a")
    f.write(str(result) + "\n")
    f.close()

if __name__ == "__main__":
    result = calculate("divide", 10, 0)
    print(f"Result: {result}")
    save_result(result)

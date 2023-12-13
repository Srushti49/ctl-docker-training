import sys

def divide_numbers(num1, num2):
    try:
        result = int(num1) / int(num2)
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero."

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python divide_script.py <num1> <num2>")
    else:
        result = divide_numbers(sys.argv[1], sys.argv[2])
        print(result)

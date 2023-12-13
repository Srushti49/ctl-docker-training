import sys

def multiply_numbers(num1, num2):
    return int(num1) * int(num2)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python multiply_script.py <num1> <num2>")
    else:
        result = multiply_numbers(sys.argv[1], sys.argv[2])
        print(result)

import math

def main():
    print("Menu:")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Power\n6. Square root\n7. Root\n8. Log\n9. Exponential\n10. Evaluate Equation\n11. Exit")
    
    while True:
        while True:
            try:
                choice = int(input("Enter your choice: "))
                break
            except ValueError:
                print("Invalid input. Please try again.")
                    
        match choice:
            case 1:
                add()
            case 2:
                subtract()
            case 3:
                multiply()
            case 4:
                divide()
            case 5:
                power()
            case 6:
                square_root()
            case 7:
                root()
            case 8:
                log()
            case 9:
                exponential()
            case 10:
                evaluate()
            case 11:
                break
            case _:
                print("Invalid choice. Please try again.")
                
                
                
def add():
    print("Addition")
    while True:
        try:    
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print(f"{a} + {b} = {a+b}")
            break
        except ValueError:
            print("Invalid input. Please try again.")
            
def subtract():
    print("Subtraction")
    while True:
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print(f"{a} - {b} = {a-b}")
            break
        except ValueError:
            print("Invalid input. Please try again.")
            
def multiply():
    print("Multiplication")
    while True:
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print(f"{a} * {b} = {a*b}")
            break
        except ValueError:
            print("Invalid input. Please try again.")
            
def divide():
    print("Division")
    while True:
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print(f"{a} / {b} = {a/b}")
            break
        except ValueError:
            print("Invalid input. Please try again.")
        except ZeroDivisionError:
            print("Division by zero is not allowed.")
            
def power():
    print("Power")
    while True:
        try:
            a = float(input("Enter the base: "))
            b = float(input("Enter the exponent: "))
            print(f"{a} ^ {b} = {a**b}")
            break
        except ValueError:
            print("Invalid input. Please try again.")
            
def square_root():
    print("Square Root")
    while True:
        try:
            a = float(input("Enter the number: "))
            print(f"√{a} = {math.sqrt(a)}")
            break
        except ValueError:
            print("Invalid input. Please try again.")
            
def root():
    print("Root")
    while True:
        try:
            a = float(input("Enter the number: "))
            b = float(input("Enter the root: "))
            print(f"{b}√{a} = {a**(1/b)}")
            break
        except ValueError:
            print("Invalid input. Please try again.")
            
def log():
    print("Logarithm")
    while True:
        try:
            a = float(input("Enter the number: "))
            b = float(input("Enter the base: "))
            print(f"log{b}({a}) = {math.log(a, b)}")
            break
        except ValueError:
            print("Invalid input. Please try again.")
            
def exponential():
    print("Exponential")
    while True:
        try:
            a = float(input("Enter the number: "))
            print(f"e^{a} = {math.exp(a)}")
            break
        except ValueError:
            print("Invalid input. Please try again.")
            
def evaluate():
    print("Evaluate Equation")
    while True:
        try:
            expression = input("Enter the expression: ")
            print
            print(f"{expression} = {eval(expression)}")
            break
        except Exception:
            print("Invalid expression. Please try again.")
            
def exit():
    print("Exiting the program.")
    sys.exit()
    
if __name__ == "__main__":
    main()
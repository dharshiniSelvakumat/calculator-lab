from cal_func import add, subtract
from cal_areaofrectangle import area_of_rectangle

def main():
    print("""Select the function from the given options:
    1. Add
    2. Subtract

    """)
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print(f"The result is: {add(a, b)}")
    elif choice == "2":
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print(f"The result is: {subtract(a, b)}")
    elif choice == "3":
        a = float(input("Enter the length: "))
        b = float(input("Enter the breadth: "))
        print(f"The result is: {area_of_rectangle(a, b)}")
        
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()

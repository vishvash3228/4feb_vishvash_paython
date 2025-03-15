def user():
   
    a = float(input("Enter Value Of A: "))  
    b = float(input("Enter Value Of B: "))

    print("\nSelect Option:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

   
    choice = input("Enter Number (1/2/3/4): ")

   
    if choice == '1':
        print("Sum:", a + b)
         
    elif choice == '2':
        print("Subtraction:", a - b) 

    elif choice == '3':
        print("Multiplication:", a * b) 

    elif choice == '4':
          print("Division:", a / b)  
    else:
        print("Invalid choice! Please enter a valid option.")

user()


accounts = []
  
print("Welcome to Python Bank Management system")

def create_account():
   
    acc_no = input("Enter Account Number: ")
    name = input("Enter Account Holder Name: ")
    acc_type = input("Enter Account Type (Saving/Current): ")

    new_account = {
        "acc_no": acc_no,
        "name": name,
        "type": acc_type,
        "balance": 0.0
    }
    accounts.append(new_account)
    print(" Account created successfully!\n")

def deposit():
    
    acc_no = input("Enter Account Number to deposit into: ")
    for acc in accounts:
        if acc["acc_no"] == acc_no:
            amount_str = input("Enter amount to deposit: ")
            try:
                amount = float(amount_str)
                if amount <= 0:
                    print("Amount must be positive!\n")
                    return
                acc["balance"] += amount
                print(f"Deposited {amount}. New Balance: {acc['balance']}\n")
            except ValueError:
                print(" Invalid amount! Please enter a number.\n")
            return
    print("Account not found!\n")

def withdraw():
    acc_no = input("Enter Account Number to withdraw from: ")
    for acc in accounts:
        if acc["acc_no"] == acc_no:
            amount_str = input("Enter amount to withdraw: ")
            try:
                amount = float(amount_str)
                if amount <= 0:
                    print(" Amount positive!\n")
                    return
                if amount > acc["balance"]:
                    print(" Insufficient balance!\n")
                    return
                acc["balance"] -= amount
                print(f" Withdrew {amount}. Remaining Balance: {acc['balance']}\n")
            except ValueError:
                print(" Invalid amount! Please enter a number.\n")
            return
    print("Account not found!\n")

def check_balance():
    acc_no = input("Enter Account Number to check balance: ").strip()
    for acc in accounts:
        if acc["acc_no"] == acc_no:
            print(f" Current Balance: {acc['balance']}\n")
            return
    print("Account not found!\n")

def view_all_accounts():
    
    if not accounts:
        print("\nNo accounts found!\n")
        return

    print("\n--- All Accounts ---")
    for acc in accounts:
        print(f"AccNo: {acc['acc_no']}, Name: {acc['name']}, Type: {acc['type']}, Balance: {acc['balance']}")
    print("--------------------\n")

def main():
   
    while True:
        print("=== Simple Bank Management ===")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. View All Accounts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            view_all_accounts()
        elif choice == "6":
            print("\nThank you for using the Bank Management System!\n")
            break
        else:
            print("Invalid choice! Please try again.\n")

create_account()
deposit()
withdraw()
check_balance()
view_all_accounts()
main()



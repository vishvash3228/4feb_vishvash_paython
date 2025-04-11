import pymysql


def get_connection():
    return pymysql.connect(
        host="localhost",
        user="your_username",      
        password="your_password",   
        database="bank_db"          
    )

# This is the basic user class
class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

# Customer class based on User
class Customer(User):
    def __init__(self, user_id, name, email, balance=0.0):
        super().__init__(user_id, name, email)
        self.__balance = balance  # Private balance, only used inside

    def add_money(self, amount):
        self.__balance += amount

    def take_money(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Not enough money in your account.")

    def check_balance(self):
        return self.__balance


class Banker(User):
    pass


def main():
    print("\n=== Welcome to Easy Bank App ===")

    customer = None 

    while True:
        print("\n1. Create New Customer")
        print("2. Add Money")
        print("3. Take Out Money")
        print("4. Show Balance")
        print("5. Exit")

        option = input("Choose an option (1-5): ")

        if option == '1':
            uid = input("Enter ID: ")
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            balance = float(input("Enter Starting Balance: "))
            customer = Customer(uid, name, email, balance)
            print("Customer created successfully!")

        elif option == '2':
            if customer:
                amount = float(input("Enter how much to add: "))
                customer.add_money(amount)
                print("Money added successfully.")
            else:
                print("Please create a customer first.")

        elif option == '3':
            if customer:
                amount = float(input("Enter how much to take: "))
                customer.take_money(amount)
            else:
                print("Please create a customer first.")

        elif option == '4':
            if customer:
                print("Your current balance is:", customer.check_balance())
            else:
                print("Please create a customer first.")

        elif option == '5':
            print("Thank you for using Easy Bank App!")
            break

        else:
            print("Please choose a valid option (1-5).")

if __name__ == '__main__':
    main()

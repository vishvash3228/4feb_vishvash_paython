#include <iostream>
using namespace std;

class BankAccount {
private:
    double balance;

public:
    BankAccount(double b) { balance = b; }

    void deposit(double amount) { balance += amount; }
    void withdraw(double amount) { if (amount <= balance) balance -= amount; }
    double getBalance() { return balance; }
};

main() {
    BankAccount account(1000);
    account.deposit(500);
    account.withdraw(300);
    cout << "Balance: " << account.getBalance();
}


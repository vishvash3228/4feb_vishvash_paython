#include <iostream>
using namespace std;

int add(int a, int b) { return a + b; }
int subtract(int a, int b) { return a - b; }
int multiply(int a, int b) { return a * b; }
float divide(int a, int b) { return b != 0 ? (float)a / b : 0; }

main() {
    int a, b, choice;
    cout << "Enter two numbers: ";
    cin >> a >> b;
    cout << "1. Add 2. Subtract 3. Multiply 4. Divide\nChoose: ";
    cin >> choice;

    if (choice == 1) cout << add(a, b);
    else if (choice == 2) cout << subtract(a, b);
    else if (choice == 3) cout << multiply(a, b);
    else if (choice == 4) cout << divide(a, b);
    else cout << "Invalid choice";

}


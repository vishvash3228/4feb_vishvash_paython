#include <iostream>
using namespace std;

int factorial(int n) {
    return (n <= 1) ? 1 : n * factorial(n - 1);
}

main() {
    int n;
    cout << "Enter number: ";
    cin >> n;
    cout << "Factorial: " << factorial(n);
}


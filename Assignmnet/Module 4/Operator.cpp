#include <iostream>
using namespace std;

main() {
    int a = 10, b = 5;

    cout << "Sum: " << a + b << endl;
    cout << "Difference: " << a - b << endl;
    cout << "Product: " << a * b << endl;
    cout << "Quotient: " << a / b << endl;
    cout << "Remainder: " << a % b << endl;

    cout << "Greater: " << (a > b) << endl;
    cout << "Smaller: " << (a < b) << endl;
    cout << "Equal: " << (a == b) << endl;

    cout << "AND: " << (a & b) << endl;
    cout << "OR: " << (a | b) << endl;
    cout << "XOR: " << (a ^ b) << endl;
}


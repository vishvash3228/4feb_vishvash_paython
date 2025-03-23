#include <iostream>
using namespace std;

class Calculator {
public:
    int add(int a, int b) { return a + b; }
    int subtract(int a, int b) { return a - b; }
    int multiply(int a, int b) { return a * b; }
    float divide(int a, int b) { return b != 0 ? (float)a / b : 0; }
};

main() {
    Calculator calc;
    cout << "Sum: " << calc.add(10, 5) << endl;
    cout << "Difference: " << calc.subtract(10, 5) << endl;
    cout << "Product: " << calc.multiply(10, 5) << endl;
    cout << "Quotient: " << calc.divide(10, 5) << endl;
}


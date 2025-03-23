#include <iostream>
using namespace std;

main() {
    int intVal = 10;
    double doubleVal = intVal;
    cout << "Implicit Conversion (int to double): " << doubleVal << endl;

    double num = 9.75;
    int castedInt = (int)num;
    cout << "Explicit Conversion (double to int): " << castedInt << endl;
}


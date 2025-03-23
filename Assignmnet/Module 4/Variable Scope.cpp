#include <iostream>
using namespace std;

int globalVar = 10;

void showScope() {
    int localVar = 5;
    cout << "Local: " << localVar << endl;
    cout << "Global: " << globalVar << endl;
}

main() {
    showScope();
    cout << "Accessing Global in main: " << globalVar;
}

#include <iostream>
using namespace std;

class Rectangle {
public:
    float length, width;

    void getInput() {
        cout << "Enter length and width: ";
        cin >> length >> width;
    }

    float calculateArea() {
        return length * width;
    }
};

main() {
    Rectangle rect;
    rect.getInput();
    cout << "Area: " << rect.calculateArea() << endl;
}


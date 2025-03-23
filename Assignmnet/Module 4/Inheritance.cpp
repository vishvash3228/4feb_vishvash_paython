#include <iostream>
using namespace std;

class Person {
public:
    string name;
    void setName(string n) { name = n; }
    void showName() { cout << "Name: " << name << endl; }
};

class Student : public Person {
public:
    void study() { cout << name << " is studying.\n"; }
};

class Teacher : public Person {
public:
    void teach() { cout << name << " is teaching.\n"; }
};

main() {
    Student s;
    s.setName("Alice");
    s.showName();
    s.study();

    Teacher t;
    t.setName("Bob");
    t.showName();
    t.teach();

}


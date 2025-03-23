#include <iostream>
using namespace std;

main() {
    string str, rev;
    cout << "Enter string: ";
    cin >> str;

    rev = string(str.rbegin(), str.rend());

    if (str == rev) cout << "Palindrome";
    else cout << "Not a Palindrome";

}


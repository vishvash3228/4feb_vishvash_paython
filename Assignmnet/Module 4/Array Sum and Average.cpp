#include <iostream>
using namespace std;

main() {
    int n, sum = 0;
    cout << "Enter size: ";
    cin >> n;
    int arr[n];

    for (int i = 0; i < n; i++) {
        cout << "Enter number: ";
        cin >> arr[i];
        sum += arr[i];
    }

    cout << "Sum: " << sum << endl;
    cout << "Average: " << (float)sum / n;
}


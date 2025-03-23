#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

main() {
    srand(time(0));
    int target = rand() % 100 + 1, guess, tries = 5;

    while (tries--) {
        cout << "Guess (1-100): ";
        cin >> guess;

        if (guess == target) {
            cout << "Correct!";
            return 0;
        }
        cout << (guess > target ? "Too high!\n" : "Too low!\n");
    }

    cout << "Out of tries! Number was " << target;
}


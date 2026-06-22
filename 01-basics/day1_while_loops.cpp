// Day 1 - While Loops
// Goal: Same logic as for loops, different syntax

#include <iostream>
using namespace std;

int main() {
    // Countdown using while loop - like a rocket launch
    int count;
    cout << "Enter countdown start number: ";
    cin >> count;

    cout << "Launch sequence: ";
    while (count > 0) {
        cout << count << "... ";
        count--;
    }
    cout << "Liftoff! 🚀" << endl;

    // Sum using while loop
    int n, sum = 0, i = 1;
    cout << "\nEnter N to find sum of 1 to N: ";
    cin >> n;
    while (i <= n) {
        sum += i;
        i++;
    }
    cout << "Sum = " << sum << endl;

    return 0;
}
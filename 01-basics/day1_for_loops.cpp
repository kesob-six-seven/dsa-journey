
#include <iostream>
using namespace std;

int main() {
    // Print 1 to N
    int n;
    cout << "Enter N: ";
    cin >> n;

    cout << "Counting up: ";
    for (int i = 1; i <= n; i++) {
        cout << i << " ";
    }
    cout << endl;

    // Multiplication table
    int num;
    cout << "Enter a number for its table: ";
    cin >> num;
    for (int i = 1; i <= 10; i++) {
        cout << num << " x " << i << " = " << (num * i) << endl;
    }

    return 0;
}
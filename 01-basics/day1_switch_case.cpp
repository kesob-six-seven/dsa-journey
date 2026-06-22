
#include <iostream>
using namespace std;

int main() {
    int day;
    cout << "Enter day number (1-7) to know your DSA topic for the day: ";
    cin >> day;

    switch (day) {
        case 1:
            cout << "Arrays" << endl;
            break;
        case 2:
            cout << "Strings" << endl;
            break;
        case 3:
            cout << "Recursion" << endl;
            break;
        case 4:
            cout << "Linked List" << endl;
            break;
        case 5:
            cout << "Trees" << endl;
            break;
        case 6:
            cout << "Graphs" << endl;
            break;
        case 7:
            cout << "Rest day, recharge!" << endl;
            break;
        default:
            cout << "Invalid day, pick 1-7." << endl;
    }

    return 0;
}
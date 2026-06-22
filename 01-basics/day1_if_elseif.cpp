
#include <iostream>
using namespace std;

int main() {
    int score;
    cout << "Enter your DSA mock test score (out of 100): ";
    cin >> score;

    if (score >= 90) {
        cout << "Beast mode. You're ready." << endl;
    } else if (score >= 60) {
        cout << "Solid. Keep grinding." << endl;
    } else if (score >= 40) {
        cout << "Okay start, more practice needed." << endl;
    } else {
        cout << "Back to basics, no shortcuts." << endl;
    }

    // Even/Odd check
    int num;
    cout << "Enter a number to check even/odd: ";
    cin >> num;
    if (num % 2 == 0)
        cout << num << " is Even" << endl;
    else
        cout << num << " is Odd" << endl;

    return 0;
}
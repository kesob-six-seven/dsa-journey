// Day 2 - Functions: Pass by Reference
// Goal: Understand that using '&' lets the function modify the ORIGINAL variable

#include <iostream>
using namespace std;

void levelUp(int &xp) { // '&' means we're passing the actual address, not a copy
    cout << "XP before bonus: " << xp << endl;
    xp = xp + 50; // this changes the ORIGINAL variable
    cout << "XP after bonus (inside function): " << xp << endl;
}

int main() {
    int playerXP = 100;

    cout << "Player XP before calling function: " << playerXP << endl;
    levelUp(playerXP);
    cout << "Player XP after calling function: " << playerXP << endl;
    // Notice: playerXP is now 150 outside too, because pass-by-reference
    // gives the function direct access to the original variable

    return 0;
}
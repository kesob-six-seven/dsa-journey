// Day 2 - Functions: Pass by Value
// Goal: Understand that changes inside the function DON'T affect the original variable

#include <iostream>
using namespace std;

void levelUp(int xp) {
    cout << "XP before bonus: " << xp << endl;
    xp = xp + 50; // this only changes the LOCAL copy
    cout << "XP after bonus (inside function): " << xp << endl;
}

int main() {
    int playerXP = 100;

    cout << "Player XP before calling function: " << playerXP << endl;
    levelUp(playerXP);
    cout << "Player XP after calling function: " << playerXP << endl;
    // Notice: playerXP is still 100 outside, because pass-by-value
    // only sends a COPY of the variable into the function

    return 0;
}
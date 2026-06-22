
#include <iostream>
using namespace std;

int main() {
    
    string topics[5] = {"Arrays", "Recursion", "Trees", "Graphs", "DP"};

    cout << "My DSA hitlist:" << endl;
    for (int i = 0; i < 5; i++) {
        cout << (i + 1) << ". " << topics[i] << endl;
    }

   
    string motto = "Consistency beats intensity";
    cout << "\nMy motto: " << motto << endl;
    cout << "Length of motto: " << motto.length() << " characters" << endl;
    cout << "First letter: " << motto[0] << endl;

    return 0;
}
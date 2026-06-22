
#include <iostream>
using namespace std;

int main() {
    
    int wins = 10;
    float gpa = 8.7;
    char grade = 'A';
    bool isPlacementReady = false; 

    cout << "Wins this semester: " << wins << endl;
    cout << "GPA: " << gpa << endl;
    cout << "Grade: " << grade << endl;
    cout << "Placement Ready? " << (isPlacementReady ? "Yes" : "Not yet, grinding...") << endl;

    return 0;
}
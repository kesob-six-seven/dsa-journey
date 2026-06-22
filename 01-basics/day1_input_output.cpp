
#include <iostream>
using namespace std;

int main() {
    string name;
    int age;

    cout << "Enter your name: ";
    cin >> name;

    cout << "Enter your age: ";
    cin >> age;

    cout << "Hey " << name << "! In 10 years you'll be " << (age + 10) << " years old." << endl;

   
    int a, b;
    cout << "Enter two numbers to add: ";
    cin >> a >> b;
    cout << "Sum = " << (a + b) << endl;

    return 0;
}
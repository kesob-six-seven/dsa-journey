#include<bits/stdc++.h>
using namespace std;
// recurssion 
// fibonacci series 
// this jsut hives sum of last 2 numbers in series 
int  f(int n){
    if (n<=1){
        return n;
    }
    else {
        return f(n-1)+f(n-2);
    }

    
//this pritns it till n   
    
}

    int main() {
        int n;
        cin>>n;
        // Edge case: if n is 0, print only 0
        if (n == 0) {
            cout << 0;
        }
        // Special case: if n is 1, print first two Fibonacci numbers
        else if (n == 1) {
            cout << 0 << " " << 1 << "\n";
        }
        // General case: generate and print Fibonacci series up to nth term
        else {
            int fib[n + 1];    // Array to store Fibonacci numbers up to index n
            fib[0] = 0;
            fib[1] = 1;
            // Fill the Fibonacci series using bottom-up dynamic programming
            for (int i = 2; i <= n; i++) {
                fib[i] = fib[i - 1] + fib[i - 2];
            }
            cout << "The Fibonacci Series up to " << n << "th term:" << endl;
            for (int i = 0; i <= n; i++) {
                cout << fib[i] << " ";
            }
        }
        return 0;
    }   


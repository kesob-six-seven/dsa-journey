#include <bits/stdc++.h>
using namespace std;

/*
 Recursive Bubble Sort 
 Time Complexity: O(N^2) for Worst & Average case.
 Best Case: O(N) when array is already sorted.
*/
void recursiveBubbleSort(int arr[], int n) {
    if (n == 1) return;
    
    int didswap = 0;
    for(int i = 0; i <= n - 2; i++) {
        if(arr[i] > arr[i+1]) {
            swap(arr[i], arr[i+1]); // STL swap, stop using temp variables
            didswap = 1; 
        }
    }
    
    if (didswap == 0) return;
    
    recursiveBubbleSort(arr, n - 1);
}

/*
 Recursive Insertion Sort 
 Time Complexity: O(N^2) for Worst & Average case.
 Best Case: O(N).
*/
void recursiveInsertionSort(int arr[], int i, int n) {
    if (i == n) return;
    int didswap=0;
    int j = i;
    while(j > 0 && arr[j-1] > arr[j]) {
        swap(arr[j], arr[j-1]); // STL swap
        j--;
        didswap=1;
    }
    if(didswap==0)return;
    recursiveInsertionSort(arr, i + 1, n);
}

int main() {
    // Basic test driver to prove it works
    int arr[] = {13, 46, 24, 52, 20, 9};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    recursiveBubbleSort(arr, n);
    // recursiveInsertionSort(arr, 0, n);
    
    for (int i = 0; i < n; i++) cout << arr[i] << " ";
    cout << endl;
    return 0;
}
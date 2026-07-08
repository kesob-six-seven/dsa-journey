#include<bits/stdc++.h>
using namespace std;
//this is shift 2

//this needs atleat 3 times of revison 
/*
 Merge Sort -its tc is way less that of the other sort
 much more optimised algo than that of the 
    (devide and merge)
 
 */
//tc is o(NlogN) - all cases 
// sc is o(n)- worst case 
// Function to merge two halves of the array
   void merge(vector<int>& arr, int low, int mid, int high) {
       // Create temp arrays
       vector<int> temp;
       int left = low, right = mid + 1;
       // Merge two sorted halves
       while (left <= mid && right <= high) {
           if (arr[left] <= arr[right])
               temp.push_back(arr[left++]);
           else
               temp.push_back(arr[right++]);
       }
       // Copy remaining elements from left half
       while (left <= mid)
           temp.push_back(arr[left++]);

       // Copy remaining elements from right half
       while (right <= high)
           temp.push_back(arr[right++]);

       // Copy sorted elements back to original array
       for (int i = low; i <= high; i++)
           arr[i] = temp[i - low];
   }

   // Recursive merge sort function
   void mergeSort(vector<int>& arr, int low, int high) {
       if (low >= high)
           return;

       // Find the middle index
       int mid = (low + high) / 2;

       // Recursively sort left half
       mergeSort(arr, low, mid);

       // Recursively sort right half
       mergeSort(arr, mid + 1, high);

       // Merge the two sorted halves
       merge(arr, low, mid, high);
   }


int main() {
   vector<int> arr = {5, 2, 8, 4, 1};
 
 mergeSort(arr, 0, arr.size() - 1);
   for (int x : arr)
       cout << x << " ";
   cout << endl;
   return 0;
}
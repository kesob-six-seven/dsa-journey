#include <bits/stdc++.h>
using namespace std;

// ---------------------------------------------------------
// Rotate array by one (left)
// Time Complexity: O(N) | Space Complexity: O(1)
// Logic: Store the first element, shift everything left by 1, 
// then place the stored element at the very end.
// ---------------------------------------------------------
void rotateArrayByOne(vector<int>& nums) {
    int temp = nums[0];  
    int n = nums.size();
    for(int i = 1; i < n; i++) {
        nums[i-1] = nums[i];
    }  
    nums[n-1] = temp;
}

// ---------------------------------------------------------
// Brute Force (left rotation by K)
// Time Complexity: O(N) | Space Complexity: O(K)
// Logic: Store the first K elements in a temp array. 
// Shift the remaining N-K elements to the left. 
// Finally, place the temp elements back at the end.
// ---------------------------------------------------------
void rotateLeftbyK(vector<int>& nums, int k) {
    int n = nums.size();
    if (n == 0) return;
    k = k % n; // Handle cases where K > N
    
    vector<int> temp(k);
    for(int i = 0; i < k; i++) {
        temp[i] = nums[i];
    }
    for (int i = k; i < n; i++) {
        nums[i - k] = nums[i];
    }
    for(int i = n - k; i < n; i++) {
        nums[i] = temp[i - n + k];
    }
    for (int i = 0; i < n; i++) {
        cout << nums[i] << " ";
    }
    cout << endl;
}

// ---------------------------------------------------------
// Optimal (left rotation by K)
// Time Complexity: O(N) | Space Complexity: O(1)
// Logic: Reverse first K elements, reverse remaining N-K elements, 
// then reverse the entire array to snap them into place.
// ---------------------------------------------------------
void optimalleft(vector<int>& nums, int k) {
    int n = nums.size();
    if(n == 0) return;
    k = k % n;
    
    reverse(nums.begin(), nums.begin() + k);
    reverse(nums.begin() + k, nums.end());
    reverse(nums.begin(), nums.end());
}

// ---------------------------------------------------------
// Normal approach (right rotation by K)
// Time Complexity: O(N) | Space Complexity: O(K)
// ---------------------------------------------------------
void rotateRightK(vector<int>& nums, int k) {
    if (k == 0) return;
    int n = nums.size();
    k = k % n;
    
    vector<int> temp(k); // Fixed from VLA to vector for C++ standards
    for (int i = n - k; i < n; i++) {
        temp[i - n + k] = nums[i];
    }
    for (int i = n - k - 1; i >= 0; i--) {
        nums[i + k] = nums[i];
    }
    for (int i = 0; i < k; i++) {
        nums[i] = temp[i];
    }
}

// ---------------------------------------------------------
// Optimal (right rotation by K)
// Time Complexity: O(N) | Space Complexity: O(1)
// Logic: Reverse the whole array, reverse first K elements, 
// then reverse the remaining N-K elements.
// ---------------------------------------------------------
void rotate(vector<int>& nums, int k) {
    int n = nums.size();
    if (n == 0) return; 
    k = k % n; 
    
    reverse(nums.begin(), nums.end());
    reverse(nums.begin(), nums.begin() + k);
    reverse(nums.begin() + k, nums.end());
}

int main() {
    vector<int> nums1 = {1, 2, 3, 4, 5, 6, 7};
    rotateArrayByOne(nums1);
    
    vector<int> nums2 = {1, 2, 3, 4, 5, 6, 7};
    rotate(nums2, 3);

    return 0;
}
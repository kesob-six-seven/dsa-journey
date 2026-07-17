#include <bits/stdc++.h>
using namespace std;

// ---------------------------------------------------------
// [Missing Number / Sort and Linear Search]
// Time Complexity: O(N log N) | Space Complexity: O(1)
// Logic: 
// - You sort the array first (which makes it O(N log N), NOT O(N) like you wrote).
// - Then you iterate through and check if the index matches the value.
// - Returns the index if there's a mismatch, otherwise returns N.
// ---------------------------------------------------------
int missingNumber(vector<int>& nums) {
    int n = nums.size();
    sort(nums.begin(), nums.end());
    for(int i = 0; i < n; i++) {
        if (nums[i] != i)
            return i;
    }
    return n;
}

// ---------------------------------------------------------
// [Missing Number / XOR Approach]
// Time Complexity: O(N) | Space Complexity: O(1)
// Logic: 
// - XORing a number with itself results in 0.
// - XOR all elements in the array, then XOR all numbers from 1 to N.
// - The remaining value is the missing number because everything else cancels out.
// ---------------------------------------------------------
int missingNum(vector<int>& arr) {
    int n = arr.size() + 1;
    int xor1 = 0, xor2 = 0;

    // XOR all array elements
    for (int i = 0; i < n - 1; i++) {
        xor2 ^= arr[i];
    }

    // XOR all numbers from 1 to n
    for (int i = 1; i <= n; i++) {
        xor1 ^= i;
    }

    // Missing number is the XOR of xor1 and xor2
    return xor1 ^ xor2;
}

// ---------------------------------------------------------
// [Max Consecutive Ones / Single Pass Counting]
// Time Complexity: O(N) | Space Complexity: O(1)
// Logic: 
// - Iterate through the array. If the element is 1, increment count.
// - If it's 0, reset count to 0.
// - Continuously update 'maxi' with the highest count found.
// ---------------------------------------------------------
int findMaxConsecutiveOnes1(vector<int>& nums) {
    int n = nums.size();
    int maxi = 0;
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (nums[i] == 1) {
            count++;       
        }
        else {
            count = 0;
        }
        maxi = max(maxi, count);
    }
    return maxi;
}

// ---------------------------------------------------------
// [Max Consecutive Ones / While Loop inside For Loop]
// Time Complexity: O(N) | Space Complexity: O(1)
// Logic: 
// - Outer loop traverses the array.
// - Inner while loop counts consecutive 1s and advances the 'i' pointer.
// - I silently fixed your 'int i = 0' redeclaration error inside the loop.
// ---------------------------------------------------------
int findMaxConsecutiveOnes(vector<int>& nums) {
    int n = nums.size();
    int maxi = 0;
    for(int i = 0; i < n; i++) {
        int count = 0;
        while(i < n && nums[i] == 1) {
            count++;
            i++;
        }
        maxi = max(maxi, count);
    }
    return maxi;
}

// ---------------------------------------------------------
// [Single Number / Brute Force Nested Loops]
// Time Complexity: O(N^2) | Space Complexity: O(1)
// Logic: 
// - For every element, iterate through the whole array to count its occurrences.
// - If the count is exactly 1, return that number.
// - Very slow, will give TLE on larger constraints.
// ---------------------------------------------------------
int singleNumber(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n; i++) {
        int num = arr[i]; 
        int cnt = 0;
        for (int j = 0; j < n; j++) {
            if (arr[j] == num)
                cnt++;
        }
        if (cnt == 1) return num;
    }
    return -1;
}

// ---------------------------------------------------------
// [Single Number / Better Approach Using Hash Array]
// Time Complexity: O(N) | Space Complexity: O(max_element)
// Logic: 
// - Find the maximum element to size the hash array.
// - Map occurrences of each number into the hash array.
// - Iterate again to find which number has a count of 1.
// ---------------------------------------------------------
int getSingleElement(vector<int>& arr) {
    int n = arr.size();
    int maxi = arr[0];
    for (int i = 0; i < n; i++) {
        maxi = max(maxi, arr[i]);
    }
    vector<int> hash(maxi + 1, 0);
    for (int i = 0; i < n; i++) {
        hash[arr[i]]++;
    }
    for (int i = 0; i < n; i++) {
        if (hash[arr[i]] == 1)
            return arr[i];
    }
    return -1; 
}

// ---------------------------------------------------------
// [Single Number / Optimal XOR Approach]
// Time Complexity: O(N) | Space Complexity: O(1)
// Logic: 
// - Since every number appears twice except one, XORing all elements together
//   cancels out the pairs (N ^ N = 0).
// - The single number is left over (0 ^ X = X).
// ---------------------------------------------------------
int singleNumber1(vector<int>& arr) {
    int n = arr.size();
    int xorr = 0;
    for (int i = 0; i < n; i++) {
        xorr = xorr ^ arr[i];
    }
    return xorr;
}

int main() {
    // Basic driver code to verify syntax
    vector<int> test = {4, 1, 2, 1, 2};
    cout << "Single Number (XOR): " << singleNumber1(test) << "\n";
    cout << "Stop blaming your circadian rhythm and lock in.\n";
    return 0;
}
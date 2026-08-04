#include <bits/stdc++.h>
using namespace std;

/*
   =========================================================
   TOPIC: ARRAYS (Medium)
   PROBLEMS: Next Permutation, Leaders in an Array
   STATUS: COMPLETED
   =========================================================
*/

// ==========================================
// 1. NEXT PERMUTATION
// ==========================================
/*
   THEORY & INTUITION:
   "Next Permutation" means finding the next lexicographically (dictionary order) greater arrangement of numbers.
   Example: [1, 2, 3] -> [1, 3, 2]
   If it's the very last permutation (e.g., [3, 2, 1]), the next one cycles back to the lowest ([1, 2, 3]).
   
   - Brute Force: Generate all sorted permutations (recursion), do a linear search for the current one, return the next. TC: O(N! * N) -> TLE.
   - Better: C++ STL provides `next_permutation(nums.begin(), nums.end())`.
   
   - Optimal Algorithm (Step-by-Step):
     1. Find the "dip" / break-point: Traverse from right to left to find the first index `i` where a[i] < a[i+1].
     2. If no dip exists (i == -1), the array is entirely in descending order (last permutation). Just reverse it and return.
     3. If a dip exists, we need to swap a[i] with the smallest element on its right that is greater than a[i]. Traverse from right to left to find this element and swap.
     4. After the swap, the elements to the right of `i` will still be in descending order. Reverse them to make them sorted in ascending order (which gives the smallest possible prefix).
   
   COMPLEXITY:
   - TC: O(N). In the worst case, we do 3 passes (find dip, find swap element, reverse right half), equating to O(3N) which is O(N).
   - SC: O(1). Everything is done in-place.
*/
vector<int> nextPermutationOptimal(vector<int>& nums) {
    int ind = -1;
    int n = nums.size();
    
    // Step 1: Find the break point
    for(int i = n - 2; i >= 0; i--) {
        if (nums[i] < nums[i+1]) {
            ind = i;
            break;
        }
    }
    
    // Step 2: If no break point, reverse the whole array
    if (ind == -1) {
        reverse(nums.begin(), nums.end());
        return nums;
    }
    
    // Step 3: Find someone slightly greater to swap with
    for(int i = n - 1; i > ind; i--) {
        if(nums[i] > nums[ind]) {
            swap(nums[i], nums[ind]);
            break;
        }
    }
    
    // Step 4: Reverse the remaining right half
    reverse(nums.begin() + ind + 1, nums.end());
    return nums;
}


// ==========================================
// 2. LEADERS IN AN ARRAY
// ==========================================
/*
   THEORY & INTUITION:
   An element is considered a "leader" if it is strictly greater than ALL the elements to its right.
   Note: The rightmost element is ALWAYS a leader since there is nothing to its right.
*/

// 🟢 Brute Force
// For each element, iterate through all elements to its right. If we find any element strictly greater, it's not a leader.
// TC: O(N^2) | SC: O(N) for answer array
vector<int> leadersBrute(vector<int>& nums) {
    vector<int> ans;
    for (int i = 0; i < nums.size(); i++) {
        bool leader = true;
        for (int j = i + 1; j < nums.size(); j++) {
            if (nums[j] >= nums[i]) {
                leader = false;
                break;
            }
        }
        if (leader) ans.push_back(nums[i]);
    }
    return ans;
}

// 🔵 Optimal Approach
// Instead of looking rightwards for every element, scan from right-to-left.
// Keep track of the maximum element seen so far. If the current element is greater than the max seen so far, it is a leader.
// TC: O(N) | SC: O(N) to store and return the answer array
vector<int> leadersOptimal(vector<int>& nums) {
    vector<int> ans;
    if(nums.empty()) return ans;
    
    int max_val = nums[nums.size() - 1];
    ans.push_back(max_val); // The last element is always a leader
    
    // Check elements from right to left
    for (int i = nums.size() - 2; i >= 0; i--) {
        if (nums[i] > max_val) { // Strictly greater than the max seen so far
            ans.push_back(nums[i]);
            max_val = nums[i]; // Update the max
        }
    }
    
    // Reverse the vector to output leaders from left to right as they appear in the original array
    reverse(ans.begin(), ans.end());
    return ans;
}
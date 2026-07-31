#include <bits/stdc++.h>
using namespace std;

/*
   =========================================================
   TOPIC: ARRAYS (Medium)
   PROBLEM: Longest Consecutive Sequence
   STATUS: COMPLETED
   =========================================================
   
   THEORY & INTUITION:
   We need to find the length of the longest sequence of consecutive 
   integers in an unsorted array. 
   Example: [100, 4, 200, 1, 3, 2] -> Sequence is [1, 2, 3, 4] -> Length 4.
*/

class Solution {
private:
    // Helper function for Brute Force
    bool linearSearch(vector<int>& a, int num) {
        for (int i = 0; i < a.size(); i++) {
            if (a[i] == num) return true;
        }
        return false;
    }

public:
    // ==========================================
    // 1. BRUTE FORCE
    // ==========================================
    /*
       Intuition: Pick every element `x`, and linearly search for `x+1`, 
       `x+2`, etc., in the array until we can't find the next number.
       
       TC: O(N^3) in the worst case. (For N elements, we might search for N 
           consecutive elements, and each linear search takes O(N)). 
       SC: O(1)
    */
    int longestConsecutiveBrute(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        
        int longest = 1; 
        int n = nums.size();

        for (int i = 0; i < n; i++) {
            int x = nums[i]; 
            int cnt = 1; 

            // linearSearch takes O(N), and we might do it N times
            while (linearSearch(nums, x + 1) == true) {
                x += 1; 
                cnt += 1; 
            }
            longest = max(longest, cnt);
        }
        return longest;
    }

    // ==========================================
    // 2. BETTER APPROACH (Sorting)
    // ==========================================
    /*
       Intuition: If we sort the array, consecutive elements will be adjacent.
       We just iterate through the sorted array and count sequences.
       
       TC: O(N log N) for sorting + O(N) for iterating = O(N log N).
       SC: O(1) or O(N) depending on the sorting algorithm used.
    */
    int longestConsecutiveBetter(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        
        sort(nums.begin(), nums.end());
        
        int lastSmaller = INT_MIN;
        int cnt = 0;
        int longest = 1;
        
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] - 1 == lastSmaller) {
                // Number is consecutive
                cnt += 1;
                lastSmaller = nums[i];
            } 
            else if (nums[i] != lastSmaller) {
                // Number is not consecutive and not a duplicate
                cnt = 1;
                lastSmaller = nums[i];
            }
            longest = max(longest, cnt);
        }
        return longest;
    }

    // ==========================================
    // 3. OPTIMAL APPROACH (Hash Set)
    // ==========================================
    /*
       Intuition: Put all numbers into an unordered_set. 
       To find sequences efficiently, we only start counting when we find the 
       "start" of a sequence. A number `x` is a start if `x - 1` does NOT 
       exist in the set.
       
       TC: O(N). Putting elements in set is O(N). Iterating through set and 
           finding sequences takes O(2N) at worst. Overall O(N).
       SC: O(N) for the unordered_set.
    */
    int longestConsecutiveOptimal(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;

        int longest = 1;
        unordered_set<int> st;

        // Put all elements in set
        for (int i = 0; i < n; i++) {
            st.insert(nums[i]);
        }

        // Find sequences
        for (auto it : st) {
            // Check if 'it' is the starting number of a sequence
            if (st.find(it - 1) == st.end()) {
                int cnt = 1;
                int x = it;

                // Find consecutive numbers
                while (st.find(x + 1) != st.end()) {
                    x += 1;
                    cnt += 1;
                }
                longest = max(longest, cnt);
            }
        }
        return longest;
    }
};
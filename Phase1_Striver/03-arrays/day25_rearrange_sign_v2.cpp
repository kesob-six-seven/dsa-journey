#include <bits/stdc++.h>
using namespace std;

/*
   =========================================================
   TOPIC: ARRAYS (Medium)
   PROBLEM: Rearrange Array Elements by Sign (Variety 2)
   STATUS: COMPLETED
   =========================================================
   
   THEORY & INTUITION:
   Unlike Variety 1, this problem states that the number of positive 
   and negative elements might NOT be equal. We still need to alternate 
   them (positive, negative, positive...) but if one sign runs out, 
   we simply append the remaining elements of the other sign at the end 
   of the array without altering their relative order.
   
   Since we cannot easily predict the indices in a single pass without 
   overwriting data (due to the unequal counts), the standard optimal 
   approach is to fall back to a 2-pass method using extra space.
   
   ALGORITHM (Step-by-Step):
   1. Create two separate vectors/arrays: `pos` and `neg`.
   2. Traverse the original array and push positive numbers into `pos` 
      and negative numbers into `neg`.
   3. Check which array has a larger size.
   4. Iterate up to the size of the smaller array, placing elements 
      back into the original array in alternating order (pos at even 
      indices, neg at odd indices).
   5. Once the smaller array is exhausted, take the leftover elements 
      from the larger array and append them directly to the end of the 
      original array.
   
   COMPLEXITY:
   - Time Complexity (TC): O(N) 
     We do one pass to separate the elements O(N), and another pass 
     to merge them back O(N). Total TC = O(N).
   - Space Complexity (SC): O(N) 
     We store all elements in the `pos` and `neg` arrays. 
     O(pos elements) + O(neg elements) = O(N) total extra space.
*/

vector<int> rearrangeArray(vector<int> nums) {
    vector<int> pos;
    vector<int> neg;
    int n = nums.size();
    
    // Step 1 & 2: Segregate positive and negative elements
    for(int i = 0; i < n; i++) {
        if (nums[i] > 0) {
            pos.push_back(nums[i]);
        } else {
            neg.push_back(nums[i]);
        }
    }
    
    // Step 3, 4 & 5: Merge them back alternately, then append leftovers
    if (pos.size() > neg.size()) {
        // Negatives run out first
        for(int i = 0; i < neg.size(); i++) {
            nums[2 * i] = pos[i];
            nums[2 * i + 1] = neg[i];
        }
        // Append leftover positives
        int index = neg.size() * 2;
        for(int i = neg.size(); i < pos.size(); i++) {
            nums[index] = pos[i];
            index++;
        }
    } 
    else {
        // Positives run out first (or they are equal)
        for(int i = 0; i < pos.size(); i++) {
            nums[2 * i] = pos[i];
            nums[2 * i + 1] = neg[i];
        }
        // Append leftover negatives
        int index = pos.size() * 2;
        for(int i = pos.size(); i < neg.size(); i++) {
            nums[index] = neg[i];
            index++;
        }
    }
    
    return nums;
}
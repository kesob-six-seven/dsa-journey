#include <bits/stdc++.h>
using namespace std;

/*
   =========================================================
   TOPIC: ARRAYS (Medium)
   PROBLEMS: Maximum Subarray, Buy/Sell Stock, Rearrange by Sign
   STATUS: COMPLETED
   =========================================================
*/

// ==========================================
// 1. MAXIMUM SUBARRAY (KADANE'S ALGORITHM)
// ==========================================

// 🟢 Brute Force: Check every possible subarray
// TC: O(N^3) | SC: O(1)
int maxSubArrayBrute(vector<int>& nums) {
    int maxy = INT_MIN;
    int n = nums.size();
    for(int i = 0; i < n; i++) {
        for(int j = i; j < n; j++) {
            int sum = 0;
            for(int k = i; k <= j; k++) {
                sum += nums[k];
            }
            maxy = max(maxy, sum);
        }
    }
    return maxy;
}

// 🟡 Better Approach: Two loops
// Intuition: We don't need a third loop to calculate the sum. We can just keep adding to the previous sum.
// TC: O(N^2) | SC: O(1)
int maxSubArrayBetter(vector<int>& nums) {
    int maxy = INT_MIN;
    int n = nums.size();
    for(int i = 0; i < n; i++) {
        int sum = 0;
        for(int j = i; j < n; j++) {
            sum += nums[j];
            maxy = max(maxy, sum);
        }
    }
    return maxy;
}

// 🔵 Optimal Approach: Kadane's Algorithm
// Intuition: A subarray with a negative sum will never contribute to a maximum sum. 
// If our running sum becomes < 0, we reset it to 0 and start a new subarray.
// TC: O(N) | SC: O(1)
int maxSubArrayOptimal(vector<int>& nums) {
    long long sum = 0, maxi = LONG_MIN;
    int start = 0, ansStart = -1, ansEnd = -1;
    
    for(int i = 0; i < nums.size(); i++) {
        if (sum == 0) start = i; // Tracking start index for printing
        
        sum += nums[i];
        
        if (sum > maxi) {
            maxi = sum;
            ansStart = start;
            ansEnd = i;
        }
        
        if (sum < 0) {
            sum = 0; // Reset if negative
        }
    }
    // Note: If you need to print the subarray, it lies from nums[ansStart] to nums[ansEnd]
    return maxi;
}


// ==========================================
// 2. BEST TIME TO BUY AND SELL STOCK
// ==========================================

// 🟢 Brute Force: Try buying on every day and selling on all future days
// TC: O(N^2) | SC: O(1)
int maxProfitBrute(vector<int>& prices) {
    int maxp = 0;
    int n = prices.size();
    for(int i = 0; i < n; i++) {
        for(int j = i + 1; j < n; j++) {
            int current_profit = prices[j] - prices[i];
            maxp = max(maxp, current_profit);
        }
    }
    return maxp;
}

// 🔵 Optimal Approach: Track Minimum Price
// Intuition: If we are selling on day 'i', to maximize profit we must have bought on the day with the lowest price BEFORE day 'i'.
// TC: O(N) | SC: O(1)
int maxProfitOptimal(vector<int>& prices) {
    int max_profit = 0;
    int min_price = INT_MAX;
    
    for(int price : prices) {
        if (price < min_price) {
            min_price = price; // Update the lowest price seen so far
        } else {
            max_profit = max(max_profit, price - min_price); // Check profit if we sold today
        }
    }
    return max_profit;
}


// ==========================================
// 3. REARRANGE ARRAY ELEMENTS BY SIGN (Variety 1 - Equal Pos/Neg)
// ==========================================

// 🟢 Brute Force: Separate into two arrays, then merge
// TC: O(N + N/2) -> O(N) | SC: O(N)
vector<int> rearrangeArrayBrute(vector<int>& nums) {
    vector<int> pos;
    vector<int> neg;
    
    for(int i = 0; i < nums.size(); i++) {
        if (nums[i] > 0) {
            pos.push_back(nums[i]);
        } else {
            neg.push_back(nums[i]);
        }
    }
    
    for(int i = 0; i < nums.size() / 2; i++) {
        nums[2 * i] = pos[i];
        nums[2 * i + 1] = neg[i];
    }
    
    return nums;  
}

// 🔵 Optimal Approach: Two Pointers (Single Pass)
// Intuition: We know positives go to even indices (0,2,4) and negatives go to odd indices (1,3,5).
// We can place them directly into a new array in one pass.
// TC: O(N) | SC: O(N)
vector<int> rearrangeArrayOptimal(vector<int>& A) {
    int n = A.size();
    vector<int> ans(n, 0);
    
    int posIndex = 0; // Even indices
    int negIndex = 1; // Odd indices
    
    for (int i = 0; i < n; i++) {
        if (A[i] < 0) {
            ans[negIndex] = A[i];
            negIndex += 2;
        } else {
            ans[posIndex] = A[i];
            posIndex += 2;
        }
    }
    
    return ans;
}
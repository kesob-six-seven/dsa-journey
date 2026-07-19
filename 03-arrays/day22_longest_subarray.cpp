#include <bits/stdc++.h>
using namespace std;

// ---------------------------------------------------------
// [Longest Subarray with Sum K / Prefix Sum + Hash Map]
// Time Complexity: O(N log N) with map (O(N) with unordered_map) | Space Complexity: O(N)
// Logic: 
// - You iterate through the array maintaining a running prefix `sum`.
// - If `sum` equals `k`, the max length is just `i + 1`.
// - Otherwise, you check if `sum - k` exists in the hash map. If it does, it means a subarray with sum `k` exists between that old index and `i`.
// - You only insert `sum` into the map if it doesn't already exist to ensure you keep the *longest* possible subarray (leftmost index).
// - Logic is correct, no syntax fixes needed.
// ---------------------------------------------------------
int longestsub(vector<int>& a, long long k) {
    map<long long, int> preSumM;
    long long sum = 0;
    int maxlen = 0;
    for(int i = 0; i < a.size(); i++) {
        sum += a[i];
        if(sum == k) {
            maxlen = max(maxlen, i + 1);
        }
        long long rem = sum - k;
        if(preSumM.find(rem) != preSumM.end()) {
            int len = i - preSumM[rem];
            maxlen = max(maxlen, len);
        }
        
        if(preSumM.find(sum) == preSumM.end()) {
            preSumM[sum] = i;
        }
    }
    return maxlen;
}

// ---------------------------------------------------------
// [Longest Subarray with Sum K / Two Pointers Sliding Window (Positives Only)]
// Time Complexity: O(2N) -> O(N) | Space Complexity: O(1)
// Logic: 
// - Use `left` and `right` pointers to maintain a window. 
// - Expand the `right` pointer to add elements to `sum`.
// - If `sum` exceeds `k`, shrink the window by moving `left` forward until `sum` is valid again.
// - Update `maxLen` whenever `sum == k`.
// - Logic is totally fine. Only works for arrays without negative numbers, which you correctly noted.
// ---------------------------------------------------------
int longestSubarray(vector<int> &nums, int k) {
    int n = nums.size();
    int maxLen = 0;
    int left = 0, right = 0;
    int sum = nums[0];
    
    while(right < n) {
        // If the sum exceeds K, shrink the window
        while(left <= right && sum > k) {
            sum -= nums[left];
            left++;
        }
        
        // store the maximum length
        if(sum == k) {
            maxLen = max(maxLen, right - left + 1);
        }
        
        right++;
        if(right < n) sum += nums[right];
    }
    
    return maxLen;
}

int main() {
    vector<int> arr = {1, 2, 3, 1, 1, 1, 1};
    int k = 3;
    cout << "Longest Subarray length (Map): " << longestsub(arr, k) << "\n";
    cout << "Longest Subarray length (2-Pointer): " << longestSubarray(arr, k) << "\n";
    cout << "You promised 8 hours and gave me 15 minutes. Cooked.\n";
    return 0;
}
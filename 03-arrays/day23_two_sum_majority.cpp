#include <bits/stdc++.h>
using namespace std;

/*
   =========================================================
   TOPIC: ARRAYS (Medium)
   PROBLEMS: Two Sum, Majority Element, Sort 0 1 2
   STATUS: COMPLETED
   =========================================================
*/

// ==========================================
// 1. TWO SUM
// ==========================================

// 🟢 Brute Force: Check every possible pair
// TC: O(N^2) | SC: O(1)
vector<int> twoSumBrute(vector<int>& nums, int target) {
    int n = nums.size();
    for(int i = 0; i < n; i++) {
        for(int j = i + 1; j < n; j++) {
            if((nums[j] + nums[i]) == target) {
                return {i, j};
            }
        }
    }
    return {};
}

// 🟡 Better Approach: Hashing (Use this if array isn't sorted)
// Intuition: As we iterate, we ask "Have I seen (target - current_element) before?" 
// If yes, we found our pair. If no, we store the current element in the map.
// TC: O(N) | SC: O(N)
vector<int> twoSumBetter(vector<int>& nums, int target) {
    unordered_map<int, int> mpp; // Stores {element, index}
    int n = nums.size();
    
    for(int i = 0; i < n; i++) {
        int moreneeded = target - nums[i]; 
        
        // If the needed number is already in our map, return both indices
        if (mpp.find(moreneeded) != mpp.end()) {
            return {mpp[moreneeded], i};
        }
        // Otherwise, add current number and its index to the map
        mpp[nums[i]] = i;
    }
    return {};
}

// 🔵 Optimal Approach: 2 Pointers (Best if we just need YES/NO, or if array is already sorted)
// Intuition: Sort the array. Put pointers at start and end. 
// If sum > target, move right pointer left to decrease sum. 
// If sum < target, move left pointer right to increase sum.
// TC: O(N log N) | SC: O(N) to store indices
vector<int> twoSumOptimal(vector<int> arr, int target) {
    int n = arr.size();
    vector<pair<int, int>> numsWithIndex; // Need to store original indices before sorting
    
    for (int i = 0; i < n; i++) {
        numsWithIndex.push_back({arr[i], i});
    }
    sort(numsWithIndex.begin(), numsWithIndex.end());

    int left = 0, right = n - 1;
    while (left < right) {
        int sum = numsWithIndex[left].first + numsWithIndex[right].first;
        if (sum == target) {
            return {numsWithIndex[left].second, numsWithIndex[right].second};
        } else if (sum < target) {
            left++; // Need a bigger sum
        } else {
            right--; // Need a smaller sum
        }
    }
    return {-1, -1};
}


// ==========================================
// 2. MAJORITY ELEMENT (> N/2)
// ==========================================

// 🟢 Brute Force: Count occurrences of every element
// TC: O(N^2) | SC: O(1)
int majorityElementBrute(vector<int>& nums) {
    int n = nums.size();
    for(int i = 0; i < n; i++) {
        int count = 1;
        for(int j = i + 1; j < n; j++) {
            if(nums[j] == nums[i]) {
                count++;
            }
        }
        if (count > n / 2) {
            return nums[i];
        }
    }
    return -1;  
}

// 🟡 Better Approach: Hashing (Frequency Map)
// Intuition: Store frequency of each element. Then check which frequency > N/2.
// TC: O(N log N) or O(N) | SC: O(N)
int majorityElementBetter(vector<int>& nums) {
    unordered_map<int, int> mpp;
    for(int i = 0; i < nums.size(); i++) {
        mpp[nums[i]]++; // Increment frequency
    }
    for(auto it : mpp) {
        if(it.second > (nums.size() / 2)) {
            return it.first;
        }
    }
    return -1;
}

// 🔵 Optimal Approach: Moore's Voting Algorithm
// Intuition: If an element appears > N/2 times, its count will outlast all other elements combined.
// We maintain a 'candidate' and a 'count'. Same element = count++, diff element = count--.
// TC: O(N) | SC: O(1)
int majorityElementOptimal(vector<int>& nums) {
    int n = nums.size();
    int cnt = 0;
    int el; 
    
    // Step 1: Find the candidate
    for (int i = 0; i < n; i++) {
        if (cnt == 0) {
            cnt = 1;
            el = nums[i];
        } else if (el == nums[i]) {
            cnt++;
        } else {
            cnt--;
        }
    }
    
    // Step 2: Verify the candidate (Strictly necessary if we aren't guaranteed a majority element exists)
    int cnt1 = 0;
    for (int i = 0; i < n; i++) {
        if (nums[i] == el) {
            cnt1++;
        }
    }
    if (cnt1 > (n / 2)) return el;
    
    return -1;
}


// ==========================================
// 3. SORT 0, 1, 2
// ==========================================

// 🟢 Brute Force: Merge Sort 
// Intuition: Divide array into halves until single elements, then merge them in sorted order.
// TC: O(N log N) | SC: O(N)
void merge(vector<int>& arr, int low, int mid, int high) {
    vector<int> temp; 
    int left = low;      
    int right = mid + 1; 

    while (left <= mid && right <= high) {
        if (arr[left] <= arr[right]) {
            temp.push_back(arr[left++]);
        } else {
            temp.push_back(arr[right++]);
        }
    }
    while (left <= mid) temp.push_back(arr[left++]);
    while (right <= high) temp.push_back(arr[right++]);
    
    for (int i = low; i <= high; i++) {
        arr[i] = temp[i - low];
    }
}

void mergeSort(vector<int>& arr, int low, int high) {
    if (low >= high) return;
    int mid = (low + high) / 2;
    mergeSort(arr, low, mid);  
    mergeSort(arr, mid + 1, high); 
    merge(arr, low, mid, high);  
}

// 🟡 Better Approach: Counting
// Intuition: Count 0s, 1s, 2s. Overwrite the array based on those counts.
// TC: O(2N) | SC: O(1)
void sortZeroOneTwoBetter(vector<int>& nums) {
    int cnt0 = 0, cnt1 = 0, cnt2 = 0;
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] == 0) cnt0++;
        else if (nums[i] == 1) cnt1++;
        else cnt2++;
    }
    for (int i = 0; i < cnt0; i++) nums[i] = 0;
    for (int i = cnt0; i < cnt0 + cnt1; i++) nums[i] = 1;
    for (int i = cnt0 + cnt1; i < nums.size(); i++) nums[i] = 2;
}

// 🔵 Optimal Approach: Dutch National Flag Algorithm
// Intuition: Maintain 3 pointers (low, mid, high) to divide array into 4 zones:
// [0...low-1] -> 0s
// [low...mid-1] -> 1s
// [mid...high] -> unsorted
// [high+1...n-1] -> 2s
// TC: O(N) | SC: O(1)
void sortZeroOneTwoOptimal(vector<int>& nums) {
    int low = 0, mid = 0, high = nums.size() - 1;
    while (mid <= high) {
        if (nums[mid] == 0) {
            swap(nums[mid], nums[low]);
            mid++; low++;
        } else if (nums[mid] == 1) {
            mid++;
        } else {
            // Swap with high, but DO NOT increment mid (we need to check the swapped element)
            swap(nums[mid], nums[high]);
            high--;
        }
    }
}
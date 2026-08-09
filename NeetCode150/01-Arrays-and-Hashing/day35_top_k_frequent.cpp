#include <bits/stdc++.h>
using namespace std;

/*
   =========================================================
   TOPIC: ARRAYS & HASHING
   PROBLEM: Top K Frequent Elements
   STATUS: COMPLETED 
   =========================================================
*/

class Solution {
public:
    /*
       APPROACH 1: Brute Force (Sorting)
       Count -> Sort EVERYTHING -> Take top K
       TC: O(N log N)
       SC: O(N)
    */
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        for(int num : nums) {
            count[num]++;
        }
        
        vector<pair<int, int>> arr;
        for(const auto &p : count) {
            arr.push_back({p.second, p.first});
        }
        
        // Sort in descending order based on frequency
        sort(arr.rbegin(), arr.rend());
        
        vector<int> res;
        for(int i = 0; i < k; i++) {
            res.push_back(arr[i].second);
        }
        return res;
    }

    /*
       APPROACH 2: Better (Min-Heap)
       Intuition:
       I need the TOP K elements
               ↓
       I don't want to sort everything
               ↓
       Use a heap of size K
               ↓
       For TOP K largest: use a MIN heap
               ↓
       When size > K: remove the smallest
       
       TC: O(N log K)
       SC: O(N)
    */
    vector<int> topKFrequentbetter(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        for(int num : nums) {
            count[num]++;
        }
        
        // Min-Heap to keep the top 'k' most frequent elements
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> heap;
        
        for(auto &entry : count) {
            heap.push({entry.second, entry.first});
            if (heap.size() > k) {
                heap.pop();
            }
        }
        
        vector<int> res;
        for(int i = 0; i < k; i++) {
            res.push_back(heap.top().second);
            heap.pop();
        }
        return res;
    }

    /*
       APPROACH 3: Optimal (Bucket Sort)
       Instead of sorting the frequencies, use an array where the index IS the frequency.
       Since the maximum possible frequency is the length of the array, we can use 
       a bucket array of size N + 1.
       
       TC: O(N)
       SC: O(N)
    */
    vector<int> topKFrequentoptimal(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        vector<vector<int>> freq(nums.size() + 1);

        for (int n : nums) {
            count[n] = 1 + count[n];
        }
        
        for (const auto& entry : count) {
            freq[entry.second].push_back(entry.first);
        }

        vector<int> res;
        // Traverse from right to left (highest frequency to lowest)
        for (int i = freq.size() - 1; i > 0; --i) {
            for (int n : freq[i]) {
                res.push_back(n);
                if (res.size() == k) {
                    return res;
                }
            }
        }
        return res;
    }
};
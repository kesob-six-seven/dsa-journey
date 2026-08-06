#include <bits/stdc++.h>
using namespace std;

/*
   =========================================================
   TOPIC: ARRAYS & HASHING
   PROBLEM 1: Two Sum
   STATUS: COMPLETED 
   =========================================================
   
   THEORY & INTUITION:
   We need to find two numbers in the array that add up to a target sum.
   
   Approach 1: Brute Force
   Use nested loops to check every possible pair.
   TC: O(N^2) | SC: O(1)
   
   Approach 2: Optimal (One-Pass Hash Map)
   As we iterate through the array, we calculate the "difference" needed 
   to reach the target (target - nums[i]). 
   We check if this difference already exists in our hash map. 
   - If it does, we found our pair!
   - If not, we add the current number and its index to the map and continue.
   
   TC: O(N) - We only traverse the array once.
   SC: O(N) - Storing at most N elements in the hash map.
*/
class TwoSumSolution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> hash;
        for(int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            
            // If the difference is in the map, we found the pair
            if (hash.find(diff) != hash.end()) {
                return {hash[diff], i};
            }
            
            // Otherwise, store the current number and its index
            hash[nums[i]] = i;
        }
        return {};
    }
};

/*
   =========================================================
   TOPIC: ARRAYS & HASHING
   PROBLEM 2: Group Anagrams
   STATUS: COMPLETED 
   =========================================================
   
   THEORY & INTUITION:
   We need to group strings together that are anagrams of each other.
   Since anagrams have the exact same characters, sorting them will result 
   in the exact same string. We can use this sorted string as a key.
   
   Approach: Hash Map with Sorting
   Use an unordered_map where the key is the sorted version of the string, 
   and the value is a vector containing all the original strings that match 
   that sorted key.
   
   TC: O(N \cdot K \log K) - Where N is the number of strings, and K is the 
       maximum length of a string (due to sorting each string).
   SC: O(N \cdot K) - To store the map and the grouped strings.
*/
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> res;
        for (const auto& s : strs) {
            vector<int> count(26, 0);
            for (char c : s) {
                count[c - 'a']++;
            }
            string key = to_string(count[0]);
            for (int i = 1; i < 26; ++i) {
                key += ',' + to_string(count[i]);
            }
            res[key].push_back(s);
        }
        vector<vector<string>> result;
        for (const auto& pair : res) {
            result.push_back(pair.second);
        }
        return result;
    }
};
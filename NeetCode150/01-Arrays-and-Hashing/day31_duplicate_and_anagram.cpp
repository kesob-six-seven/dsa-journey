#include <bits/stdc++.h>
using namespace std;

/*
   =========================================================
   TOPIC: ARRAYS & HASHING
   PROBLEM 1: Contains Duplicate
   STATUS: COMPLETED 
   =========================================================
   
   THEORY & INTUITION:
   We need to determine if any value appears at least twice in the array.
   
   Approach 1: Brute/Better (Sorting)
   Sort the array first. If there are duplicates, they will be adjacent.
   Iterate through and check if nums[i] == nums[i+1].
   TC: O(N log N) - due to sorting.
   SC: O(1) or O(N) depending on the sorting algorithm under the hood.
   
   Approach 2: Optimal (Hash Set)
   Use an unordered_set to store elements as we iterate through the array.
   If we encounter an element that is already in the set (seen.count(num) > 0), 
   we immediately return true.
   TC: O(N) - iterating through the array once. Hash set lookups are O(1) avg.
   SC: O(N) - storing up to N elements in the worst case (no duplicates).
*/
class ContainsDuplicateSolution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        for(int num : nums) {
            if (seen.count(num)) {
                return true;
            }
            seen.insert(num);
        }
        return false;
    }
};

/*
   =========================================================
   TOPIC: ARRAYS & HASHING
   PROBLEM 2: Valid Anagram
   STATUS: COMPLETED 
   =========================================================
   
   THEORY & INTUITION:
   An anagram is a word or phrase formed by rearranging the letters of a 
   different word or phrase, using all the original letters exactly once.
   
   Approach 1: Brute/Better (Sorting)
   Sort both strings and check if they are identical (s == t).
   TC: O(N log N) - due to sorting.
   SC: O(1) or O(N) depending on the language's sorting algorithm.
   
   Approach 2: Optimal (Frequency Array)
   Since the problem guarantees lowercase English letters, we can use a 
   fixed-size array of 26 to count character frequencies.
   - Increment the count for characters in string 's'.
   - Decrement the count for characters in string 't'.
   - If the strings are anagrams, every value in the array will balance out to 0.
   
   TC: O(N) - iterating through the strings of length N.
   SC: O(1) - the array size is always 26, independent of string size.
*/
class ValidAnagramSolution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }

        vector<int> count(26, 0);
        
        for (int i = 0; i < s.length(); i++) {
            count[s[i] - 'a']++; 
            count[t[i] - 'a']--; 
        }

        for (int val : count) {
            if (val != 0) {
                return false;
            }
        }
        return true;
    }
};
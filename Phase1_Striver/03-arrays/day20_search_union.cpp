#include <bits/stdc++.h>
using namespace std;

// ---------------------------------------------------------
// [Brute Force Move Zeroes / Moves all zeroes to the end using a temp array]
// Time Complexity: O(N) | Space Complexity: O(N)
// Logic: 
// - Iterate through the array and store non-zero elements in a temporary array.
// - Copy the non-zero elements back into the original array.
// - Your logic is exactly the same, no syntax errors here. Just basic brute force.
// ---------------------------------------------------------
void moveZeroes(vector<int>& nums) {
    int n = nums.size();
    int index = 0;
    vector<int> temp(n, 0);
    for(int i = 0; i < n; i++) {
        if (nums[i] != 0) {
            temp[index] = nums[i];
            index++;
        }
    }
    for (int i = 0; i < n; i++) {
        nums[i] = temp[i];
    }
}

// ---------------------------------------------------------
// [Optimal Move Zeroes / Moves zeroes in-place using two pointers]
// Time Complexity: O(N) | Space Complexity: O(1)
// Logic: 
// - Find the first zero's position with pointer 'j'.
// - Use pointer 'i' to iterate ahead and find non-zero elements.
// - Swap the non-zero element at 'i' with the zero at 'j', then increment 'j'.
// - Logic is solid, no fixes needed.
// ---------------------------------------------------------
void optimalforq1(vector<int>& nums) {
    int n = nums.size();
    int j = -1;
    for(int i = 0; i < n; i++) {
        if (nums[i] == 0) {
            j = i;
            break;
        }
    }
    if (j == -1) return;
    for (int i = j + 1; i < n; i++) {
        if (nums[i] != 0) {
            swap(nums[i], nums[j]);
            j++;
        }
    }
}

// ---------------------------------------------------------
// [Linear Search / Finds the target index by checking every element]
// Time Complexity: O(N) | Space Complexity: O(1)
// Logic: 
// - Literally just a single for-loop iterating through the array.
// - Checks if nums[i] == target and returns the index.
// - No errors.
// ---------------------------------------------------------
int linearSearch(vector<int>& nums, int target) {
    int n = nums.size();
    for(int i = 0; i < n; i++) {
        if (nums[i] == target) {
            return i;
        }
    }
    return -1;
}

// ---------------------------------------------------------
// [Brute Force Union of 2 Sorted Arrays / Uses a set to get unique elements]
// Time Complexity: O(N1 log N1 + N2 log N2) + O(N1+N2) | Space Complexity: O(N1+N2)
// Logic: 
// - Insert everything from both arrays into a `std::set` to handle duplicates.
// - Since it's an ordered set, it automatically sorts the elements.
// - Push everything from the set into a final vector.
// - I quietly added the missing closing brace `}` at the end of the function so it compiles.
// ---------------------------------------------------------
vector<int> sortedunion(vector<int> a, vector<int> b) {
    int n1 = a.size();
    int n2 = b.size();
    set<int> st;
    for(int i = 0; i < n1; i++) {
        st.insert(a[i]);
    }
    for(int i = 0; i < n2; i++) {
        st.insert(b[i]);
    }
    vector<int> temp;
    for(auto it : st) {
        temp.push_back(it);
    }
    return temp; 
}

// ---------------------------------------------------------
// [Optimal Union of 2 Sorted Arrays / Uses two pointers to merge]
// Time Complexity: O(N1+N2) | Space Complexity: O(N1+N2)
// Logic: 
// - Iterate through both arrays simultaneously using pointers 'i' and 'j'.
// - Pick the smaller element and add it to `unionArr` only if it's not a duplicate.
// - Handle remaining elements in either array once one pointer goes out of bounds.
// - Code is completely fine.
// ---------------------------------------------------------
vector<int> optimalopp(vector<int> a, vector<int> b) {
    int n1 = a.size();
    int n2 = b.size();
    int i = 0;
    int j = 0;
    vector<int> unionArr;
    while(i < n1 && j < n2) {
        if (a[i] <= b[j]) {
            if (unionArr.size() == 0 || unionArr.back() != a[i]) {
                unionArr.push_back(a[i]);
            }
            i++;
        } else {
            if (unionArr.size() == 0 || unionArr.back() != b[j]) {
                unionArr.push_back(b[j]);
            }
            j++;
        }
    }
    while(j < n2) {
        if (unionArr.size() == 0 || unionArr.back() != b[j]) {
            unionArr.push_back(b[j]);
        }
        j++;
    }
    while(i < n1) {
        if (unionArr.size() == 0 || unionArr.back() != a[i]) {
            unionArr.push_back(a[i]);
        }
        i++;
    }
    return unionArr;
}

// ---------------------------------------------------------
// [Optimal Intersection of 2 Sorted Arrays / Two pointers approach]
// Time Complexity: O(N1+N2) | Space Complexity: O(min(N1,N2))
// Logic: 
// - Compare elements at pointers 'i' and 'j'.
// - If they don't match, increment the pointer of the smaller element.
// - If they match, add to `intersectArr` (checking for duplicates) and increment both.
// - No fixes needed.
// ---------------------------------------------------------
vector<int> optimalIntersection(vector<int>& a, vector<int>& b) {
    int n1 = a.size();
    int n2 = b.size();
    int i = 0;
    int j = 0;
    vector<int> intersectArr;
    
    while (i < n1 && j < n2) {
        if (a[i] < b[j]) {
            i++;
        } 
        else if (b[j] < a[i]) {
            j++;
        } 
        else {
            if (intersectArr.empty() || intersectArr.back() != a[i]) {
                intersectArr.push_back(a[i]);
            }
            i++;
            j++;
        }
    }
    
    return intersectArr;
}

int main() {
    vector<int> arr1 = {1, 2, 2, 3, 4};
    vector<int> arr2 = {2, 2, 4, 6};
    vector<int> ans = optimalIntersection(arr1, arr2);
    
    cout << "Intersection Test: ";
    for(auto it : ans) cout << it << " ";
    cout << "\nCode runs. Stay hungry." << endl;
    return 0;
}
#include <bits/stdc++.h>
using namespace std;

/*
   =========================================================
   TOPIC: ARRAYS (Medium)
   PROBLEM: Rotate Matrix by 90 Degrees (Clockwise)
   STATUS: COMPLETED
   =========================================================
   
   THEORY & INTUITION:
   You are given an n x n 2D matrix representing an image, rotate the image 
   by 90 degrees (clockwise).
   
   Example: 
   1 2 3      7 4 1
   4 5 6  ->  8 5 2
   7 8 9      9 6 3
*/

class Solution {
public:
    // ==========================================
    // 1. BRUTE FORCE
    // ==========================================
    /*
       Intuition: Create a new dummy matrix of the same size. 
       Observe the index transformations when rotating by 90 degrees clockwise:
       The first row of the original matrix becomes the last column of the new matrix.
       Formula: rotated[j][n - i - 1] = matrix[i][j]
       
       TC: O(N^2) - Iterating through all N*N elements.
       SC: O(N^2) - Using an extra 2D array of size N*N to store the result.
    */
    vector<vector<int>> rotateClockwiseBrute(vector<vector<int>>& matrix) {
        int n = matrix.size();
        vector<vector<int>> rotated(n, vector<int>(n));
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                rotated[j][n - i - 1] = matrix[i][j];
            }
        }
        return rotated;
    }

    // ==========================================
    // 2. OPTIMAL APPROACH (In-Place)
    // ==========================================
    /*
       Intuition: We can avoid the O(N^2) extra space by doing mathematical 
       transformations on the matrix in-place.
       
       Step 1: Transpose the matrix.
               (Rows become columns: swap matrix[i][j] with matrix[j][i]).
               Make sure to only swap elements in the upper triangle (j > i) 
               to avoid double-swapping back to the original state.
       Step 2: Reverse every individual row.
       
       Visual Walkthrough:
       Original:     Transpose:     Reverse Rows (Result):
       1 2 3         1 4 7          7 4 1
       4 5 6   ->    2 5 8    ->    8 5 2
       7 8 9         3 6 9          9 6 3
       
       TC: O(N^2 / 2) for transpose + O(N^2 / 2) for reverse -> Overall O(N^2).
       SC: O(1) - No extra space used, modified in-place.
    */
    void rotateClockwiseOptimal(vector<vector<int>>& matrix) {
        int n = matrix.size();

        // Step 1: Transpose the matrix
        for (int i = 0; i < n; ++i) {
            // j starts from i + 1 to only swap the upper triangle
            for (int j = i + 1; j < n; j++) {
                swap(matrix[i][j], matrix[j][i]);
            }
        }

        // Step 2: Reverse each row
        for (int i = 0; i < n; i++) {
            reverse(matrix[i].begin(), matrix[i].end());
        }
    }
};
#include <bits/stdc++.h>
using namespace std;

/*
   =========================================================
   TOPIC: ARRAYS (Medium)
   PROBLEM: Set Matrix Zeroes
   STATUS: COMPLETED
   =========================================================
   
   THEORY & INTUITION:
   Given an m x n integer matrix matrix, if an element is 0, set its 
   entire row and column to 0's. You must do it in place.
*/

class Solution {
public:
    // ==========================================
    // 1. BRUTE FORCE
    // ==========================================
    /*
       Intuition: Traverse the matrix. Whenever we find a 0, we can't immediately 
       set the row and col to 0, because it will mess up future reads. Instead, 
       we mark the non-zero elements in that row and col with a dummy value 
       (e.g., -1). Finally, we traverse again and change all -1s to 0s.
       (Note: This only works if -1 is not a valid matrix value. If it is, this fails).
       
       TC: O(N*M) * O(N + M) + O(N*M) ~ O(N^3)
       SC: O(1)
    */
    void markRow(vector<vector<int>> &matrix, int n, int m, int i) {
        for (int j = 0; j < m; j++) {
            if (matrix[i][j] != 0) matrix[i][j] = -1;
        }
    }
    void markCol(vector<vector<int>> &matrix, int n, int m, int j) {
        for (int i = 0; i < n; i++) {
            if (matrix[i][j] != 0) matrix[i][j] = -1;
        }
    }
    void setZeroesBrute(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int m = matrix[0].size();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (matrix[i][j] == 0) {
                    markRow(matrix, n, m, i);
                    markCol(matrix, n, m, j);
                }
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (matrix[i][j] == -1) {
                    matrix[i][j] = 0;
                }
            }
        }
    }

    // ==========================================
    // 2. BETTER APPROACH
    // ==========================================
    /*
       Intuition: Instead of updating rows/cols immediately, use two separate 
       arrays (a row array and a col array) to keep track of which rows and 
       columns need to be zeroed.
       
       TC: O(2 * N*M) -> O(N*M)
       SC: O(N) + O(M) for the dummy arrays.
    */
    void setZeroesBetter(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int m = matrix[0].size();
        vector<int> row(n, 0); // row array
        vector<int> col(m, 0); // col array
        
        // Traverse to mark the dummy arrays
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (matrix[i][j] == 0) {
                    row[i] = 1;
                    col[j] = 1;
                }
            }
        }
        
        // Traverse again and set zeroes based on dummy arrays
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (row[i] || col[j]) {
                    matrix[i][j] = 0;
                }
            }
        }
    }

    // ==========================================
    // 3. OPTIMAL APPROACH
    // ==========================================
    /*
       Intuition: We can optimize the SC from O(N + M) to O(1) by using the 
       first row and first column of the matrix itself as our dummy arrays!
       - `matrix[..][0]` acts as the `row` array.
       - `matrix[0][..]` acts as the `col` array.
       Because `matrix[0][0]` overlaps for both, we use an extra variable `col0`
       to track if the first column needs to be zero.
       
       TC: O(2 * N*M) -> O(N*M)
       SC: O(1)
    */
    void setZeroesOptimal(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int m = matrix[0].size();
        int col0 = 1;

        // Step 1: Traverse and mark first row & col
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;     // mark row
                    if (j != 0)
                        matrix[0][j] = 0; // mark col
                    else
                        col0 = 0;         // overlapping case
                }
            }
        }

        // Step 2: Set matrix cells to 0 (excluding first row/col)
        for (int i = 1; i < n; i++) {
            for (int j = 1; j < m; j++) {
                if (matrix[i][j] != 0) {
                    if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                        matrix[i][j] = 0;
                    }
                }
            }
        }

        // Step 3: Handle the first row
        if (matrix[0][0] == 0) {
            for (int j = 0; j < m; j++) {
                matrix[0][j] = 0;
            }
        }
        
        // Step 4: Handle the first column
        if (col0 == 0) {
            for (int i = 0; i < n; i++) {
                matrix[i][0] = 0;
            }
        }
    }
};
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int total_row = matrix.size();
        int total_cols = matrix[0].size();
        int row = 0, col = total_cols -1;
        while(row < total_row && col > -1){
            if(matrix[row][col] == target) return true;
            else if(matrix[row][col] > target) col--;
            else if(matrix[row][col] < target) row++;
        }
        return false;
    }
};
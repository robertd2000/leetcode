class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        reverse(matrix);
        transpose(matrix);
    }

private:
    void reverse(vector<vector<int>>& matrix) {
        int left = 0;
        int right = matrix.size() - 1;

        while (left < right) {
            swap(matrix[left], matrix[right]);
            left++;
            right--;
        }
    }

    void transpose(vector<vector<int>>& matrix) {
        for (int i = 0; i < matrix.size(); i++) {
            for (int j = 0; j < i; j++) {
                swap(matrix[i][j], matrix[j][i]);
            }
        }
    }
};
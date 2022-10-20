class Solution {
public:
    void sortColors(vector<int>& nums) {
        int pivot = 1;
        int left = 0, right = nums.size() - 1;
        for(int i = 0; i <= right; i++) {
            if(nums[i] < pivot) {
                swap(nums[i], nums[left]);
                left++;
            } else if(nums[i] > pivot) {
                swap(nums[i], nums[right]);
                right--;
                i--;
            }
        }
    }
};
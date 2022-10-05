class Solution{
    public:
        bool(vector<int>& nums){
            if(nums.size() <= 1){
                return true;
            }
            int numsLength = nums.size()-1;
            int maxJump = 0;
            int i = 0;
            while(i < numsLength && maxJump >= i){
                maxJump = max(maxJump, i + nums[i]);
                if(maxJump >= numsLength){
                    return true;
                }
                i++;
            }
            return false;
        }
}
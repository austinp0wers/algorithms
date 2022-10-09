class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        if(n <2) return 0;
        int maxTravel = nums[0], jump = 1, curr=nums[0];
        for(int i = 0; i < n-1; i++){
            maxTravel = max(maxTravel, nums[i]+i);
            if(curr == i){
                jump ++;
                curr = maxTravel;
            }
        }
        return jump;
    }
};
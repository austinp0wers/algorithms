class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());

        vector <vector<int>> answer;
        for(auto interval : intervals){
            if(answer.empty() || answer.back()[1] < interval[0]){
                answer.push_back(interval);
            }
            else{
                answer.back()[1] = max(answer.back()[1], interval[1]);
            }
        }
        return answer;
    }
};
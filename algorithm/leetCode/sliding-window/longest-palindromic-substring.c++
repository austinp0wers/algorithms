class Solution {
public:
    string longestPalindrome(string s) {
        if(s.size() <= 1) return s;
        int n = s.size();
        int start = 0; int end = 0;
        int max_length= 1;

        for(int i = 0; i < n-1; i++){
            int left = i;
            int right = i;
            while(left >= 0 && right <n){
                if(s[left] == s[right]){
                    left --;
                    right ++;
                }
                else break;
            }
            int len = right - left - 1;
            if(max_length < len){
                max_length = len;
                start = left + 1;
                end = right -1;
            }
        }

        for(int i = 0; i < n-1; i++){
            int left = i;
            int right = i+1;
            while(left >= 0 && right < n){
                if(s[left] == s[right]){
                    left --;
                    right ++;
                }
                else break;
            }
            int len = right - left - 1;
            if(max_length < len){
                max_length = len;
                start = left + 1;
                end = right -1;
            }
        }
        return s.substr(start, max_length);
    }
};
// O(n2) 에 시간 복잡도를 가지며, 전형적인 sliding window를 사용 
class solution{
    public:
        int lengthOfLongestSubstring(string s) {
        unordered_map<char,int> characters;
        int left = 0;
        int right = 0;
        int answer = 0;
        while(right < s.length()){
            char r = s[right];
            characters[r]++;
            while(characters[r] > 1){
                char l = s[left];
                characters[l]--;
                left ++;
            }
            answer = max(answer, right - left +1);
            right ++;
        }
        return answer;
        }
}


// O(n) 을 가지며, Hashmap에 몇번 나왔는지가 아닌, 인덱스를 저장 해서 바로 인덱스로 넘어가는 방식.
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char,int> characters;
        int sLength = s.length(); 
        int answer = 0;
        for(int i = 0, j = 0; j < sLength; j++){
            if(characters[s[j]] > 0){
                i = max(characters[s[j]], i);
            }
            answer = max(answer, j-i +1);
            characters[s[j]] = j+1;
        }
        return answer;
    }
};
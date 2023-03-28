class Solution {
public:
    string check(int start, int end,string s){
        while (start>=0 && end<=s.size()-1 && s[start]==s[end]){
            start--;
            end++;
        }
        start++;
        end--;
    
        return s.substr(start,end-start+1);
    }



    string longestPalindrome(string s) {     
       int l=0;
        string temp1="",  temp2="", res=temp1;
        for (int i=0;i<s.size();i++){
            temp1=check(i,i,s);
            temp2=check(i,i+1,s);
            if (temp1.size()>=res.size()) res=temp1;
            if (temp2.size()>=res.size()) res=temp2;
        }
        return res;
    }
};

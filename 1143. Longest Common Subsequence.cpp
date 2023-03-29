class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int col=text1.size()+1;
        int row=text2.size()+1;
        vector <vector <int>> dp (row, vector <int> (col,0));

        for (int r=row-2;r>-1;r--){
            for (int c=col-2;c>-1;c--){
                if (text1[c]==text2[r]) dp[r][c]=1+dp[r+1][c+1];
                else dp[r][c]=max(dp[r+1][c],+dp[r][c+1]);
            }
        }
        return dp[0][0];
    }
};

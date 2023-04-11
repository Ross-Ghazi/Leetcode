/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    unordered_map <long long,long long> dic;    
    int res=0;
    void traverse (TreeNode* root, int targetSum, long long  currentSum){
        if (!root) return;
        long long val=root->val;
        currentSum=currentSum+val;
        long long  tem=currentSum-targetSum;
        res+=dic[currentSum-targetSum];          
        dic[currentSum]++;       
        traverse(root->left,targetSum,currentSum);
        traverse(root->right,targetSum,currentSum);
        dic[currentSum]--;

    }
public:
    int pathSum(TreeNode* root, int targetSum) {
      dic[0]=1;
      traverse(root,targetSum, 0);
      return res;

    }
};

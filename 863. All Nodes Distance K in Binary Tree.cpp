/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    unordered_map <TreeNode*, TreeNode*> parents;
    void traverse(TreeNode* root){
        if (!root) {return;}
        if (root->left) {parents[root->left]=root;}
        if (root->right) {parents[root->right]=root;}
        traverse(root->left);
        traverse(root->right);

    }



    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        unordered_set <TreeNode*> seen;
        traverse(root);
        int round =0;
        vector<TreeNode*> stack {target};
        seen.insert(target);

        while(round<k)
        {
          vector<TreeNode*> resTemp;  

          for (auto node:stack)
          {


              if (node->left && seen.count(node->left)==0){
                  resTemp.push_back(node->left);
                  seen.insert(node->left);
              }

                if (node->right!=NULL && seen.count(node->right)==0){
                  resTemp.push_back(node->right);
                  seen.insert(node->right);
              }

              
                if (parents.count(node)!=0 && seen.count(parents[node])==0){
                  resTemp.push_back(parents[node]);
                  seen.insert(parents[node]);
              }        
            }
 
            stack=resTemp;
            round++;
        }

        vector <int> res;
        for (auto item:stack){
            res.push_back(item->val);
        }
       return res;        
        
    }
};

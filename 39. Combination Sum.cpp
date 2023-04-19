class Solution {
    
    
public:
  unordered_map <string,  vector<vector<int>>> seen;    
    vector<vector<int>> dfs(int index,vector<int>& candidates, int target){
        vector<vector<int>>  res;
        if (target<=0){
            return res;            
        }    

        if (seen.count("s"+to_string(index)+"d"+to_string(target))!=0)    {

            return seen["s"+to_string(index)+"d"+to_string(target)];
        }
        for (int i=index;i<candidates.size();i++){
            if (candidates[i]==target) res.push_back(vector<int> {target});
            auto temp=dfs( i,candidates,target-candidates[i]);
            for (auto item :temp){
                auto newitem=item;
                newitem.push_back(candidates[i]);
                res.push_back(newitem);
            }
        }
    string  index_target {"s"+to_string(index)+"d"+to_string(target)};        
       seen.emplace(index_target ,res);
        return res; 
    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
       sort(candidates.begin(), candidates.end());
        return dfs(0,candidates,target);   
    }

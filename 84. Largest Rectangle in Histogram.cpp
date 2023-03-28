class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        vector <vector<int>> stack;
        vector <int> vec;
        int index, val,start=0,res=0, temp=0;
        heights.push_back(0);
        for (int i=0;i<heights.size();i++){
            start=i;
            while (stack.size()>0 && stack.back()[1]>heights[i]){
                index=stack.back()[0];
                val=stack.back()[1];
                res=max(res,val*(i-index));
                start=index;
                stack.pop_back();
            }
            stack.push_back(vector <int> {start, heights[i]});

           
        }
        return res;      
    }
};

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int res=nums[0];
        int currentSum=0;
        for (auto n:nums){
            currentSum=max(currentSum+n,n);
            res=max(res,currentSum);           

        }
        return res;

    }
};

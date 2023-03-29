class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l=0;
        int r=nums.size()-1;
        int mid;
        while (true){
            if (l>r) return -1;
            mid=l+(r-l)/2;
            if (nums[mid]==target) return mid;
            if ((nums[mid]>=nums[0])==(target>=nums[0])){
                cout<<"int"<<endl;
                if (nums[mid]>target) r=mid-1;
                else l=mid+1;
                
            } 
            else {
                if (target>=nums[0]) r=mid-1;
                else  l=mid+1;
            }
        
        }
    }
};

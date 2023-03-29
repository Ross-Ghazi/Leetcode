class Solution {
public:
  vector<vector<int>> threeSum(vector<int> &nums) {
    int l, r, total;
    vector<vector<int>> res;
    vector<int> tmp;
    sort(nums.begin(), nums.end());
    for (int i; i < nums.size() - 2; i++) {
      if (i > 0 && nums[i - 1] == nums[i])
        continue;
      l = i + 1;
      r = nums.size() - 1;
      while (l < r) {
        total = nums[i] + nums[r] + nums[l];
        if (total == 0) {
          res.push_back(vector<int>{nums[i], nums[r], nums[l]});
          while (l < r && nums[l] == nums[l + 1])
            ++l;
          ++l;
        } else if (total > 0) {
          r--;
        } else {
          l++;
        }
      }
    }

    return res;
  }
};

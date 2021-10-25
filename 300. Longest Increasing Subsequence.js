var lengthOfLIS = function(nums) {
    let dp=[]
    nums.forEach((n,i)=>
    {
        let temp=1
        for (let j=0;j<i;j++)  if (nums[i]>nums[j]) temp=Math.max(temp, dp[j]+1)
        dp.push(temp)
  
        
        
    })         

    return Math.max(...dp)
    

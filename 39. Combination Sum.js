var combinationSum = function(candidates, target) {
    let res=[]
        function dfs(path, currentSum,index){

            if (currentSum==target)  return res.push([...path])                        
            if (currentSum>target) return             

            for (let i=index;i<candidates.length;++i )
                {   path.push(candidates[i])
                    dfs (path,currentSum+candidates[i], i)
                    path.pop()                 
                }

        }
    
    dfs([],0,0)
    
    return res
    
};



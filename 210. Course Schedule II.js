var findOrder = function(numCourses, prerequisites) {
    preq=new Map
    for ([a,b] of prerequisites){
        preq.has(a)? preq.get(a).push(b) : preq.set(a,[b])                
    }
    seen=new Set
    loop=new Set
    let flag=true
    
    function dfs(i) {
        if (loop.has(i)) {
            flag=false           
            return
        }

        if (seen.has(i)) return        
        seen.add(i)        
        loop.add(i)      
        
        let pre=preq.get(i)        
        if (pre)  {for (c of pre) dfs(c)}
        loop.delete(i)              
        path.push(i) 
        return 
        
    
    }    
    
    path=[]
    for(let i=0;i<numCourses;i++){        
       dfs(i)        
    }

return (flag ? path :[])
};

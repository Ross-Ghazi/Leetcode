var leastInterval = function(tasks, n) {
    let freq= new Map()
    for (item of tasks){
    freq.has(item)? freq.set(item,freq.get(item)+1) : freq.set(item,1)
    }
    
    let maxFreq=0
    for (val of freq.values())
       { maxFreq=Math.max(maxFreq,val)}
    
    let counter=0
    for (val of freq.values())
       {maxFreq==val && (++counter)}
 
    let res=tasks.length
    
    res=Math.max (res, (maxFreq-1)*(n+1)+counter)
    
    return res
        
    
    
    
    
    
    
};

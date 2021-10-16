var removeStones = function(stones) {
   const dfs=(i)=>{
         let X=stones[i][0]
         let Y=stones[i][1]  
   
   if (seen.has(i)) {return}
   seen.add(i) 
   let tempArr=x.get(X)     
   for (index of tempArr)
        {dfs(index) } 
   tempArr=y.get(Y) 
   for (index of tempArr)
        {dfs(index) }  
         return 
       
   }
    
    
    
    
    x=new Map()
    y=new Map()    
    for (let i=0;i<stones.length;++i)
       { 
       
        let stone=stones[i]
        let X=stone[0]
        let Y=stone[1] 
        x.has(X) ? (x.get(X).push(i)):  x.set(X,[i])
        y.has(Y) ? (y.get(Y).push(i)):  y.set(Y,[i])
      
       }
   let count=0; 
   let seen= new Set()
   for (let i=0;i<stones.length;++i)
       { 
           
       if (!seen.has(i)){
           ++count      
           dfs(i)          
           
           
       }
           
       }

 return (stones.length-count)
    
};

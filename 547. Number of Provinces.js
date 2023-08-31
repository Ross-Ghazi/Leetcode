/**
 * @param {number[][]} isConnected
 * @return {number}
 */
var findCircleNum = function(isConnected) {
    let res=0;
    let seen=new Set();
    let n =isConnected.length;
    
  const check=(index)=>{
        if (seen.has(index)) {return;}
        seen.add(index);
        for (let i=0;i<n;i+=1)
        {
            if (isConnected[i][index]==1){
                check(i);
            }
        }
    }

    for (let i=0;i<n;i+=1){
        if (!seen.has(i)){
            res+=1;
            check(i);
        }
    } 
    return res;    
};

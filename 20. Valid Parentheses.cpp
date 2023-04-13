class Solution {
public:
    bool isValid(string s) {
        vector <char> opening;
        string openString {"({["};
        for  (auto c:s){
            if (openString.find(c)!=-1){
                opening.push_back(c);
            }
            else{
                if (opening.size()==0) return false;
                if (
                    (c==')' && opening.back()=='(') 
                ||  (c=='}' && opening.back()=='{')
                ||  (c==']' && opening.back()=='[')
                )
                {opening.pop_back();}
                else {return false;}
            }      
        }
        if (opening.size()>0) return false;
        return true;
    }
};

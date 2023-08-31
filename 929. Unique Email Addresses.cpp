class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
    unordered_set<string> clearedEmails;
    for (auto& email:emails){
        string local=email.substr(0,email.find('@'));
        string domain =email.substr(email.find('@'));
        local=local.substr(0,email.find('+'));
        string newLocal="";
        for (auto c:local){
            if (c!='.') newLocal+=c;
        }

        clearedEmails.insert(newLocal+domain);        
     }

    return clearedEmails.size();
    }
};

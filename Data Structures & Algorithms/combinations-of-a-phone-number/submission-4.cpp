class Solution {
public: 
    unordered_map<char,string> D = {
        {'2',"abc"},
        {'3',"def"},
        {'4',"ghi"},
        {'5',"jkl"},
        {'6',"mno"},
        {'7',"pqrs"},
        {'8',"tuv"},
        {'9',"wxyz"}
    };
    vector<string> res ={};
    string cur;
    void dfs(string digits,int i,int k ){
        if(k== D[digits[i]].size()) return ;
        cur+= D[digits[i]].at(k);
        if(i==digits.size()-1){
            res.push_back(cur);
            cur.pop_back();
            dfs(digits,i,k+1);
        }
        else{
            dfs(digits,i+1,0);
            cur.pop_back();
            dfs(digits,i,k+1);
        }
    }
    vector<string> letterCombinations(string digits) {
        vector<string> x ={};
        if( digits.size() ==0) return x ;
        dfs(digits,0,0);
        return res;
    }
};

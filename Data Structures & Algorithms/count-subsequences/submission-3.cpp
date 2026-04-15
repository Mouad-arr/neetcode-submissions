class Solution {
public:
    int c=0;
    vector<char> cur ={};
    void dfs(int i ,int j , string s , string t){
        if(i>= s.size() || j>=t.size()) return ;
        if(s[i]==t[j]){
            this->cur.push_back(t[i]);
            if(this->cur.size()==t.size()) this->c++;
            else dfs(i+1,j+1,s,t);
            this->cur.pop_back();
            dfs(i+1,j,s,t);
        }
        else dfs(i+1,j,s,t);
    }
    int numDistinct(string s, string t) {
        dfs(0,0,s,t);
        return c;
    }
};

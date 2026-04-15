class TrieNode{
public :
    unordered_map<char, TrieNode*> children;
    bool endOfWord ;
    TrieNode(){
        this->endOfWord=false;
    }
};
class WordDictionary {
public:
    TrieNode* root ; 
    WordDictionary() {
        root = new TrieNode();
    }
    
    void addWord(string word) {
        TrieNode* cur = root ;
        for(char c : word){
            if (cur->children.find(c) == cur->children.end()){
                cur->children[c]= new TrieNode();
            }
            cur=cur->children[c];
        }
        cur->endOfWord= true ;
    }
    bool dfs(int j , TrieNode* root, string word){
        TrieNode* cur = root ;
        for(int i =j ; i<word.size();i++){
            if(word[i]=='.'){
                for(auto const& [key, child] : cur->children){
                    if(dfs(i+1,child,word)) return true;
                }
                return false;
            }
            else{
                if (cur->children.find(word[i]) == cur->children.end()) return false;
                cur=cur->children[word[i]];
            }
        }
        return cur->endOfWord ;
    }
    bool search(string word) {
        return dfs(0,this->root,word);
    }
};

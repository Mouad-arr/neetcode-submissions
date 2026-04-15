class Solution {
public:
    bool isTrue(string word, string w){
        int diff=0;
        for(int i=0;i<word.size();i++){
            if(word.at(i)!=w.at(i))
               diff++;
        }
        return diff==1 ;
    }
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_map<string,unordered_set<string>> d ;
        for(string word:wordList){
            if(isTrue(word,beginWord)){
                d[beginWord].insert(word);
            }
        }
        for(string word:wordList){
            for(string w : wordList){
                if(w == word)
                   continue;
                if(isTrue(word,w))
                  d[word].insert(w);
            }
        }
        queue<pair<string,int>> q ;
        q.push({beginWord,1});
        unordered_set<string> visited;
        visited.insert(beginWord);
        while(!q.empty()){
            auto [curr, dist] = q.front();
            q.pop();
            if(curr == endWord)
              return dist;
            if(d.find(curr) != d.end()){
                for(string nei : d[curr]){
                    if(visited.find(nei) == visited.end()){
                       visited.insert(nei);
                       q.push({nei,dist+1});
                    }
                }
            }
        }
        return 0 ;
    }
};

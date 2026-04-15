class Solution {
    /**
     * @param {string} beginWord
     * @param {string} endWord
     * @param {string[]} wordList
     * @return {number}
     */
    isTrue(word,w){
        let diff=0;
        for(let i=0;i<word.length ;i++){
            if(word[i]!=w[i]) diff++;
        }
        return diff===1;
    }
    ladderLength(beginWord, endWord, wordList) {
        if (!wordList.includes(endWord)) return 0;
        const d= new Map();
        const allWords = [beginWord, ...wordList];
        for(let word of allWords){
            d.set(word, []);
            for(let w of wordList){
                if(this.isTrue(word,w))
                 d.get(word).push(w);
            }
        }
        const q =[[beginWord,1]];
        const visited = new Set();
        visited.add(beginWord);
        while(q.length!=0){
            const [curr,dist] = q.shift();
            if(curr==endWord)
               return dist;
            for(let nei of (d.get(curr) || [])){
                if(!visited.has(nei)){
                    visited.add(nei);
                    q.push([nei,dist+1]);
                }
            }
        }
        return 0;
    }
}
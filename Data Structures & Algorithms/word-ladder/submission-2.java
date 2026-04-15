class Solution {
    public boolean isTrue(String word, String w){
        int diff=0;
        for(int i=0;i<word.length();i++){
            if(word.charAt(i)!=w.charAt(i))
              diff++;
        }
        return diff==1  ;
    }
    record Pair(String word, int dist) {}
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        if(!wordList.contains(endWord)) return 0;
        Map<String,Set<String>> d = new HashMap<>();

        for(String word : wordList){
            if(isTrue(word,beginWord)){
                d.putIfAbsent(beginWord,new HashSet<>());
                d.get(beginWord).add(word);
            }
        }
        for(String word : wordList){
            for(String w : wordList){
                if(w.equals(word)) continue ;
                if(isTrue(w,word)){
                   d.putIfAbsent(word,new HashSet<>());
                   d.get(word).add(w);
                }
            }
        }
        Queue<Pair> q = new ArrayDeque<>();
        q.offer(new Pair(beginWord,1));
        Set<String> visited = new HashSet<>();
        visited.add(beginWord);
        while (q.size()>0){
            Pair current = q.poll();
            String curr = current.word;
            int dist = current.dist ;
            if(curr.equals(endWord))
                return dist ;
            if (d.get(curr) != null) {
                for(String nei : d.get(curr)){
                    if(!visited.contains(nei)){
                       visited.add(nei);
                       q.offer(new Pair(nei,dist+1));
                    }
                }
            }
        }
        return 0;
    }
}
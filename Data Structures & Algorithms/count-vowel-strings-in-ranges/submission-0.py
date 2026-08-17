class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        wordsC = [0]*len(words)
        vowels={'a','e','i','o','u'}
        for i in range(len(words)) :
            if words[i][0] in vowels and words[i][-1] in vowels :
                wordsC[i]=1
        ans=[]
        for q in queries :
            ans.append(wordsC[q[0]:q[1]+1].count(1))
        return ans
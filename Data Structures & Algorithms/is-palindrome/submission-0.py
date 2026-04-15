class Solution:
    def isPalindrome(self, s: str) -> bool:
        S = [num.lower() for num in list(s) if num.isalnum()]
        for i in range(len(S)//2) :
            if S[i] != S[len(S)-1-i] :
                return False
        return True
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        arr = [0] * (n + 1)

        for start, end, direction in shifts:
            shif = 1 if direction == 1 else -1

            arr[start] += shif
            arr[end + 1] -= shif
        newstr=""
        current=0
        for i in range(n):
            current+=arr[i]
            newstr += chr(ord('a') + (ord(s[i]) - ord('a') + current) % 26)
        return newstr

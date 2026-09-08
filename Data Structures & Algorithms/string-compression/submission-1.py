class Solution:
    def compress(self, chars: List[str]) -> int:       
        i = 0
        write = 0

        while i < len(chars):
            c = chars[i]
            j = i

            while j < len(chars) and chars[j] == c:
                j += 1

            chars[write] = c
            write += 1

            count = j - i

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

            i = j

        return write
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        n = len(words)
        i = 0

        while i < n:
            line = []
            line_length = 0

            while i < n:
                new_length = line_length + len(words[i])

                if line:
                    new_length += len(line)

                if new_length > maxWidth:
                    break

                line.append(words[i])
                line_length += len(words[i])
                i += 1

            if i == n:
                text = ' '.join(line)
                res.append(text + ' ' * (maxWidth - len(text)))
                break

            gaps = len(line) - 1

            if gaps == 0:
                res.append(line[0] + ' ' * (maxWidth - len(line[0])))
                continue

            extra_spaces = maxWidth - line_length

            base = extra_spaces // gaps
            remainder = extra_spaces % gaps

            text = ""

            for j in range(gaps):
                text += line[j]
                text += ' ' * (base + (1 if j < remainder else 0))

            text += line[-1]

            res.append(text)

        return res
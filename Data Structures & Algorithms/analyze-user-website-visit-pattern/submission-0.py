class Solution:
    def mostVisitedPattern(
        self,
        username: List[str],
        timestamp: List[int],
        website: List[str]
    ) -> List[str]:
        users = {}

        for i in range(len(username)):
            users.setdefault(username[i], []).append(
                (timestamp[i], website[i])
            )

        pattern_count = {}

        for user in users:

            users[user].sort()

            sites = [site for _, site in users[user]]

            n = len(sites)
            if n < 3:
                continue

            user_patterns = set()

            for i in range(n):
                for j in range(i + 1, n):
                    for k in range(j + 1, n):
                        pattern = (sites[i], sites[j], sites[k])
                        user_patterns.add(pattern)

            for pattern in user_patterns:
                pattern_count[pattern] = pattern_count.get(pattern, 0) + 1

        best = sorted(
            pattern_count.items(),
            key=lambda x: (-x[1], x[0])
        )

        return list(best[0][0])
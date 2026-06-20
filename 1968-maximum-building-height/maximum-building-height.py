from typing import List

class Solution:
    def maxBuilding(self, n: int, r: List[List[int]]) -> int:
        r.append([1, 0])
        r.sort()

        m = len(r)

        for i in range(1, m):
            pos1, h1 = r[i - 1]
            pos2, h2 = r[i]

            r[i][1] = min(
                h2,
                h1 + (pos2 - pos1)
            )

        for i in range(m - 2, -1, -1):
            pos1, h1 = r[i]
            pos2, h2 = r[i + 1]

            r[i][1] = min(
                r[i][1],
                h2 + (pos2 - pos1)
            )

        ans = 0

        for i in range(1, m):
            p1, h1 = r[i - 1]
            p2, h2 = r[i]

            d = p2 - p1

            ans = max(
                ans,
                (h1 + h2 + d) // 2
            )

        last_pos, last_h = r[-1]

        ans = max(
            ans,
            last_h + (n - last_pos)
        )

        return ans
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l,r = 0,len(people)-1
        res = []

        while l <= r:
            if people[r] + people[l] <= limit:
                res.append((people[l],people[r]))
                r -= 1
                l += 1
            else:
                res.append((people[r]))
                r -= 1

        return len(res)
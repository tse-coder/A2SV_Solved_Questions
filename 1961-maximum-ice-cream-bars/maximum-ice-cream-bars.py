class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        _max = max(costs)
        counts = [0]*(_max+1)
        for cost in costs:
            counts[cost] += 1
        
        for i in range(1,_max+1):
            counts[i] += counts[i-1]
        s = [0]*len(costs)

        for cost in costs[::-1]:
            counts[cost] -= 1
            s[counts[cost]] = cost
        res = 0
        curr_coins = 0
        for coin in s:
            if curr_coins + coin <= coins:
                curr_coins += coin
                res += 1
            else:
                break
        return res


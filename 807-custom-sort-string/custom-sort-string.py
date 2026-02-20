class Solution:
    def customSortString(self, order: str, s: str) -> str:
        common = set(order) & set(s)
        res = []
        miss = []
        initial_cnt = Counter(s)
        pro = set()
        for char in order:
            if char in initial_cnt:
                res += [char] * initial_cnt[char]
            pro.add(char)
            
        for c in s:
            if c not in pro:
                miss.append(c)
        # print(res)
        # for char in s:
        #     if char not in visited_cnt:
        #         for _ in range(initial_cnt[char]):
        #             res += char
        #         visited_cnt[char] = initial_cnt[char]
        #     elif visited_cnt[char] < initial_cnt[char]:
        #         diff = initial_cnt[char] - visited_cnt[char]
        #         for _ in range(diff):
        #             res += char
        #         visited_cnt[char]+= diff
        res.extend(miss)
        
        return "".join(res)
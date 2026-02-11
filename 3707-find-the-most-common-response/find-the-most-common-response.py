class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        set_list = []
        for response in responses:
            set_list.append(list(set(response)))
        
        val_counter = {}
        for response in set_list:
            for val in response:
                if val in val_counter:
                    val_counter[val] += 1
                else:
                    val_counter[val] = 1
        max_strs = []
        max_count = 0
        for val in val_counter:
            if val_counter[val] > max_count:
                max_count = val_counter[val]
        for val in val_counter:
            if val_counter[val] == max_count:
                max_strs.append(val)
        
        return sorted(max_strs)[0]
        
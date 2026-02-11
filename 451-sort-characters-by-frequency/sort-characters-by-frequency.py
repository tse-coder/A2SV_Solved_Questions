class Solution:
    def frequencySort(self, s: str) -> str:
        vals = list(s)
        vals_counter = Counter(vals)
        val_count_list = []
        for val in vals_counter:
            val_count_list.append([vals_counter[val],val])
        val_count_list.sort()
        res = ""
        for val_count in val_count_list[::-1]:
            res+=val_count[1]*val_count[0]
        return res
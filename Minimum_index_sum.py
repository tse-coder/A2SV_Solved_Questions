class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ref = {}
        indexes = []
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    if i+j in ref:
                        ref[i+j].append(list1[i])
                    else:
                        ref[i+j] = [list1[i]]
                    indexes.append(i+j)
        return ref[min(indexes)]


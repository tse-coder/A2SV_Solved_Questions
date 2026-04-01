class Solution:
    def rever(self,string,start,end):
        while start < end:
            string[start],string[end] = string[end],string[start]
            end -= 1
            start += 1

    def smallestNumber(self, pattern: str) -> str:
        l = len(pattern) 
        ans = [str(i) for i in range(1,l+2)]
        j = 0
        while j < l:
            if pattern[j] == "I":
                j += 1
            else:
                start = j
                while j < l and pattern[j] == "D":
                    j += 1
                self.rever(ans,start,j)
        return "".join(ans)


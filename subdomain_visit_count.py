class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domDict = {}
        for ctp in cpdomains:
            vals = ctp.split(" ")
            count = int(vals[0])
            doms = vals[1].split(".")
            dom = doms[-1]
            if dom in domDict:
                domDict[dom] += count
            else:
                domDict[dom] = count
            
            for i in range(len(doms)-2,-1,-1):
                dom = doms[i] + "." + dom
                if dom in domDict:
                    domDict[dom] += count
                else:
                    domDict[dom] = count
        res = []
        for val in domDict:
            curr = str(domDict[val])+ " " + val
            res.append(curr)
        return res
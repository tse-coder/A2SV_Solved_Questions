class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        out  = []
        blockCom = False
        temp = ""
        for i in range(len(source)):
            strr = source[i]
            right = 0
            while right < len(strr):
                if strr[right:right+2] == "/*" and not blockCom:
                    blockCom = True
                    right += 1
                elif strr[right:right+2] == "*/" and blockCom:
                    blockCom = False
                    right += 1
                elif not blockCom and strr[right:right+2] == "//":
                    break
                elif not blockCom:
                    temp += strr[right]
                right += 1
            if not blockCom and temp != "":
                out.append(temp)
                temp = ""
        return out
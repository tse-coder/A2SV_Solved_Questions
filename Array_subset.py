#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        valCountA = {}
        for val in a:
            if val not in valCountA:
                valCountA[val] = 0
            valCountA[val] += 1
        valCountB = {}
        for val in b:
            if val not in valCountB:
                valCountB[val] = 0
            valCountB[val] += 1
        for val in valCountB:
            if val not in valCountA or valCountB[val] > valCountA[val]:
                return False
        return True
        
        
    
    
    
    

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedL = {}
        index =0
        newlist = []
        for item in strs:
            x = str(sorted(item))
            if x not in sortedL:
                sortedL[x] = [index]
            else:
                sortedL[x].append(index)
            index+=1
        
        for key in sortedL:
            temp = []
            y = sortedL[key]
            print (y)
            for x in y:
                temp.append(strs[x])
            newlist.append(temp)
        
        return newlist
class Solution:
    def isValidSudoku(self, bd: List[List[str]]) -> bool:
        mp1 = [defaultdict(int) for _ in range(9)]
        mp2 = [defaultdict(int) for _ in range(9)]      #mp2[i] gives us a map
        mp3 = [defaultdict(int) for _ in range(9)]      #mp2[i][val] means "map2[i] map me "val" add kardo
        for i in range(len(bd)):
            for j in range(len(bd[0])):
                if bd[i][j]==".":
                    continue
                else:
                    val = bd[i][j]
                    box_id = i//3*3 + j//3
                    if val in mp1[i].keys() or val in mp2[j].keys() or val in mp3[box_id].keys():
                        return False
                    mp1[i][val]+=1
                    mp2[j][val]+=1
                    mp3[box_id][val]+=1
                    
        return True
                    


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 
        r=len(numbers) -1
        while l<r:
            if numbers[l]+numbers[r] < target:
                l+=1
                print("l=",l)
            elif numbers[l]+numbers[r] > target:
                r-=1
                print("r=",r)
            else :
                print(l,r)
                return [l+1,r+1]
                break

        
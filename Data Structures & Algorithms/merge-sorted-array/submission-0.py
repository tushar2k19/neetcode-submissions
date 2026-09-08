class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j,k = (m-1),(n-1),(m+n-1)
        print (i,j,k)
        while k>=0:
            print(k)
            if i<0 or j<0:
                break;
            if nums1[i]>=nums2[j]:
                nums1[k] = nums1[i]
                i-=1
            else:
                nums1[k] = nums2[j]
                j-=1
            k-=1
        print (i,j,k)
        while i>=0 and k>=0:
            nums1[k] = nums1[i]
            i-=1
            k-=1
        while j>=0 and k>=0:
            print("jere")
            nums1[k] = nums2[j]
            j-=1
            k-=1
        print (i,j,k)
        

        
    
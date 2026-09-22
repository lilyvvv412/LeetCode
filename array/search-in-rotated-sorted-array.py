#i及右边>=target(ans in blue);i左边<target(red)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def isBlue(i: int)->bool: #i:mid
            end=nums[-1]
            if nums[i]>end:
                return target>end and nums[i]>=target
            else: return target>end or nums[i]>=target
        left=-1
        right=len(nums)
        while left+1<right:
            mid=(left+right)//2
            if isBlue(mid): right=mid
            else: left=mid
        if right==len(nums) or nums[right]!=target: return -1
        return right
#non-decreasing
def lower_bound(nums: List[int],target: int)->int:
    left=0
    right=len(nums)-1 #[]
    while left<=right:
        mid=(left+right)//2 #下取整
        if nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return left
def lower_bound2(nums: List[int],target: int)->int:
    left=0
    right=len(nums) #[)
    while left<right:
        mid=(left+right)//2 #下取整
        if nums[mid]<target:
            left=mid+1
        else:
            right=mid
    return left #or right
def lower_bound3(nums: List[int],target: int)->int:
    left=-1
    right=len(nums)-1 #()
    while left+1<right:
        mid=(left+right)//2 #下取整
        if nums[mid]<target:
            left=mid
        else:
            right=mid
    return right

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start=lower_bound(nums,target)
        if start==len(nums) or nums[start]!=target:
            return[-1,-1]
        end=lower_bound(nums,target+1)-1
        return [start,end]
#time: O(log n) space:O(1)
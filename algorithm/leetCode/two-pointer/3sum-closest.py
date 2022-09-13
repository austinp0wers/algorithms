class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < target:
                    left += 1
                    if closest < target:
                        closest = max(closest, total)
                    else:
                        if closest-target > target - total:
                            closest = total
                elif total > target:
                    right -= 1
                    if closest > target:
                        closest = min(closest, total)
                    else:
                        if target -closest > total-target:
                            closest = total
                else:
                    return total
        return closest
                
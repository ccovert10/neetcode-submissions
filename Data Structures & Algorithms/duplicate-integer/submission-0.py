class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num = sorted(nums)
        rear = 0
        front = 1
        while front < len(num):
            if num[rear] == num[front]:
                return True
            rear += 1
            front += 1
        return False
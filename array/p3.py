# p3.py
# Given an array arr of N integers. Find the contiguous sub-array with maximum sum.

class MaximumSubSum:

    def __init__(self, arr=list):
        self.arr = arr

    def max_sub_sum(self):
        cur_sum = 0
        max_sum = 0
        for i in range( len(self.arr)):
            cur_sum += self.arr[i]
            if cur_sum > max_sum:
                max_sum = cur_sum
            else:
                continue
        if max_sum > 0:
            return max_sum
        else:
            return -1
            
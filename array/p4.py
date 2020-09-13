# p4.py
# Given an array C of size N-1 and given that there are numbers from 1 to N with one element missing, the missing number is to be found.

class MissingNumber:
    def __init__(self, arr=list):

        self.arr = arr
    
    def one_missing_number(self):
        arr_sum = sum(self.arr)
        arr_len = self.arr.__len__()+1
        natural_sum = (arr_len * (arr_len +1)) / 2
        return natural_sum - arr_sum

    def multiple_missing_number(self, arr_len=int):
        complete_arr = set(range(1, arr_len))
        diff  = complete_arr.difference(self.arr)
        return diff
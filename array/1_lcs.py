# lcs.py
import unittest


class LCS:

    def __init__(self, seq=list):
        self.seq = seq
    
    def __repr__(self):
        return f"input sequence: {self.seq}"


    def lcs(self):
        data = self.seq.copy() # save a copy of data
        data.sort() # sort the list
        res = [y-x for x,y in zip(data, data[1:])] # substract the values from consecutive elements 
        if res.count(1) == 0: # count the ones in the result 
            return 0 # no consecutive numbers have a difference of one so no consecutive numbers
        else: 
            return(res.count(1)+1) # no of consecutive numbers = no. of ones + 1

if __name__ == '__main__':
    test_case =  int(input('no. of test cases: '))
    seq_len = int(input("sequence length: "))
    seq = []
    for val in range(1,seq_len+1):
        element = int(input(f"enter {val} element: "))
        seq.append(element)
    lcs = LCS(seq)
    print("No of continous elements: ", lcs.lcs())
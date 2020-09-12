# lcs.py

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
            count = 0
            last_max_count = 0
            for i in range(res.count(1)+1):
                if res[i] == 1:
                    count += 1
                    last_max_count = count
                else:
                    last_max_count = count
                    count = 0

            return(last_max_count+1) # no of consecutive numbers = no. of ones + 1

if __name__ == '__main__':
    test_case =  int(input('no. of test cases: '))
    seq_len = int(input("sequence length: "))
    seq = []
    while test_case != 0:
        for val in range(1,seq_len+1):
            element = int(input(f"enter {val} element of arr{test_case}: "))
            seq.append(element)
        test_case -= 1
    lcs = LCS(seq)
    print("No of continous elements: ", lcs.lcs())
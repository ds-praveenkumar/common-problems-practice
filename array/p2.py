# p2.py

# Given an unsorted array A of size N of non-negative integers, 
# find a continuous sub-array which adds to a given number S.

class SubArraySum:

    def __init__(self, arr=list, sum=int):
        self.arr = arr
        self.sum = sum

    def sub_array_sum(self):
        for i in range(self.arr.__len__()):
            for j in range(self.arr.__len__()):
                j = i+1
                if self.arr.__contains__(self.sum - self.arr[i]):
                    return i,self.arr.index(self.sum - self.arr[i])
                else:
                    return -1
                

    
if __name__ == "__main__":
    test_case = int(input("no. of test cases: "))
    num_elements =  int(input("num of array elements: "))
    array_sum = int(input("sum: "))
    arr = []
    while test_case != 0:
        for val in range(1,1+num_elements):
            element = element = int(input(f"enter {val} element of arr{test_case}: "))
            arr.append(element)
        test_case -= 1
    sas = SubArraySum(arr, array_sum)
    res = sas.sub_array_sum()
    print(res)
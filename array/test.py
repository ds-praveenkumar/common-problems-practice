import unittest

from p1_lcs import LCS
from p2 import SubArraySum
from p3 import MaximumSubSum
from p4 import MissingNumber


class TestLCS(unittest.TestCase):

    def test_lcs_case1(self):
        seq = [34, 7, 90, 9, 8]
        lcs = LCS(seq)
        res = lcs.lcs()
        self.assertEqual(res, 3)

    def test_lcs_case2(self):
        seq = [34, 7, 90, 9, 8, 10]
        lcs = LCS(seq)
        res = lcs.lcs()
        self.assertEqual(res, 4)

    def test_lcs_case3(self):
        seq = [34, 7, 90, 19, 38, 10]
        lcs = LCS(seq)
        res = lcs.lcs()
        self.assertEqual(res, 0)
    
    def test_lcs_case4(self):
        seq = [7, 7, 7, 7, 7, 7]
        lcs = LCS(seq)
        res = lcs.lcs()
        self.assertEqual(res, 0)

    def test_lcs_case5(self):
        seq = [7, 17, 8, 18, 9, 19, 20]
        lcs = LCS(seq)
        res = lcs.lcs()

        self.assertEqual(res, 4)

    def test_lcs_case6(self):
        seq = [7,8,1,2]
        lcs = LCS(seq)
        res = lcs.lcs()
        self.assertEqual(res, 2)

    def test_p2_case1(self):
        seq = [1,2,4,4, 6, 90]
        sum = 7
        p2 = SubArraySum(arr=seq, sum=sum)
        res = p2.sub_array_sum()
        self.assertEqual(res, (0, 4))

    def test_p2_case2(self):
        seq = [1,2,4,4, 9,8]
        sum = 89
        p2 = SubArraySum(arr=seq, sum=sum)
        res = p2.sub_array_sum()
        self.assertEqual(res, -1)
    
    def test_p3_case1(self):
        seq = [1,2,4,4]
        p3 = MaximumSubSum(arr=seq)
        res = p3.max_sub_sum()
        self.assertEqual(res, 11)

    def test_p3_case2(self):
            seq = [-1,2,4,4]
            p3 = MaximumSubSum(arr=seq)
            res = p3.max_sub_sum()
            self.assertEqual(res, 9)

    def test_p3_case3(self):
            seq = [-1,-2,-4,-4]  
            p3 = MaximumSubSum(arr=seq)
            res = p3.max_sub_sum()
            self.assertEqual(res, -1)

    def test_p4_case1(self):
            seq = [1,2,4,5]  
            p3 = MissingNumber(arr=seq)
            res = p3.one_missing_number()
            self.assertEqual(res, 3)

    def test_p4_case2(self):
            seq = [1,2,6,5,4]  
            p3 = MissingNumber(arr=seq)
            res = p3.one_missing_number()
            self.assertEqual(res, 3)
    
    def test_p4_case3(self):
            seq = [1,2,6,5]  
            p3 = MissingNumber(arr=seq)
            res = p3.multiple_missing_number(6)
            self.assertEqual(res, {3,4})


if __name__ == '__main__':
    unittest.main()
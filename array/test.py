import unittest

from p1_lcs import LCS


class TestLCS(unittest.TestCase):

    def test_lcs_case1(self):
        seq = [34, 7, 90, 9, 8]
        lcs = LCS(seq)
        res = lcs.lcs()
        print(res)
        self.assertEqual(res, 3)

    def test_lcs_case2(self):
        seq = [34, 7, 90, 9, 8, 10]
        lcs = LCS(seq)
        res = lcs.lcs()
        print(res)
        self.assertEqual(res, 4)

    def test_lcs_case3(self):
        seq = [34, 7, 90, 19, 38, 10]
        lcs = LCS(seq)
        res = lcs.lcs()
        print(res)
        self.assertEqual(res, 0)
    
    def test_lcs_case4(self):
        seq = [7, 7, 7, 7, 7, 7]
        lcs = LCS(seq)
        res = lcs.lcs()
        print(res)
        self.assertEqual(res, 0)

    def test_lcs_case5(self):
        seq = [7, 17, 8, 18, 9, 19, 20]
        lcs = LCS(seq)
        res = lcs.lcs()
        print(res)
        self.assertEqual(res, 4)

    def test_lcs_case6(self):
        seq = [7,8,1,2]
        lcs = LCS(seq)
        res = lcs.lcs()
        print(res)
        self.assertEqual(res, 2)

if __name__ == '__main__':
    unittest.main()
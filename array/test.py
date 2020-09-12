import unittest

from lcs import LCS


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

if __name__ == '__main__':
    unittest.main()
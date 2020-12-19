import unittest
from div_alg import div_alg


class TestDivAlg(unittest.TestCase):
    def test_zero_div(self):
        self.assertEqual(div_alg(3, 0), "Zero Division Error")

    def test_bigger_divisor(self):
        self.assertEqual(div_alg(3, 4), (0, 3))

    def test_unsigned_div_alg(self):
        self.assertEqual(div_alg(7, 3), (2, 1))

    def test_signed_div_alg(self):
        self.assertEqual(div_alg(-17, 3), (-6, 1))
        self.assertEqual(div_alg(2, -4), (-1, 2))
        # We calculated this taking (2, -4) --> (-2, 4). Then -2 = 4(-1) +2


if __name__ == '__main__':
    unittest.main()

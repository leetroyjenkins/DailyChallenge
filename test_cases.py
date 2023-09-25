from gfg import maxindexdiff
from gfg import stockBuyAndSell
from gfg import countsubarraylessthank


class TestMaxIndexDiff:
    #pytest -k TestMaxIndexDiff

    def test_maxIndexDiff_01(self):
        self.test_array = [34, 8, 10, 3, 2, 80, 30, 33, 1]
        self.n = 9
        assert maxindexdiff.max_index_diff(self.n, self.test_array) == 6

    def test_maxIndexDiff_02(self):
        self.test_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.n = 8
        assert maxindexdiff.max_index_diff(self.n, self.test_array) == 8

    def test_maxIndexDiff_03(self):
        self.test_array = [1]
        self.n = 1
        assert maxindexdiff.max_index_diff(self.n, self.test_array) == 0


class TestStockAndBuy:
    # pytest -k TestStockAndBuy
    def test_stockBuyAndSell_01(self):
        self.test_array = [3, 4, 1, 5]
        self.n = 4
        assert stockBuyAndSell.stockBuyAndSell(self.test_array, self.n) == 5

    def test_stockBuyAndSell_02(self):
        self.test_array = [1, 3, 5, 7, 9]
        self.n = 5
        assert stockBuyAndSell.stockBuyAndSell(self.test_array, self.n) == 8

    def test_stockBuyAndSell_03(self):
        self.test_array =  [100, 180, 260, 310, 40, 535, 695]
        self.n = 7
        assert stockBuyAndSell.stockBuyAndSell(self.test_array, self.n) == 865

class TestCountSubarraysLessThanK:
    #pytest -k TestCountSubarraysLessThanK
    def test_TestCountSubarraysLessThanK_01(self):
        self.a = [1, 2, 3, 4]
        self.n = 4
        self.k = 10
        assert countsubarraylessthank.subArrayLessThanK(self.a, self.n, self.k) == 7

    def test_TestCountSubarraysLessThanK_02(self):
        self.a = [1, 9, 2, 8, 6, 4, 3]
        self.n = 7
        self.k = 100
        assert countsubarraylessthank.subArrayLessThanK(self.a, self.n, self.k) == 16

class TestFindSpiral:
    #pytest -k TestCountSubarraysLessThanK
    def test_find_spiral_01(self):
        self.a = [1, 2, 3, 4]
        self.n = 4
        self.k = 10
        assert countsubarraylessthank.subArrayLessThanK(self.a, self.n, self.k) == 7

    def test_find_spiral_02(self):
        self.a = [1, 9, 2, 8, 6, 4, 3]
        self.n = 7
        self.k = 100
        assert countsubarraylessthank.subArrayLessThanK(self.a, self.n, self.k) == 16
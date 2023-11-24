#Write to json in the test_results folder
# pytest tests/test_cases.py -q --report-log=test_results/log.json

import gfg

class TestselectionSort:
    def test_selectionSort_01(self):
        self.n = 5
        self.arr = [4, 1, 3, 9, 7]
        result = [1, 3, 4, 7, 9]
        assert gfg.selectionSort.selectionSort(self.arr, self.n) == result

    def test_selectionSort_02(self):
        self.n = 5
        self.arr = [4, 1, 3, 9, 7]
        result = [1, 3, 4, 7, 9]
        assert gfg.selectionSort.selectionSort(self.arr, self.n) == result


class TestinsertionSort:
    def test_insertionSort_01(self):
        self.n = 5
        self.arr = [12, 11, 13, 5, 6]
        result = [5, 6, 11, 12, 13]
        assert gfg.insertionSort.insertionSort(self.arr, self.n) == result

    def test_insertionSort_02(self):
        self.n = 5
        self.arr = [4, 1, 3, 9, 7]
        result = [1, 3, 4, 7, 9]
        assert gfg.insertionSort.insertionSort(self.arr, self.n) == result

    def test_insertionSort_03(self):
        self.n = 10
        self.arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        assert gfg.insertionSort.insertionSort(self.arr, self.n) == result
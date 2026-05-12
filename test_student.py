import unittest
from proj3 import huffman_encoding, heapify_up, heapify_down

class TestProj3(unittest.TestCase):

    def test_heapify_up(self):
        heap = [5, 10, 8, 20, 15, 9, 1]
        result = heapify_up(heap, 6)
        self.assertEqual(result, [1, 10, 5, 20, 15, 9, 8])

    def test_heapify_down(self):
        heap = [9, 3, 5]
        result = heapify_down(heap, 0)
        self.assertEqual(result, [3, 9, 5])

if __name__ == "__main__":
    unittest.main()
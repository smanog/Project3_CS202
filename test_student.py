import unittest
from proj3 import huffman_encoding, heapify_up, heapify_down, Node, MinHeap, insert

class TestProj3(unittest.TestCase):

    def test_heapify_up(self):
        heap = MinHeap([Node(1, 'A', Node(3, 'F', Node(5, 'S')))])
        result = heapify_up(heap, 6)
        self.assertEqual(result, [1, 10, 5, 20, 15, 9, 8])

    def test_heapify_down(self):
        heap = [9, 3, 5]
        result = heapify_down(heap, 0)
        self.assertEqual(result, [3, 9, 5])

    def test_insert(self):
        heap = MinHeap([Node(1, 'A', Node(3, 'F', Node(5, 'S')))])
        result = insert(heap, Node(20, 'Z'))
        self.assertEqual(result, MinHeap([Node(1, 'A', Node(3, 'F', Node(5, 'S'), Node(20, 'Z')))]))

if __name__ == "__main__":
    unittest.main()
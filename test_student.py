import unittest
from proj3 import huffman_encoding, heapify_up, heapify_down, Node, MinHeap, insert, extract_min, count_frequency, create_priority_queue

class TestProj3(unittest.TestCase):

    def test_heapify_up(self):
        heap = MinHeap([Node(1, 'A', Node(3, 'F', Node(5, 'S'))), Node(7, 'z')])
        result = heapify_up(heap, 0)
        self.assertEqual(result, MinHeap([Node(1,'A', Node(3, 'F', Node(5,'S'))), Node(7, 'z')]))

    def test_heapify_down(self):
        heap = [9, 3, 5]
        result = heapify_down(heap, 0)
        self.assertEqual(result, [3, 9, 5])

    def test_insert(self):
        heap = MinHeap([Node(1, 'A', Node(3, 'F', Node(5, 'S')))])
        result = insert(heap, Node(20, 'Z'))
        self.assertEqual(result, MinHeap([Node(1, 'A', Node(3, 'F', Node(5, 'S'), Node(20, 'Z')))]))

    def test_extract_min(self):
        heap = MinHeap([Node(1, 'A', Node(3, 'F', Node(5, 'S')))])
        result = extract_min(heap)
        self.assertEqual(result, Node(1, 'A', Node(3, 'F', Node(5, 'S'))))

    def test_count_frequency(self):
        s = 'hello'
        result = count_frequency(s)
        self.assertEqual(result, {'h': 1, 'e': 1, 'l': 2, 'o': 1})

    def test_create_priority_queue(self):
        pass

if __name__ == "__main__":
    unittest.main()
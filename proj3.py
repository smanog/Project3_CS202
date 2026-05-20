from __future__ import annotations
from dataclasses import dataclass, field

@dataclass(order=True, frozen=True)
class Node:
    freq: int
    char: str
    left: Node | None = None
    right: Node | None  = None

    def __str__(self):
        return f"Node: {self.char}, Freq: {self.freq}"

@dataclass(frozen=True)
class MinHeap:
    data: list[Node] = field(default_factory=list)

def heapify_up(heap: MinHeap, index: int) -> MinHeap:
    new_heap = heap
    #if index == 0:
     #   return new_heap

    parent_freq = (index - 1) // 2

    if new_heap.data[index].freq < new_heap.data[parent_freq].freq:
        temp = new_heap.data[index].freq
        new_heap.data[index].freq = new_heap.data[parent_freq].freq
        new_heap.data[parent_freq].freq = temp
        return heapify_up(new_heap, parent_freq)

    if new_heap.data[index].char < new_heap.data[parent_freq].char:
        temp = new_heap.data[index].char
        new_heap.data[index].char = new_heap.data[parent_freq].char
        new_heap.data[parent_freq].char = temp
        return heapify_up(new_heap, parent_freq)
    return new_heap

def insert(heap: MinHeap, element: Node) -> MinHeap:
    new_heap = MinHeap(heap.data + [element])
    new_heap = heapify_up(new_heap, len(new_heap.data) - 1)
    return new_heap

def heapify_down(heap: MinHeap, index: int) -> MinHeap:
    new_heap = heap
    left = 2 * index + 1
    right = 2 * index + 2
    size = len(new_heap.data)
    if left >= size:
        return new_heap

    smallest = left

    if right < size and new_heap.data[right] < new_heap.data[left]:
        smallest = right
    if new_heap.data[smallest] < new_heap.data[index]:
        temp = new_heap.data[index]
        new_heap.data[index] = new_heap.data[smallest]
        new_heap.data[smallest] = temp
        return heapify_down(new_heap, smallest)
    return new_heap


def extract_min(heap: MinHeap) -> tuple[MinHeap, Node]:
    heapify_down(heap, 0)
    return heap, heap.data[0]

        
def count_frequency(s: str)-> dict[str,int]:
    freq = { }
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq


def create_priority_queue(frequency: dict[str, int]) -> MinHeap:
    pq = MinHeap([])
    for key in frequency:
        insert(pq, Node(frequency[key], key))
    return pq

def build_tree_from_queue(priority_queue: MinHeap) -> Node:
    pq = priority_queue
    while len(priority_queue.data) != 1:
        for data in priority_queue.data:
            freq = data.freq + data[1].freq
            char = min(data.char, data[1].char)
            new_node = Node(freq, char)
            insert(pq, new_node)
            extract_min(pq)
    return pq




def generate_codes(node: Node | None, prefix="", code: dict | None =None)-> dict:
    if code is None:
        code = {}  
    pass


def encode(s: str, codes: dict)-> str:
    pass


def decode(encoded_string: str, root: Node)-> str:
    pass

def huffman_encoding(s:str):
    #Do Not Change this function
    frequency = count_frequency(s)
    pq = create_priority_queue(frequency)
    root = build_tree_from_queue(pq)
    codes = generate_codes(root)
    encoded_string = encode(s, codes)
    decoded_string = decode(encoded_string,root)
    return encoded_string, decoded_string, codes


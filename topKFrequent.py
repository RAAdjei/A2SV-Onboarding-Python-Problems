class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        heap_count = Counter(words)

        heap_count = [(-values, key) for key, values in heap_count.items()]

        heapq.heapify(heap_count)

        while len(heap) < k:
            heap.append(heappop(heap_count)[1])
        return heap

"""
Time - O(N)
Space - O(N)
"""

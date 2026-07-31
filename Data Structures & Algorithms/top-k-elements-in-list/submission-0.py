import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_counter = {}
        for num in nums:
            freq_counter[num] = freq_counter.get(num, 0) + 1
        
        heap = [(-val, key) for key, val in freq_counter.items()]
        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]
        

        
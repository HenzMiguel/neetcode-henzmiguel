import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)

        # Check if rearrangement is impossible
        if max(count.values()) > (len(s) + 1) // 2:
            return ""

        # Max heap: (-frequency, character)
        heap = [(-freq, ch) for ch, freq in count.items()]
        heapq.heapify(heap)

        res = []

        while len(heap) >= 2:
            freq1, ch1 = heapq.heappop(heap)
            freq2, ch2 = heapq.heappop(heap)

            # Use the two most frequent different characters
            res.append(ch1)
            res.append(ch2)

            # Decrease counts (remember freq is negative)
            if freq1 + 1 < 0:
                heapq.heappush(heap, (freq1 + 1, ch1))
            if freq2 + 1 < 0:
                heapq.heappush(heap, (freq2 + 1, ch2))

        if heap:
            res.append(heap[0][1])

        return "".join(res)
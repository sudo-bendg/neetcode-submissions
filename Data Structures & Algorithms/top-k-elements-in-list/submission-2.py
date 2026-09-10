class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        L = len(nums)

        frequencies = dict()
        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1

        buckets = [[] for i in range(L)]

        for num in frequencies:
            buckets[frequencies[num] - 1].append(num)
        
        returnSet = [0] * k
        returnedItems = 0

        for i in range(L - 1, -1, -1):
            if buckets[i]:
                for n in buckets[i]:
                    if returnedItems < k:
                        returnSet[returnedItems] = n
                        returnedItems += 1
        
        return returnSet
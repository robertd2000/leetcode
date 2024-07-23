from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        frequency = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        for i, j in hashmap.items():
            frequency[j].append(i)

        res = []

        for i in range(len(frequency) - 1, 0, -1):
            for j in frequency[i]:
                res.append(j)
                if len(res) == k:
                    return res

        # hashmap = {}
        # res = []

        # for i in nums:
        #     if i in hashmap:
        #         hashmap[i] += 1
        #     else:
        #         hashmap[i] = 1
        # print(hashmap)
        # sorted_hash = list(sorted(hashmap.items(), key=lambda item: item[1]))[::-1]
        # print(sorted_hash)

        # return [i for i, _ in list(sorted_hash)[:k]]
            
        # counter = Counter(nums).most_common(k)
        # return [i for i, _ in list(counter)]
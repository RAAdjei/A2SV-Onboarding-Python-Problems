class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        hashmap = defaultdict(int) 
        hashmap[0] = 1 
        count = 0

        for num in nums:
            if num % 2 == 1:
                prefix_sum += 1  # Increment the prefix sum for odd numbers
            if prefix_sum - k in hashmap:
                count += hashmap[prefix_sum - k]
            hashmap[prefix_sum] += 1

        return count

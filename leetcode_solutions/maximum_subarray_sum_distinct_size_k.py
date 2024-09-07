def maximumSubarraySum(nums: list[int], k: int) -> int:
        max_sum = 0
        cur_sum = sum(nums[:k])
        freq    = {}

        for v in nums[:k]:
            if v in freq:
                freq[v] += 1
            else:
                freq[v] = 1
        
        if len(freq) == k:
            max_sum = cur_sum

        for i in range(k, len(nums)):
            # current sum = current sum + (end of window - start of window) 
            cur_sum += nums[i] - nums[i - k]

            # get rid of whats no longer in window
            freq[nums[i - k]] -= 1
            if freq[nums[i - k]] == 0:
                del freq[nums[i - k]]

            # insert newest item's freq which is the end of the window
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
            
            # Update max if current sum is greater than max
            if len(freq) == k:
                max_sum = max(cur_sum, max_sum)

        return max_sum
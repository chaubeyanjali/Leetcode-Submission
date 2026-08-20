class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = {}

        for ch in s1:
            s1_count[ch] = s1_count.get(ch,0)+1

        left = 0
        window_count = {}

        for right in range(len(s2)):
            window_count[s2[right]] = window_count.get(s2[right], 0)+1

            if right - left + 1 > len(s1):
                window_count[s2[left]] -= 1
                
                if window_count[s2[left]] == 0:
                    del window_count[s2[left]] 
                left += 1
          
            if s1_count == window_count:
                return True

        return False

        
        
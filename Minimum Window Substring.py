class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''
        
        t_map, s_map = {}, {}
        for chr in t:
            t_map[chr] = 1 + t_map.get(chr,0)
            s_map[chr] = 0
        left, have, need = 0, 0, len(t_map)
        index, res = [-1, 1], float('infinity')

        for right,chr in enumerate(s):
            if t_map.get(chr, 0):
                s_map[chr] = 1 + s_map.get(chr, 0)
                if s_map[chr] == t_map[chr]:
                    have += 1
            
            while have == need:
                if right - left + 1 < res:
                    res = right - left + 1
                    index = [left , right]
                
                s_map[s[left]] = s_map.get(s[left], 0) - 1
                if s[left] in t_map and s_map[s[left]] < t_map[s[left]]:
                    have -= 1
                left += 1

        l, r = index
        if res != float('infinity'):
            return s[l : r+1]
        else:
            return ''

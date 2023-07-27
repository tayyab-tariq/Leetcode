class TimeMap:

    def __init__(self):        
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.time_map.get(key, 0):
            self.time_map[key].append((value, timestamp))
        else:
            self.time_map[key] = []
            self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # print(self.time_map)
        # print(key, timestamp)
        if self.time_map.get(key, 0):
            nums = self.time_map[key]
            if timestamp == 15:
                print(self.time_map[key])

            left, right = 0, len(nums)-1
            if left != right:
                if timestamp < nums[left][1]:
                    return ''
                elif timestamp > nums[right][1]:
                    return nums[right][0]

                while left <= right:
                    mid = (left+right) // 2
                    # if timestamp == 15:
                        # print(mid, nums[mid], nums[mid][1], nums[left][1],left, right)
                    if nums[mid][1] == timestamp:
                        return nums[mid][0] 
                    elif nums[mid][1] < timestamp:
                        left = mid + 1
                    else:
                        right = mid - 1  
                
                # if timestamp == 15:
                #     print(nums[right][0], nums[right][1], '     ', nums[left][0], nums[left][1])
                #     print()
                
                if nums[right][1] <= timestamp: 
                    return nums[right][0]
                else:
                    return nums[left][0]
            else:
                return nums[left][0]
        else:
            return ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

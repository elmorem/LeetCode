from typing import List
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        starts = sorted(i[0] for i in intervals)
        ends = sorted(i[1] for i in intervals)
        i = j = 0
        used = 0
        max_rooms = 0
        while i < len(starts):
            if starts[i] < ends[j]:
                used +=1
                if used > max_rooms:
                    max_rooms = used
                i+=1
            else:
                used -=1
                j +=1
        return max_rooms

if __name__ == "__main__":
    sol = Solution()
    intervals1 = [[0,30],[5,10],[15,20]]
    print(sol.minMeetingRooms(intervals1))  # Expected output: 2

    intervals2 = [[7,10],[2,4]]
    print(sol.minMeetingRooms(intervals2))  # Expected output: 1

    intervals3 = [[1,5],[8,9],[8,9]]
    print(sol.minMeetingRooms(intervals3))  # Expected output: 2

    intervals4 = []
    print(sol.minMeetingRooms(intervals4))  # Expected output: 0

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # l = 0
        # r = len(intervals) - 1
        # while l < r:
        #     middle = l + ((r - l) // 2)

        #     if newInterval[0] == intervals[middle][0]:
        #         break
        #     elif newInterval[0] > intervals[middle][0]:
        #         l = middle + 1
        #     else:
        #         r = middle - 1

        # if l <= 0: #start
        #     if newInterval[1] >= intervals[l][0]:
        #         intervals[l][0] = newIntervals[0]
        # elif l >= len(intervals): #end
        #     if newInterval[0] <= intervals[l-1][1]:
        #         intervals[l-1][1] = newIntervals[1]
        # else: #middle
        #     if newInterval[0] > intervals[l-1][1] and newInterval[0] < intervals[l][0]:
        #         intervals.insert(l, newInterval)
        #     else:
        #         if newInterval[0] <= intervals[l-1][1]:
        #             intervals[l-1][1] = newIntervals[1]
        #         if newInterval[1] >= intervals[l][0]:
        #             intervals[l][0] = newIntervals[0]
        #         if intervals[l][0] <= intervals[l-1][1]:
        #             intervals[l-1][1] = intervals[l][1]
        #             del intervals[l]

        i = 0
        while i < len(intervals):
            if newInterval[0] <= intervals[i][1]:
                if newInterval[0] >= intervals[i][0]:
                    newInterval[0] = intervals[i][0]
                break
            i += 1

        start = i
        while i < len(intervals):
            # standard continuation. absorb interval
            if intervals[i][1] <= newInterval[1]:
                i+=1
                continue
            else:
                # merge and end
                if intervals[i][0] <= newInterval[1]:
                    newInterval[1] = intervals[i][1]
                    intervals[i][0] = newInterval[0]
                    del intervals[start:i]
                    return intervals
                # insert and end
                else:
                    del intervals[start:i]  
                    intervals.insert(start, newInterval)
                    return intervals   

        del intervals[start:]
        intervals.append(newInterval)
        return intervals

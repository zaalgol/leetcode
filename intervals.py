class Solution:
    def insert(self, intervals: list[list[int]], newInterval):
            def overlap(interval, new_interval):
                if new_interval[0] > interval[1]:
                    return 'new_is_bigger'
                if new_interval[1] < interval[0]:
                    return 'new_is_samller'
                return "overlap"
            leni = len(intervals)
            if not leni:
                intervals.append(newInterval)
                return intervals
            if newInterval[0] > intervals[leni-1][1]:
                intervals.append(newInterval)
                return intervals
            j = 0
            result = []
            inserted = False
            while j< leni:
                overlap_status = overlap(intervals[j], newInterval)
                if overlap_status == 'new_is_bigger':
                    result.append(intervals[j])
                    j +=1
                    continue
                if overlap_status == 'new_is_samller': #add before
                    result.append(newInterval)
                    return result + intervals[j:]
                
                # overlap
                min_start = min(newInterval[0], intervals[j][0])
                max_end = max(newInterval[1], intervals[j][1])
                j +=1
                while j< leni:
                    overlap_status = overlap(intervals[j], newInterval)
                    if overlap_status == 'new_is_samller': #add before
                        result.append([min_start, max_end])
                        return result + intervals[j:]

                    max_end = max(max_end, intervals[j][1])
                    j +=1
                result.append([min_start, max_end])
                return result
            
solution = Solution()
solution.insert([[1,5]], )
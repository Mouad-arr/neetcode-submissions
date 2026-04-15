class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals)==0:
            intervals.append(newInterval)
        elif newInterval[0]<intervals[0][0] :
            blackList=list()
            i=0
            if intervals[0][0] <= newInterval[1] :
                intervals[0][0]= newInterval[0]
                i+=1
                while  i<len(intervals) and intervals[i][0] < newInterval[1] :
                    blackList.append(i)
                    i+=1
                if intervals[i-1][1] > newInterval[1]:
                    intervals[0][1]=intervals[i-1][1]
                else:
                    intervals[0][1]=newInterval[1]
                for x in range(len(blackList)-1,-1,-1) :
                    intervals.remove(intervals[blackList[x]])
            else:
                intervals.insert(0,newInterval)
        else:
            for i in range(len(intervals)) :
                if intervals[i][0]<=newInterval[0]<=intervals[i][1]:
                    if intervals[i][1] < newInterval[1] :
                        blackList=list()
                        j=i+1
                        while j<len(intervals) and intervals[j][0] < newInterval[1] :
                            blackList.append(j)
                            j+=1
                        if intervals[j-1][1] > newInterval[1]:
                            intervals[i][1]=intervals[j-1][1]
                        elif j<len(intervals) and intervals[j][0] == newInterval[1]:
                            blackList.append(j)
                            intervals[i][1]=intervals[j][1]
                        else:
                            intervals[i][1]=newInterval[1]
                        for x in range(len(blackList)-1,-1,-1) :
                            intervals.remove(intervals[blackList[x]])
                    break
                elif newInterval[0]>intervals[i][1] and i<len(intervals)-1 and newInterval[0]<=intervals[i+1][0]:
                    if i<len(intervals)-1 :
                        if  newInterval[1]<intervals[i+1][0]:
                            intervals.insert(i+1,newInterval)
                        else:
                            blackList=list()
                            j=i+1
                            while intervals[j][0] < newInterval[1] and j<len(intervals) :
                                blackList.append(j)
                                j+=1
                            if intervals[j-1][1] > newInterval[1]:
                                intervals[i][1]=intervals[j-1][1]
                            else:
                                intervals[i][1]=newInterval[1]
                            for x in range(len(blackList)-1,-1,-1) :
                                intervals.remove(intervals[blackList[x]])
                    else:
                        intervals.append(newInterval)
                    break
                elif i==len(intervals)-1:
                    intervals.append(newInterval)
                    break
        return intervals
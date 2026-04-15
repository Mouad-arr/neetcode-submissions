class Solution {
    /**
     * @param {number[][]} intervals
     * @return {number}
     */
    eraseOverlapIntervals(intervals) {
        intervals.sort((a, b) => a[0] - b[0]);
        let count=0;
        let n=intervals.length ;
        for(let i=1;i<n;i++){
            if(intervals[i][0]<intervals[i-1][1]){
                count++;
                intervals[i][1]=Math.min(intervals[i][1],intervals[i-1][1]);
            }
        }
        return count;
    }
}

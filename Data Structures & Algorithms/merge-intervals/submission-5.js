class Solution {
    /**
     * @param {number[][]} intervals
     * @return {number[][]}
     */
    merge(intervals) {
        intervals.sort((a, b) => a[0] - b[0]);
        let i=0,n=intervals.length ;
        while(i<n-1){
            if(intervals[i][1]>=intervals[i+1][0]){
                intervals[i][1]=Math.max(intervals[i][1],intervals[i+1][1]);
                intervals.splice(i+1,1);
                n=intervals.length ;
            }
            else i++;
        }
        return intervals;
    }
}

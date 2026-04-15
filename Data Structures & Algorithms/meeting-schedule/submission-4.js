/**
 * Definition of Interval:
 * class Interval {
 *   constructor(start, end) {
 *     this.start = start;
 *     this.end = end;
 *   }
 * }
 */

class Solution {
    /**
     * @param {Interval[]} intervals
     * @returns {boolean}
     */
    canAttendMeetings(intervals) {
        let n = intervals.length ;
        for(let i=1;i<n;i++){
            if(intervals[i].start < intervals[i-1].end && intervals[i].start >= intervals[i-1].start){
                return false;
            }
        }
        return true;
    }
}

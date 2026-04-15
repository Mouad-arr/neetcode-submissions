class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
         return a[0] < b[0];
        });
        int count=0;
        int n=intervals.size();
        for(int i=1;i<n;i++){
            if(intervals[i][0]<intervals[i-1][1]){
                count++;
                intervals[i][1]=min(intervals[i][1],intervals[i-1][1]);
            }
        }
        return count ;
    }
};

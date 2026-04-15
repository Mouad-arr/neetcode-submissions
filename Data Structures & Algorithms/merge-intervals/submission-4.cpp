class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
         return a[0] < b[0];
        });
        int i=0,n=intervals.size();
        while(i<n-1){
            if(intervals[i][1]>=intervals[i+1][0]){
                intervals[i][1]=max(intervals[i][1],intervals[i+1][1]);
                intervals.erase(intervals.begin() + i+1);
                n=intervals.size();
            }
            else i++;
        }
        return intervals;
    }
};

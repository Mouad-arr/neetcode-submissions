class Solution {
    public int[][] merge(int[][] intervals) {
         Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        int i=0,n=intervals.length ;
        while(i<n-1){
            if(intervals[i][1]>=intervals[i+1][0]){
                intervals[i][1]=Math.max(intervals[i][1],intervals[i+1][1]);
                ArrayList<int[]> list = new ArrayList<>(Arrays.asList(intervals));
                list.remove(i+1); 
                intervals = list.toArray(new int[0][]); 
                n=intervals.length;
            }
            else i++;
        }
        return intervals;
    }
}

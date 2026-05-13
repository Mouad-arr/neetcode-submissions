class Solution {
     public int partition(int[] A, int low, int high) {
        int pivot = A[high];
        int i = low - 1;
        for (int j = low; j < high; j++) {
            if (A[j] <= pivot) {
                i++;
                int temp=A[i];
                A[i]=A[j];
                A[j]=temp;
            }
        }
        int temp=A[i+1];
        A[i+1]=A[high];
        A[high]=temp;
        return i + 1;
    }
    private void quickSort(int[] arr,int low ,int high){
        if(low<high){
            int pi = partition(arr, low, high);
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }
    public int numRescueBoats(int[] people, int limit) {
        int n = people.length ;
        int left=0,right=n-1 , res=0;
        quickSort(people,left,right);
        while(left<right){
            if(people[left]+people[right]<=limit){
                res++;
                right--;
                left++;
            }
            else{
                res++;
                right--;
            }
        }
        if(left==right)
             return ++res;
        return res ;
    }
}
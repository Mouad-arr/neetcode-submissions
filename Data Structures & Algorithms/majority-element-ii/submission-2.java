class Solution {
    public List<Integer> majorityElement(int[] nums) {
        int c1 = 0, c2 = 0;
        Integer a = null, b = null;

        for (int x : nums) {
            if (a != null && x == a) c1++;
            else if (b != null && x == b) c2++;
            else if (c1 == 0) {
                a = x;
                c1 = 1;
            } else if (c2 == 0) {
                b = x;
                c2 = 1;
            } else {
                c1--;
                c2--;
            }
        }

        c1 = 0;
        c2 = 0;

        for (int x : nums) {
            if (a != null && x == a) c1++;
            else if (b != null && x == b) c2++;
        }

        List<Integer> res = new ArrayList<>();

        if (c1 > nums.length / 3) res.add(a);
        if (c2 > nums.length / 3) res.add(b);

        return res;
    }
}
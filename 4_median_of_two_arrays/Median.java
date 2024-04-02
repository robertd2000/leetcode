class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int n = nums1.length;
        int m = nums2.length;
        int r = n + m;
        int[] res = new int[r];

        int i = 0;
        int j = 0;
        int k = 0;

        while (i < n && j < m) {
            if (nums1[i] < nums2[j]) {
                res[k] = nums1[i];
                i++;
            } else {
                res[k] = nums2[j];
                j++;
            }
            k++;
        }

        while (i < n) {
            res[k] = nums1[i];
            i++;
            k++;
        }

        while (j < m) {
            res[k] = nums2[j];
            j++;
            k++;
        }

        int q = res.length / 2;

        if (r % 2 == 0) {
            return (res[q] + res[q - 1]) / 2.0;
        }

        return res[q];
    }
}
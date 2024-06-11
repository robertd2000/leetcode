class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        int[] count = new int[1001];

        for (int i : arr1) {
            count[i]++;

        }

        int pos = 0;

        for (int i : arr2) {
            while (count[i] > 0) {
                count[i]--;
                arr1[pos] = i;
                pos++;
            }
        }

        for (int i = 0; i < count.length; i++) {
            while (count[i] > 0) {
                count[i]--;
                arr1[pos] = i;
                pos++;
            }
        }

        return arr1;
    }
}
class Solution {
    public int hIndex(int[] citations) {
        Arrays.sort(citations);

        int h = 0;
        int n = citations.length;

        for (int i = 0; i < n; i++) {
            int m = n - getIndexOf(citations, citations[i], i);
            h = Math.max(h, Math.min(citations[i], m));
        }

        return h;
    }

    private int getIndexOf(int[] arr, int element, int start) {
        for (int i = start; i < arr.length; i++) {
            if (arr[i] == element)
                return i;
        }

        return -1;
    }
}
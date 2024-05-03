class Solution {
    public int compareVersion(String version1, String version2) {
        String[] l1 = version1.split("\\.");
        String[] l2 = version2.split("\\.");

        int n1 = l1.length;
        int n2 = l2.length;

        int n = Math.max(n1, n2);

        for (int i = 0; i < n; i++) {
            Integer v1 = i < n1 ? Integer.parseInt(l1[i]) : 0;
            Integer v2 = i < n2 ? Integer.parseInt(l2[i]) : 0;

            int v = v1.compareTo(v2);
            if (v != 0) {
                return v;
            }
        }
        return 0;
    }
}
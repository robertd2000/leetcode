class Solution {
    public int maxDepth(String s) {
        int maxNesting = 0;
        int currentParentheses = 0;

        for (int i : s.toCharArray()) {
            if (i == '(') {
                currentParentheses++;
                maxNesting = Math.max(currentParentheses, maxNesting);
            }
            if (i == ')') {
                currentParentheses--;
            }
        }

        return maxNesting;
    }
}
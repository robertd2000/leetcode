class Solution {
    public int maxDepth(String s) {
        int maxNesting = 0;
        List<String> stack = new ArrayList<String>();

        for (char i : s.toCharArray()) {
            if (i == '(') {
                stack.add(String.valueOf(i));
                maxNesting = Math.max(stack.size(), maxNesting);
            }
            if (i == ')') {
                stack.remove(stack.size() - 1);
            }
        }

        return maxNesting;
    }
}
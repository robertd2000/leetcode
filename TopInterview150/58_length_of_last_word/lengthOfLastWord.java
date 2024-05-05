class Solution {
    public int lengthOfLastWord(String s) {
        int len = 0;
        int tail = s.length() - 1;

        while (tail >= 0 && s.charAt(tail) == ' ' ) {
            tail--;
        }

        while (tail >= 0 && s.charAt(tail) != ' ' ) {
            len++;
            tail--;
        }

        return len;
    }
}
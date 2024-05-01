class Solution {
    public String reversePrefix(String word, char ch) {
        int charIndex = word.indexOf(ch);
        String pre = new StringBuilder(word.substring(0, charIndex + 1)).reverse().toString();
        return pre + word.substring( charIndex + 1);
    }
}
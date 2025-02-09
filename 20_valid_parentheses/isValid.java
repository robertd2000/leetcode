class Solution {
    public boolean isValid(String s) {
        Character[] values = { '(', '[', '{' };
        List<Character> stack = new ArrayList<>();
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (Arrays.asList(values).contains(c)) {
                stack.add(c);
            } else {
                if (stack.size() == 0) {
                    return false;
                } else {
                    Character current = stack.remove(stack.size() - 1);

                    if (current == '(' && c != ')') {
                        return false;
                    } else if (current == '[' && c != ']') {
                        return false;
                    }
                    if (current == '{' && c != '}') {
                        return false;
                    }
                }
            }
        }

        if (stack.size() > 0) {
            return false;
        }

        return true;
    }
}
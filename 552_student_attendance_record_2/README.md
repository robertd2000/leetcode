# [552. Student Attendance Record II](https://leetcode.com/problems/student-attendance-record-ii/description/?envType=daily-question&envId=2024-05-26)

An attendance record for a student can be represented as a string where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

- `'A'`: Absent.
- `'L'`: Late.
- `'P'`: Present.

Any student is eligible for an attendance award if they meet **both** of the following criteria:

- The student was absent (`'A'`) for **strictly** fewer than 2 days **total**.
- The student was **never** late (`'L'`) for 3 or more **consecutive** days.

Given an integer `n`, _return the **number** of possible attendance records of length n that make a student eligible for an attendance award. The answer may be very large, so return it **modulo** `10^9 + 7`._

## Example 1:

```

Input: n = 2
Output: 8
Explanation: There are 8 records with length 2 that are eligible for an award:
"PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).

```

## Example 2:

```

Input: n = 1
Output: 3

```

## Example 3:

```

Input: n = 10101
Output: 183236316

```

## Constraints:

- `1 <= n <= 10^5`

# Code

```java

class Solution {
    public int checkRecord(int n) {
        final int MOD = 1000000007;
        int[][][] f = new int[n + 1][2][3];

        f[0] = new int[][] { { 1, 1, 1 }, { 1, 1, 1 } };
        for (int i = 1; i <= n; i++)
            for (int j = 0; j < 2; j++)
                for (int k = 0; k < 3; k++) {
                    int val = f[i - 1][j][2];
                    if (j > 0)
                        val = (val + f[i - 1][j - 1][2]) % MOD;
                    if (k > 0)
                        val = (val + f[i - 1][j][k - 1]) % MOD;
                    f[i][j][k] = val;
                }

        return f[n][1][2];
    }
}

```

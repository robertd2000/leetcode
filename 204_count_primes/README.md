[204. Count Primes](https://leetcode.com/problems/count-primes/description/)

Given an integer `n`, return _the number of prime numbers that are strictly less than_ `n`.

**Example 1:**

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

**Example 1:**

Input: n = 0
Output: 0

**Constraints:**

- `0 <= n <= 5 * 10^6`

Idea:
There are several ways to go about solving this problem, but the classic solution is known as the sieve of Eratosthenes. For the sieve of Eratosthenes, we start by creating a boolean array (seen) of size n to represent each of the numbers less than n.

We start at 2 and for each number processed (num), we iterate through and mark each multiple (mult) of num, starting at num^2, as seen. We start at num^2 because every multiple up to the num'th multiple will have been guaranteed to have been seen before, since they're also a multiple of a smaller number. For example, when processing 5s, we can skip to 25 because 10 will have been seen when we processed 2s, 15 when we processed 3s, and 20 when we processed 2s.

Then we move num forward, skipping any numbers that have already been seen. By doing this, we will only stop on prime numbers, because they haven't been seen as a multiple of a previous iteration. We just have to update our count (ans) each time we stop and then return ans once we reach n.

Visual 1

![alt text](Sieve_of_Eratosthenes_animation.gif)

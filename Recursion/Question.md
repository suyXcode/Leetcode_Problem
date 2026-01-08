# Number of Digit One

## Solution
---
Approach #1 Brute force [Time Limit Exceeded]
---

Intuition:
Do as directed in question.

Algorithm

- Iterate over i from 1 to n:
    1. Convert i to string and count ’1’ in each integer string
    2. Add count of ’1’ in each string to the sum, say 'countr'
--- 
int countDigitOne(int n)
{
    int countr = 0;
    for (int i = 1; i <= n; i++) {
        string str = to_string(i);
        countr += count(str.begin(), str.end(), '1');
    }
    return countr;
}

---

# Complexity Analysis
---
- Time complexity: O(n∗log (n)).

    1. We iterate from 1 to n
    2. In each iteration, we convert integer to string and count '1' in string which takes linear time in number of digits in i, which is log10(n).
- Space complexity: O(log10(n)) Extra space for the countr and the converted string str.


---


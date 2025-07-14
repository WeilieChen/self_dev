# Example 1:

# Input: 
s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


def long_sub(s):
    index_map ={}
    left = 0
    max_len = 0

    for right in range(len(s)):
        if s[right] in index_map:
            ### move the left pointer to ensure no duplicate char 
            left = max(left, index_map[s[right]]+1)
        # update the lat seen index of chart

        index_map[s[right]] = right

        max_len = max(max_len,right - left +1)

    return max_len
print(long_sub(s))
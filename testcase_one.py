def funnyString(s):
    n = len(s)
    for i in range(1, n):
        start_diff = abs(ord(s[i]) - ord(s[i - 1]))
        end_diff = abs(ord(s[n - i]) - ord(s[n - i - 1]))
        if start_diff != end_diff:
            return 'Not Funny'
    return 'Funny'

# Test cases
test_cases = [
    ("", "Funny"),            # Empty string
    ("a", "Funny"),           # Single character
    ("aa", "Funny"),          # Two identical characters
    ("ab", "Funny"),          # Two different characters
    ("aaa", "Funny"),         # All same characters
    ("racecar", "Funny"),     # Palindrome (odd length)
    ("abba", "Funny"),        # Palindrome (even length)
    ("abcde", "Funny"),       # Non-palindrome (odd length)
    ("abcd", "Funny"),        # Non-palindrome (even length)
    ("bcxz", "Not Funny"),    # Non-funny string (odd length)
    ("abababab", "Funny"),    # Alternating characters
    ("azAZ", "Funny"),        # Large differences
]

all_passed = True
for s, expected in test_cases:
    result = funnyString(s)
    if result != expected:
        all_passed = False
        print(f"Test case {s}: Failed (Expected {expected}, got {result})")
    else:
        print(f"Test case {s}: Passed")

if all_passed:
    print("All test cases passed!")
else:
    print("Some test cases failed.")
def staircase(n, display):
    if n <= 0 or n > 30:
        return "n must be in the range of 1 to 30"
    
    result = []
    for i in range(1, n + 1):
        result.append(display * i)
    return '\n'.join(result)

# Test cases
test_cases = [
    (1, "#", "#"),  # n = 1, display = "#"
    (4, "#", "#\n##\n###\n####"),  # n = 4, display = "#"
    (5, "*", "*\n**\n***\n****\n*****"),  # n = 5, display = "*"
    (30, "+", "+\n++\n+++\n++++\n+++++\n" + "\n".join(["+" * i for i in range(6, 31)])),  # n = 30, display = "+"
    (0, "#", "n must be in the range of 1 to 30"),  # n = 0, display = "#"
    (-1, "*", "n must be in the range of 1 to 30"),  # n = -1, display = "*"
    (31, "+", "n must be in the range of 1 to 30"),  # n = 31, display = "+"
    (100, "*", "n must be in the range of 1 to 30"),  # n = 100, display = "*"
    (5, "A", "A\nAA\nAAA\nAAAA\nAAAAA"),  # n = 5, display = "A"
    (2, "@", "@\n@@")  # n = 2, display = "@"
]

all_passed = True  # Track the status of test cases

for i, (n, display, expected_output) in enumerate(test_cases):
    print(f"Running Test Case {i+1}: n = {n}, display = '{display}'")
    try:
        captured_output = staircase(n, display)
        
        # Check if the result matches the expected output
        if captured_output != expected_output:
            print(f"Test Failed! Expected:\n{expected_output}\nbut got:\n{captured_output}")
            all_passed = False
        else:
            print(f"Test Passed!")
    except Exception as e:
        print(f"Test Failed! Error: {e}")
        all_passed = False  # Mark as failed if an error occurs
    print()

# Check if all test cases passed
if all_passed:
    print("All test cases passed!")
else:
    print("Some test cases failed.")


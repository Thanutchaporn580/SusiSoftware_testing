def fizzbuzz(x):
    if x % 3 == 0 and x % 5 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return str(x)
    
test_cases = [
    (3, "Fizz"),
    (6, "Fizz"),
    (9, "Fizz"),
    (12, "Fizz"),
    (5, "Buzz"),
    (10, "Buzz"),
    (20, "Buzz"),
    (25, "Buzz"),
    (15, "FizzBuzz"),
    (30, "FizzBuzz"),
    (45, "FizzBuzz"),
    (60, "FizzBuzz"),
    (1, "1"),
    (2, "2"),
    (4, "4"),
    (7, "7"),
    (8, "8"),
    (11, "11"),
]
all_passed = True

for x, expected in test_cases:
    result = fizzbuzz(x)
    print(f"fizzbuzz({x}) = {result} (Expected: {expected})")
    if result == expected:
        print("Test Passed!")
    else:
        print("Test Failed!")
        all_passed = False
    print()

if all_passed:
    print("All test cases passed!")
else:
    print("Some test cases failed.")
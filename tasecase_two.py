def alternatingCharacters(s):
    # Write your code here
    deletions = 0
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            deletions += 1
    return deletions

def test_alternatingCharacters():
    test_cases = [
        ("AAAA", 3, "ซ้ำกันทั้งหมด A"),
        ("BBBBB", 4, "ซ้ำกันทั้งหมด B"),
        ("ABABABAB", 0, "ไม่มีการลบ (AB สลับกัน)"),
        ("BABABA", 0, "ไม่มีการลบ (BA สลับกัน)"),
        ("AAABBB", 4, "แบ่งเป็นสองกลุ่มซ้ำกัน"),
        ("A", 0, "มีตัวอักษรเดียว"),
        ("AB", 0, "ไม่มีการลบ AB"),
        ("BA", 0, "ไม่มีการลบ BA"),
        ("AABBAB", 2, "ซ้ำกันบางจุด"),
        ("ABBAABB", 3, "ซ้ำกันและมีรูปแบบที่ต้องลบหลายจุด")
    ]
    
    all_passed = True
    
    for s, expected, desc in test_cases:
        result = alternatingCharacters(s)
        print(f"Test case: {s} ({desc})")
        print(f"Expected: {expected}, Got: {result}")
        if result != expected:
            print("Failed!")
            all_passed = False
        else:
            print("Passed!")
        print()
    
    if all_passed:
        print("All test cases passed!")
    else:
        print("Some test cases failed!")

test_alternatingCharacters()

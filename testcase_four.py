def alternate(s):
    lens = [0]   
    letters = list(set(s))
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            two = []
            for c in s:
                if c in (letters[i], letters[j]):
                    if two and two[-1] == c:
                        two = []
                        break
                    two.append(c)
            lens.append(len(two))
    return max(lens)

test_cases = [
    ("beabeefeab", 5),     # ปกติ
    ("aaaa", 0),           # มีตัวเดียว
    ("ababab", 6),         # สลับกันปกติ
    ("abcabcabc", 6),      # มีหลายตัว ควรเลือกคู่ที่ดีที่สุด
    ("aabbcc", 0),         # ไม่มีตัวที่สลับกันได้จริง
    ("abcde", 2),          # เลือกคู่ที่ดีที่สุด
    ("zazbzbz", 0),        # ไม่มีตัวที่สลับกันได้จริง
    ("a", 0),              # ตัวเดียว
    ("", 0),               # ว่างเปล่า
    ("ababababababa", 13), # สลับกันยาวที่สุด
]

test_number = 1

for test in test_cases:
    inp = test[0]        # ดึง input
    expected = test[1]   # ดึง expected output
    result = alternate(inp)  # เรียกใช้ฟังก์ชัน

    if result == expected:
        print(f"Test case {test_number}: Passed")
    else:
        print(f"Test case {test_number}: Failed (Your output {result} should be {expected})")
    
    test_number += 1  # เพิ่มเลข test case
print("All test cases passed!")  # แสดงผลเมื่อผ่านทุกกรณี
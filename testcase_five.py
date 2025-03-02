def gridChallenge(grid):
    # Write your code here
    rows_item = []
    for item in grid:
        items = list(item)
        items.sort()
        rows_item.append(items)
    for i in range(len(rows_item[0])):
        for j in range(1, len(rows_item)):
            if rows_item[j][i] < rows_item[j-1][i]:
                return "NO"
    
    return "YES"

test_cases = [
    (["abc", "def", "ghi"], "YES"),  # กรณีที่แถวและคอลัมน์เรียงตามลำดับตัวอักษร โดยแถวจะเรียงแบบเรียงต่อไปตัวถัดไป
    (["abc", "fde", "ghi"], "YES"),  # มีแถวที่เรียงไม่ได้
    (["axb"], "YES"),  # กรณีขนาดเล็กสุดที่แถวไม่เรียง
    (["aaa", "aaa", "aaa"], "YES"),  # ทุกตัวเหมือนกัน
    (["abcd", "bcde", "cdef", "defg"], "YES"),  # กรณีที่ grid ขนาด 4*4 เรียงกันทั้งแถวและคอลัมน์
    (["a", "b", "c"], "YES"),  # มีแค่คอลัมน์เดียว แต่เรียงกันจาก a - z
    (["c", "b", "a"], "NO"),  # มีแค่คอลัมน์เดียว แต่เรียงแบบย้อนกลับ (z -> y -> x)
    (["az", "by", "cx"], "NO"),  # ตัวอักษรกระจัดกระจาย แต่ไม่เรียงทั้งแถวและคอลัมน์
    (["aa", "bb", "cc"], "YES"),  # ตัวอักษรซ้ำกันเป็นกลุ่ม แต่เรียงทั้งแถวและคอลัมน์
    (["zy", "wx", "vu"], "NO"),  # กรณีที่ลำดับตัวอักษรไม่เรียงกันจาก a - z
    (["mnop", "qrst", "uvwx", "yzab"], "NO"),  # กรณีที่ตัวอักษรเรียงกันทั้งแถวและคอลัมน์ แต่เมื่อถึง z แล้ววนกลับไป a
    (["abc"], "YES"),  # กรณีมีเพียง 1 แถว และตัวอักษรเรียงตามลำดับ
    (["aab", "abb", "bcc"], "YES"),  # กรณีตัวอักษรซ้ำกันในแถวและคอลัมน์
    (["abc", "ade", "efg"], "YES"),  # กรณีที่แถวและคอลัมน์เรียงตามลำดับตัวอักษร (คอลัมน์ : a a e, b d f และ c e g)
    (["zyx", "wvu", "tsr"], "NO")  # กรณีแถวที่เรียงไม่ได้
]

all_passed = True  # ตัวแปรบอกว่าทุกเทสต์ pass หรือไม่ 

for i in range(len(test_cases)):  
    grid, expected = test_cases[i]  # ดึงค่าจาก test_cases ทีละชุด
    result = gridChallenge(grid)  

    if result == expected:  
        print("Test case", i + 1, ": PASS")  
    else: 
        print("Test case", i + 1, ": FAIL")  
        all_passed = False  

if all_passed == True:  
    print("All test cases passed!")  
else:  
    print("Some test cases failed.")  

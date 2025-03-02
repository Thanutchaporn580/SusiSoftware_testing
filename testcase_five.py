import unittest

def gridChallenge(grid):
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

class TestGridChallengeFunction(unittest.TestCase):

    def test_grid_challenge(self):
        test_cases = [
            (["abc", "def", "ghi"], "YES"),  # กรณีที่แถวและคอลัมน์เรียงตามลำดับตัวอักษร โดยแถวจะเรียงแบบเรียงต่อไปตัวถัดไป
            (["abc", "fde", "ghi"], "YES"),  # มีแถวที่เรียงไม่ได้ แต่ยังคงผ่าน
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

        for grid, expected in test_cases:
            with self.subTest(grid=grid):
                self.assertEqual(gridChallenge(grid), expected)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGridChallengeFunction)
    runner = unittest.TextTestRunner(verbosity=2)
    results = runner.run(suite)
    
    total_tests = results.testsRun
    passed_tests = total_tests - len(results.failures) - len(results.errors)
    percentage_passed = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
    
    print(f"Test Passed: {passed_tests} จาก {total_tests} ({percentage_passed:.2f}%)")

if __name__ == '__main__':
    main()

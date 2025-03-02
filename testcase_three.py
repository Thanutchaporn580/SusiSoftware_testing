def caesarCipher(s, k):
    def transform(char):
        if char.islower():
            return chr((ord(char) - ord('a') + k) % 26 + ord('a'))
        if char.isupper():
            return chr((ord(char) - ord('A') + k) % 26 + ord('A'))
        else:
            return char
    
    characters = list(s)
    
    return "".join(map(transform, characters))

def test_caesarCipher():
    # lowercase
    assert caesarCipher("abc", 2) == "cde"
    assert caesarCipher("xyz", 2) == "zab"  # 'z' -> 'a'
    assert caesarCipher("morning", 5) == "rtwsnsl"

    # uppercase
    assert caesarCipher("ABC", 3) == "DEF"
    assert caesarCipher("XYZ", 3) == "ABC"  # 'Z' -> 'A'
    assert caesarCipher("MORNING", 7) == "TVYUPUN"

    # mixed case
    assert caesarCipher("GoodMorning", 4) == "KsshQsvrmrk"

    # special characters
    assert caesarCipher("Hello, World!", 3) == "Khoor, Zruog!"
    assert caesarCipher("123-456!", 5) == "123-456!"

    # k = 0 (ค่าคงเดิม)
    assert caesarCipher("NoChange", 0) == "NoChange"

    # k > 26 (ผลลัพธ์ต้องเหมือน k % 26)
    assert caesarCipher("abc", 26) == "abc"  # 26 คือรอบเต็ม
    assert caesarCipher("xyz", 28) == "zab"  # 28 % 26 = 2
    assert caesarCipher("ABC", 52) == "ABC"  # 52 % 26 = 0 (ไม่เปลี่ยนแปลง)

    # k เป็นค่าลบ (reverse)
    assert caesarCipher("def", -2) == "bcd"
    assert caesarCipher("XYZ", -3) == "UVW"
    assert caesarCipher("aBc", -1) == "zAb"  # เลื่อนย้อนกลับจาก 'a' -> 'z'

    # Empty string
    assert caesarCipher("", 5) == ""

    print("All test cases passed!")

test_caesarCipher()

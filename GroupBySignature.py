from collections import defaultdict

def group_by_signature(words: list) -> list:
    #pass
    groups = defaultdict(list)

    for word in words:
        # ข้ามคำที่ว่างเปล่า หรือคำที่มีอักขระที่ไม่ใช่ a-z (หรือ A-Z)
        if not word or not word.isalpha():
            continue

        # สร้าง Signature โดยการแปลงเป็นตัวพิมพ์เล็กและเรียงลำดับตัวอักษร
        signature = "".join(sorted(word.lower()))

        # จัดกลุ่มตาม Signature
        groups[signature].append(word)

    return list(groups.values())

if __name__ == "__main__":
    # Example 1
    words = ["abc", "bca", "cab", "bac", "xyz", "yxz", "zxy", "dog"]
    print(group_by_signature(words))
    # Output: [["abc", "bca", "cab", "bac"], ["xyz", "yxz", "zxy"], ["dog"]]

    # Example 2
    words = ["apple", "pale", "leap", "plea", "papel", "hello"]
    print(group_by_signature(words))
    # Output: [["apple", "papel"], ["pale", "leap", "plea"], ["hello"]]

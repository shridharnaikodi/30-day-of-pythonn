#Easy


def count_vowels(s):
    vowels = "aeiou"
    count = 0

    s = s.lower()

    for char in s:
        if char in vowels:
            count += 1

    return count


# Test Cases
print(count_vowels("Programming"))   # 3
print(count_vowels("PYTHON"))        # 1
print(count_vowels("AEIOU"))         # 5



#Medium

def missing_number(nums):
    n = max(nums)

    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)

    return expected_sum - actual_sum


# Test Cases
print(missing_number([1, 2, 4, 5]))      # 3
print(missing_number([2, 3, 1, 5]))      # 4
print(missing_number([1, 3]))            # 2



#Interview Level


def valid_anagram(s1, s2):

    if len(s1) != len(s2):
        return False

    freq1 = {}
    freq2 = {}

    for char in s1:
        freq1[char] = freq1.get(char, 0) + 1

    for char in s2:
        freq2[char] = freq2.get(char, 0) + 1

    return freq1 == freq2


# Test Cases
print(valid_anagram("listen", "silent"))    # True
print(valid_anagram("hello", "world"))      # False
print(valid_anagram("race", "care"))        # True
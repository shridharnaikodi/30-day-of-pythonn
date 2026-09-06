#easy
# Q1 : Given a list of integers, count how many numbers are even.
def count_even(nums):
    count = 0

    for num in nums:
        if num % 2 == 0:
            count += 1

    return count

#test cases
print(count_even([1, 2, 4, 7, 8, 11]))


#medium
# Q2:Given a list of integers, create a new list containing each number only once, while keeping the original order.
def remove_duplicates(nums):
    seen = set()
    result = []

    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result

#test cases
print(remove_duplicates([1, 2, 2, 3, 1, 4, 3]))

#interview level
# Q3: Given a string, find the first character that appears only once.
def first_non_repeating(s):
    frequency = {}

    # Step 1: Count each character
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1

    # Step 2: Find the first character with frequency 1
    for char in s:
        if frequency[char] == 1:
            return char

    return None


print(first_non_repeating("aabbcddee"))
print(first_non_repeating("aabb"))
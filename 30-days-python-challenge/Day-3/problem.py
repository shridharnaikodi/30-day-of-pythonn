#easy

def largest_number(nums):
    largest = nums[0]

    for num in nums:
        if num > largest:
            largest = num

    return largest
#test Cases
print(largest_number([3, 5, 2, 8, 1]))      # 8
print(largest_number([-1, -5, -3, -2]))      # -1   
print(largest_number([10, 20, 30, 40, 50]))  # 50


#medium


def reverse_string(sentence):

    words = sentence.split()

    reversed_words = []

    for word in words:
        reversed_words.append(word[::-1])

    return " ".join(reversed_words)

# Test Cases
print(reverse_string("Hello World"))          # "olleH dlroW"
print(reverse_string("Python is fun"))       # "nohtyP si nuf"
print(reverse_string("I love programming"))  # "I evol gnimmargorp"


#interview level


def duplicate_elements(nums):

    seen = set()
    duplicates = set()

    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)

# Test Cases
print(duplicate_elements([1, 2, 3, 2, 4, 5, 4]))  # [2, 4]
print(duplicate_elements([1, 2, 3, 4, 5]))        # []
print(duplicate_elements([1, 1, 1, 1]))           # [1]
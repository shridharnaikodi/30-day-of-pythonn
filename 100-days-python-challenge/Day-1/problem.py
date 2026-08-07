#Easy


# Write a function that takes a list of integers and returns the sum of all even numbers
def sum_even_num(numbers):
    total = 0
    for num in numbers:
        if(num%2 == 0):
            total += num
    return total
print(sum_even_num([1,2,3,4,5,6,7,8,9,10]))



#Medium

#Write a function that returns the second largest unique number in a list
def second_number(num):
    unique_num  = list(set(num))
    if len(unique_num) < 2:
        return None
    unique_num.sort()
    return unique_num[-2]
print(second_number([10,30,64,63,97,86,23]))


#Interview Level

#Given a string, return the first character that appears only once
def first_unique_char(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in string:
        if char_count[char] == 1:
            return char
    return None

print(first_unique_char("abccba"))  
print(first_unique_char("abcabc"))  
print(first_unique_char("abcdef"))  
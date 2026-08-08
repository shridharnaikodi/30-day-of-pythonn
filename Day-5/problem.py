#easy 
#Q1:Write a function that finds the character that appears most frequently in a string.

def chara(string):
    freq = {}
    for char in string:
        freq[char] = freq.get(char,0) + 1
    highest = 0
    for char in freq:
        if freq[char] > highest:
            highest = freq[char]
    for char in freq:
        if freq[char] == highest:
            return char


#test cases
print(chara("programming"))
print(chara("hello world"))


#medium
#Q2:Given a list of words, create a dictionary where:
            #The key is the word length.
            #The value is a list of words having that length.

def length(words):
  result = {}

  for word in words:
    length = len(word)

    if length not in result:
      result[length] = []
    result[length].append(word)
  return result

#test cases

print(length(["cat", "dog", "apple", "hi", "book"]))

#interview
#Q3: Given two lists, return the elements that are present in both lists, without repeating them.


def common_elements(list1, list2):
    result = []

    for num in list1:
        if num in list2 and num not in result:
            result.append(num)

    return result


print(common_elements(
    [1, 2, 2, 3, 4, 5],
    [2, 2, 4, 4, 6]
))
      



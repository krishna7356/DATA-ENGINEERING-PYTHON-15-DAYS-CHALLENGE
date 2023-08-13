# Day 2: The Anagram Challenge

# Determine if two strings are anagrams of each other.


# Your task is to write a Python function that checks whether two given strings are anagrams of each other. Anagrams are words or phrases formed by rearranging the letters of another.

# method 1
def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    if len(str1) != len(str2):
        return False
    
    char_frequency_str1 = {}
    char_frequency_str2 = {}
    
    for char in str1:
        char_frequency_str1[char] = char_frequency_str1.get(char, 0) + 1
        
    for char in str2:
        char_frequency_str2[char] = char_frequency_str2.get(char, 0) + 1
    
    return char_frequency_str1 == char_frequency_str2

string1 = "listen"
string2 = "silent"
print(are_anagrams(string1, string2))  # Output: True

# method 2

def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)

string1 = "listen"
string2 = "silent"
print(are_anagrams(string1, string2))  # Output: True

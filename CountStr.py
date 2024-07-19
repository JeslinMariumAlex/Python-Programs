string = input("Enter the string: ")
alphabet = digit = special_character = word = lowercase = uppercase = vowel = space = 0
vowels = "AEIOUaeiou"
for ch in string:
    if ch.isalpha():
        alphabet += 1
        if ch in vowels:
            vowel += 1
        if ch.islower():
            lowercase += 1
        else:
            uppercase += 1
    elif ch.isdigit():
        digit += 1
    elif ch.isspace():
        space += 1
        word += 1
    else:
        special_character += 1
print("Total Alphabets:", alphabet)
print("Total Digits:", digit)
print("Total Uppercase letters:", uppercase)
print("Total Lowercase letters:", lowercase)
print("Total Space:", space)
print("Total Vowels:", vowel)
print("Total Special Characters:", special_character)
print("Total Words:", (word + 1))

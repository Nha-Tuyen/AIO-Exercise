string = input("Enter a string: ").lower()

# decompose each character in the string
char_count = {}


def count_chars(str):
    for char in str:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

print(count_chars(string))

# Caesar Scipher Cracker
# Programmed in python by Josh Tozer


# Split the scipher into letters
def split_string(string):
    return [l for l in string if l.isalpha()]

# Count the number of occurences of each letter in the scipher
def letter_count(string):
    counts = dict()
    letters = split_string(string)

    for l in letters:
        if l in counts:
            counts[l] += 1
        else:
            counts[l] = 1
    return counts

def descipher(shift, string):
    plaintext = ''
    for l in string:
        if l.isalpha():
            plaintext += chr((ord(l) - 97 - shift) % 26 + 97)
        elif l == ' ':
            plaintext += l
    return plaintext

print('Please enter a Caesar scipher:')
string = input()
string = string.lower()
letters = letter_count(string)
max_freq= max(letters.values())
max_letter = [k for k, v in letters.items() if v == max_freq]

print('If the desciphered language is english, usually the sciphertext letter with the greatest frequency will represent the plaintext "e", but if that doesn\'t work other good choices are: "a", "o", and "t".')
print('Which letter do you want to select as the most frequent in the plaintext? (usually "e", "a", "o" or "t").')
shift_letter= input()

print('The letter(s) with the greatest frequency are: ')
print(max_letter)
print("Choose one of the above letters to be the key to determine the shift:")
response = input()

response = response.lower()
shift = ord(response) - ord(shift_letter)
print('plaintext:')
print(descipher(shift, string))



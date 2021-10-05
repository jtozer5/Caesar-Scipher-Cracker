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

print('**************************************************')
print('If the desciphered language is english, usually the sciphertext letter with the greatest frequency will represent the plaintext "e", but if that doesn\'t work other good choices are: "a", "o", and "t".\n')
print('Which key letter would you like to select? (usually "e", "a", "o" or "t").')
print('Or type "done" to quit.')
shift_letter = ''
response = ''
while (True):
    shift_letter= input()
    if len(shift_letter) == 1:
        print('The letter(s) with the greatest frequency are: ')
        print(*max_letter, sep = ", ")
        print("Choose one of above most frequent letters:")

        response = input()

        if len(response) == 1:
            response = response.lower()
            shift = ord(response) - ord(shift_letter)
            print('shifted text:')
            print(descipher(shift, string) + '\n')
            print('If that worked please enter "done", otherwise enter a new key letter.')
        elif response == 'done':
            break
        else:
            print('Invalid input.  Please only enter one letter or "done".')
    elif shift_letter == 'done':
        break
    else:
        print('Invalid input.  Please only enter one letter or "done".')



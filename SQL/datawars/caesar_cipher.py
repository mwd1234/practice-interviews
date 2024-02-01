import string

letters = list(string.ascii_uppercase)

shift_5 = letters[5:] + letters[:5]

def shift_letters(letters, shift):
    letters = ''.join([letters[(i + shift) % len(letters)] for i in range(len(letters))])
    
    return letters 


spanish_letters = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
print(shift_letters(spanish_letters, 9))
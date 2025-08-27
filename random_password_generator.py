import random 
import string

def generate_password():
    
    length = int(input("Enter a desired password length: ").strip())

    if length < 4:
        print("Password length must be at least 4 characters!")
        return
    
    include_uppercase = input("Include uppercase? (yes/no): ").strip().lower()
    include_specials = input("Include special characters? (yes/no): ").strip().lower()
    include_digits = input("Include digits? (yes/no): ").strip().lower()

    lower = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase == 'yes' else ''
    specials =  string.punctuation if include_specials == 'yes' else ''
    digits = string.digits if include_digits == 'yes' else ''
    all_chars = lower + uppercase + specials + digits

    required_chars = []

    if include_uppercase == 'yes':
        required_chars.append(random.choice(uppercase))
    if include_specials == 'yes':
        required_chars.append(random.choice(specials))
    if include_digits == 'yes':
        required_chars.append(random.choice(digits))

    remaining_chars = length - len(required_chars)
    password = required_chars

    for _ in range(remaining_chars):
        char =  random.choice(all_chars)
        password.append(char)
    
    random.shuffle(password)
    return "".join(password)



if __name__ == '__main__':

    password = generate_password()
    print(password)
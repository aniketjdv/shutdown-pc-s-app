import msvcrt
import sys

def get_password(prompt="Enter your password: "):
    print(prompt, end='', flush=True)
    password = []
    while True:
        char = msvcrt.getch()
        # 13 is the ASCII code for Enter
        if char in [b'\r', b'\n']:
            print()
            break
        # 8 is the ASCII code for Backspace
        elif char == b'\x08':
            if password:
                del password[-1]
                sys.stdout.write('\b \b')  # Erase the last character from the screen
        else:
            password.append(char.decode('utf-8'))
            sys.stdout.write('*')  # Print '*' instead of the actual character

    return ''.join(password)

# Example usage:
password = get_password()
print("Password entered:", password)

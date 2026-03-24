import random
import string
import os
import sys
from colorama import Fore, init
import pyfiglet

init(autoreset=True)

def banner():
    os.system("clear")
    print(Fore.CYAN + pyfiglet.figlet_format("MIXED PASS GEN"))
    print(Fore.YELLOW + "1. Generate Passwords")
    print(Fore.YELLOW + "2. Exit\n")

def generate_number_password(length):
    return "".join(random.choice(string.digits) for _ in range(length))

def generate_letter_number_password(letters_count, numbers_count):
    pw = "".join(random.choice(string.ascii_letters) for _ in range(letters_count))
    pw += "".join(random.choice(string.digits) for _ in range(numbers_count))
    return "".join(random.sample(pw, len(pw)))  # shuffle

def generate_letter_number_symbol_password(letters_count, numbers_count, symbols_count):
    pw = "".join(random.choice(string.ascii_letters) for _ in range(letters_count))
    pw += "".join(random.choice(string.digits) for _ in range(numbers_count))
    pw += "".join(random.choice(string.punctuation) for _ in range(symbols_count))
    return "".join(random.sample(pw, len(pw)))  # shuffle

def password_strength(pw):
    score = 0
    if any(c.islower() for c in pw): score += 1
    if any(c.isupper() for c in pw): score += 1
    if any(c.isdigit() for c in pw): score += 1
    if any(c in string.punctuation for c in pw): score += 1
    if len(pw) >= 8: score += 1
    if score <= 2: return Fore.RED + "Weak"
    elif score <= 4: return Fore.YELLOW + "Medium"
    else: return Fore.GREEN + "Strong"

def main():
    while True:
        banner()
        choice = input(Fore.GREEN + "Select option: ")

        if choice == "1":
            try:
                total = int(input("How many passwords to generate? "))
            except:
                print(Fore.RED + "Invalid number")
                input("Press Enter...")
                continue

            filename = input("Save file name (e.g., passwords.txt): ")

            passwords = []
            with open(filename, "w") as f:
                for _ in range(total):
                    pw_type = random.choice([1,2,3])
                    if pw_type == 1:
                        pw = generate_number_password(random.randint(6,8))
                    elif pw_type == 2:
                        pw = generate_letter_number_password(random.randint(3,6), random.randint(2,4))
                    else:
                        pw = generate_letter_number_symbol_password(random.randint(3,6), random.randint(2,4), random.randint(1,2))
                    f.write(pw + "\n")
                    passwords.append(pw)

            print(Fore.GREEN + f"\n{total} passwords saved to {filename}\n")
            print(Fore.CYAN + "Passwords & Strength:")
            for pw in passwords:
                print(f"{pw}  [{password_strength(pw)}]")

            input("\nPress Enter to continue...")

        elif choice == "2":
            print(Fore.YELLOW + "Goodbye!")
            sys.exit()
        else:
            print(Fore.RED + "Invalid option")
            input("Press Enter...")

if __name__ == "__main__":
    main()

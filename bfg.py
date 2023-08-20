#wer

import random
import time
import pyautogui
from time import sleep

def generate_password():
    return str(random.randint(100000, 999999))

def save_passwords_to_file(passwords, file_name):
    with open(file_name, 'w') as file:
        for password in passwords:
            file.write(password + '\n')

def main():
    print("")
    sleep(1)
    print("Hey, this might take a while. Go get some coconut water or something.")
    print("And don't forget to delete the generated files (they are in the same folder as 'bfg.py').")

    num_passwords = 30000000
    passwords = [generate_password() for _ in range(num_passwords)]

    timestamp = time.strftime('%Y%m%d%H%M%S')
    file_name = f'passwords_{timestamp}.txt'

    save_passwords_to_file(passwords, file_name)

    print(f"{num_passwords} passwords generated and saved in '{file_name}'.")

    for _ in range(20):
        pyautogui.press('backspace')

    sleep(20)

    pyautogui.press("enter")

    sleep(2)

    with open(file_name, "r") as file:
        for line in file:
            password = line.strip()
            pyautogui.typewrite(password[:6])
            pyautogui.press("enter")
            pyautogui.press('backspace', presses=6)  # Delete the first 6 digits

    sleep(10)

    for _ in range(20):
        pyautogui.press('backspace')

if __name__ == "__main__":
    main()

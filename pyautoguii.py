# import pyautogui
# from time import sleep

# n = int(input())
# sleep(3)
# for i in range(1,n+1):
#     pyautogui.write('#'*i)
#     if i!=n:
#         pyautogui.press('enter')

import pyautogui
from time import sleep

# Get the number of rows for the pyramid from the user
n = int(input("Enter the number of rows for the pyramid: "))
sleep(3)  # Pause to allow the user to switch to the desired application

# Loop to create each row of the pyramid
for i in range(1, n + 1):
    # Calculate the spaces needed for center alignment
    spaces = ' ' * (n - i)
    # Calculate the pyramid row with '#'
    row = spaces + '#' * (2 * i - 1)
    
    # Use pyautogui to type the row and press Enter
    pyautogui.write(row)
    pyautogui.press('enter')

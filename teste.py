from time import sleep 
from pyautogui import typewrite 

message = input('type the message: ')

repetitions = int(input('how many times? '))

sleep(2)

for i in range(repetitions):
    
    typewrite(message + '\n')
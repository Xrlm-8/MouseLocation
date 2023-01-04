import pyautogui  #as = renomear
from pyautogui import displayMousePosition

displayMousePosition()

pyautogui.alert('This is an alert box.')
pyautogui.confirm('Shall I proceed?')
pyautogui.confirm('Enter option.', buttons=['A', 'B', 'C'])
pyautogui.prompt('What is your name?')
pyautogui.password('Enter password (text will be hidden)')
im1 = pyautogui.screenshot()
button7location = pyautogui.locateOnScreen('button.png')
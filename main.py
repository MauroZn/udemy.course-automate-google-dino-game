import pyautogui
from selenium import webdriver
import time
import keyboard

url = "https://elgoog.im/dinosaur-game/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(url)

currentMouseX, currentMouseY = pyautogui.position()
time.sleep(1)
pyautogui.moveTo(260, 775)
pyautogui.click()

def jump():
    if not hasattr(jump, "has_run"):
        pyautogui.press('space')
        jump.has_run = True
    x, y = pyautogui.position()
    r, g, b = pyautogui.pixel(x, y)
    if r  != 255 and g != 255 and b != 255:
        pyautogui.press('space')


while True:
    jump()
    if keyboard.is_pressed("q"):
        driver.close()
        break
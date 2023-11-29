import pyautogui
import time
#pyautogui.mouseInfo()


def clicker():
    while True:
        pyautogui.leftClick(x = 385, y = 503)

def world():
    x = 186
    y = 403

    color = pyautogui.pixel(x,y)

    if color == (85,18,11):
        world = 'Mars'
    elif color == (217,229,235):
        world = 'Moon'
    elif color == (235,221,175):
        world = 'Earth'
    
    return world

def collector(world):
    if world == 'Mars':
        location_2stack_coin = pyautogui.locateOnScreen('Mars/mars_2stack_coin.png')
        location_4stack_coin = pyautogui.locateOnScreen('Mars/mars_4stack_coin.png')
        location_6stack_coin = pyautogui.locateOnScreen('Mars/mars_6stack_coin.png')
        location_chest = pyautogui.locateOnScreen('Mars/mars_chest.png')
        location_close_button = pyautogui.locateOnScreen('Mars/mars_close_button.png')
        location_equip_button = pyautogui.locateOnScreen('Mars/mars_equip_button.png')
        location_fortune_box = pyautogui.locateOnScreen('Mars/mars_fortune_box.png')
        location_grab_button = pyautogui.locateOnScreen('Mars/mars_grab_button.png')
        location_loot_button = pyautogui.locateOnScreen('Mars/mars_loot_button.png')
        location_open_now_button = pyautogui.locateOnScreen('Mars/mars_open_now_button.png')

        pyautogui.click(location_2stack_coin)
        pyautogui.click(location_4stack_coin)
        pyautogui.click(location_6stack_coin)
        pyautogui.click(location_chest)
        pyautogui.click(location_close_button)
        pyautogui.click(location_equip_button)
        pyautogui.click(location_fortune_box)
        pyautogui.click(location_grab_button)
        pyautogui.click(location_loot_button)
        pyautogui.click(location_open_now_button)
    elif world == 'Moon':
        location_2stack_coin = pyautogui.locateOnScreen('Moon/moon_2stack_coin.png')
        location_4stack_coin = pyautogui.locateOnScreen('Moon/moon_4stack_coin.png')
        location_6stack_coin = pyautogui.locateOnScreen('Moon/moon_6stack_coin.png')
        location_chest = pyautogui.locateOnScreen('Moon/moon_crate.png')
        #location_close_button = pyautogui.locateOnScreen('Moon/Moon_close_button.png')
        location_equip_button = pyautogui.locateOnScreen('Moon/moon_equip_button.png')
        location_fortune_box = pyautogui.locateOnScreen('Moon/moon_fortune_box.png')
        location_grab_button = pyautogui.locateOnScreen('Moon/moon_grab_button.png')
        location_loot_button = pyautogui.locateOnScreen('Moon/moon_loot_button.png')
        location_open_now_button = pyautogui.locateOnScreen('Moon/moon_open_now_button.png')

        pyautogui.click(location_2stack_coin)
        pyautogui.click(location_4stack_coin)
        pyautogui.click(location_6stack_coin)
        pyautogui.click(location_chest)
        #pyautogui.click(location_close_button)
        pyautogui.click(location_equip_button)
        pyautogui.click(location_fortune_box)
        pyautogui.click(location_grab_button)
        pyautogui.click(location_loot_button)
        pyautogui.click(location_open_now_button)
    elif world == 'Earth':
        location_2stack_coin = pyautogui.locateOnScreen('Earth/Earth_2stack_coin.png')
        location_4stack_coin = pyautogui.locateOnScreen('Earth/Earth_4stack_coin.png')
        location_6stack_coin = pyautogui.locateOnScreen('Earth/Earth_6stack_coin.png')
        location_chest = pyautogui.locateOnScreen('Earth/Earth_crate.png')
        #location_close_button = pyautogui.locateOnScreen('Earth/Earth_close_button.png')
        location_equip_button = pyautogui.locateOnScreen('Earth/Earth_equip_button.png')
        location_fortune_box = pyautogui.locateOnScreen('Earth/Earth_fortune_box.png')
        location_grab_button = pyautogui.locateOnScreen('Earth/Earth_grab_button.png')
        location_loot_button = pyautogui.locateOnScreen('Earth/Earth_loot_button.png')
        location_open_now_button = pyautogui.locateOnScreen('Earth/Earth_open_now_button.png')

        pyautogui.click(location_2stack_coin)
        pyautogui.click(location_4stack_coin)
        pyautogui.click(location_6stack_coin)
        pyautogui.click(location_chest)
        #pyautogui.click(location_close_button)
        pyautogui.click(location_equip_button)
        pyautogui.click(location_fortune_box)
        pyautogui.click(location_grab_button)
        pyautogui.click(location_loot_button)
        pyautogui.click(location_open_now_button)
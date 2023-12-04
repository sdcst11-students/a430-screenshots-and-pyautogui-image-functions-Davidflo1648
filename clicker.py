import pyautogui
import time
#pyautogui.mouseInfo()


def clicker():
    time.sleep(2)
    while True:
        pyautogui.leftClick(x = 385, y = 503)

def world():
    x = 186
    y = 403

    color = pyautogui.pixel(x,y)

    world_name = None

    if color == (85,18,11):
        world_name = 'Mars'
    elif color == (217,229,235):
        world_name = 'Moon'
    elif color == (235,221,175):
        world_name = 'Earth'
    
    return world_name

def collector(world_name):
    if world_name == 'Mars':
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

        if location_2stack_coin is not None:
            pyautogui.click(location_2stack_coin)
        if location_4stack_coin is not None:
            pyautogui.click(location_4stack_coin)
        if location_6stack_coin is not None:
            pyautogui.click(location_6stack_coin)
        if location_chest is not None:
            pyautogui.click(location_chest)
        if location_close_button is not None:
            pyautogui.click(location_close_button)
        if location_equip_button is not None:
            pyautogui.click(location_equip_button)
        if location_fortune_box is not None:
            pyautogui.click(location_fortune_box)
        if location_grab_button is not None:
            pyautogui.click(location_grab_button)
        if location_loot_button is not None:
            pyautogui.click(location_loot_button)
        if location_open_now_button is not None:
            pyautogui.click(location_open_now_button)

    elif world_name == 'Moon':
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

        if location_2stack_coin is not None:
            pyautogui.click(location_2stack_coin)
        if location_4stack_coin is not None:
            pyautogui.click(location_4stack_coin)
        if location_6stack_coin is not None:
            pyautogui.click(location_6stack_coin)
        if location_chest is not None:
            pyautogui.click(location_chest)
        #if location_close_button is not None:
            #pyautogui.click(location_close_button)
        if location_equip_button is not None:
            pyautogui.click(location_equip_button)
        if location_fortune_box is not None:
            pyautogui.click(location_fortune_box)
        if location_grab_button is not None:
            pyautogui.click(location_grab_button)
        if location_loot_button is not None:
            pyautogui.click(location_loot_button)
        if location_open_now_button is not None:
            pyautogui.click(location_open_now_button)

    elif world_name == 'Earth':
        location_2stack_coin = pyautogui.locateOnScreen('Earth/earth_2stack_coin.png')
        location_4stack_coin = pyautogui.locateOnScreen('Earth/earth_4stack_coin.png')
        location_6stack_coin = pyautogui.locateOnScreen('Earth/earth_6stack_coin.png')
        location_chest = pyautogui.locateOnScreen('Earth/earth_bag.png')
        #location_close_button = pyautogui.locateOnScreen('Earth/Earth_close_button.png')
        location_equip_button = pyautogui.locateOnScreen('Earth/earth_equip_button.png')
        location_fortune_box = pyautogui.locateOnScreen('Earth/earth_fortune_box.png')
        location_grab_button = pyautogui.locateOnScreen('Earth/earth_grab_button.png')
        location_loot_button = pyautogui.locateOnScreen('Earth/earth_loot_button.png')
        location_open_now_button = pyautogui.locateOnScreen('Earth/earth_open_now_button.png')

        if location_2stack_coin is not None:
            pyautogui.click(location_2stack_coin)
        if location_4stack_coin is not None:
            pyautogui.click(location_4stack_coin)
        if location_6stack_coin is not None:
            pyautogui.click(location_6stack_coin)
        if location_chest is not None:
            pyautogui.click(location_chest)
        #if location_close_button is not None:
            #pyautogui.click(location_close_button)
        if location_equip_button is not None:
            pyautogui.click(location_equip_button)
        if location_fortune_box is not None:
            pyautogui.click(location_fortune_box)
        if location_grab_button is not None:
            pyautogui.click(location_grab_button)
        if location_loot_button is not None:
            pyautogui.click(location_loot_button)
        if location_open_now_button is not None:
            pyautogui.click(location_open_now_button)

#def mars_upgrades():
    #if pyautogui.pixelMatchesColor(212,199,199):
        #pyautogui.leftClick(847,631 or 804,483 or 805,327 or 1044,338 or 1030,479)

world_name = world()
collector(world_name)
clicker()
#mars_upgrades()
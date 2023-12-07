import pyautogui
import time
#pyautogui.mouseInfo()


def clicker():
    time.sleep(1)
    for i in range(20):
        pyautogui.leftClick(x = 385, y = 503)

def world():
    x = 465
    y = 552
    #color = pyautogui.pixel(x, y)
    #print(color)
    world_name = None
    if pyautogui.pixelMatchesColor(x, y, (99,32,24), tolerance=10):
        world_name = 'Mars'
    elif pyautogui.pixelMatchesColor(x, y, (218,231,239), tolerance=10):
        world_name = 'Moon'
    elif pyautogui.pixelMatchesColor(x, y, (242,225,174), tolerance=10):
        world_name = 'Earth'

    return world_name

def findImage(filename):
    try:
        imageLoc = pyautogui.locateOnScreen(filename,confidence=0.8)
        return imageLoc
    except:
        print(f"{filename} not found")
        return None

def collector(world_name):
    if world_name == 'Mars':
        location_2stack_coin = findImage('Mars/mars_2stack_coin.png')
        location_4stack_coin = findImage('Mars/mars_4stack_coin.png')
        location_6stack_coin = pyautogui.locateOnScreen('Mars/mars_6stack_coin.png',confidence=0.8)
        location_chest = pyautogui.locateOnScreen('Mars/mars_chest.png',confidence=0.8)
        location_close_button = pyautogui.locateOnScreen('Mars/mars_close_button.png',confidence=0.8)
        location_equip_button = pyautogui.locateOnScreen('Mars/mars_equip_button.png',confidence=0.8)
        location_fortune_box = pyautogui.locateOnScreen('Mars/mars_fortune_box.png',confidence=0.8)
        location_grab_button = pyautogui.locateOnScreen('Mars/mars_grab_button.png',confidence=0.8)
        location_loot_button = pyautogui.locateOnScreen('Mars/mars_loot_button.png',confidence=0.8)
        location_open_now_button = pyautogui.locateOnScreen('Mars/mars_open_now_button.png',confidence=0.8)
        #print(location_2stack_coin)

        if location_2stack_coin is not None:
            pyautogui.leftClick(location_2stack_coin)
        if location_4stack_coin is not None:
            pyautogui.leftClick(location_4stack_coin)
        if location_6stack_coin is not None:
            pyautogui.leftClick(location_6stack_coin)
        if location_chest is not None:
            pyautogui.leftClick(location_chest)
        if location_close_button is not None:
            pyautogui.leftClick(location_close_button)
        if location_equip_button is not None:
            pyautogui.leftClick(location_equip_button)
        if location_fortune_box is not None:
            pyautogui.leftClick(location_fortune_box)
        if location_grab_button is not None:
            pyautogui.leftClick(location_grab_button)
        if location_loot_button is not None:
            pyautogui.leftClick(location_loot_button)
        if location_open_now_button is not None:
            pyautogui.leftClick(location_open_now_button)


    elif world_name == 'Moon':
        location_2stack_coin = pyautogui.locateOnScreen('Moon/moon_2stack_coin.png',confidence=0.8)
        location_4stack_coin = pyautogui.locateOnScreen('Moon/moon_4stack_coin.png',confidence=0.8)
        location_6stack_coin = pyautogui.locateOnScreen('Moon/moon_6stack_coin.png',confidence=0.8)
        location_crate = pyautogui.locateOnScreen('Moon/moon_crate.png',confidence=0.8)
        #location_close_button = pyautogui.locateOnScreen('Moon/Moon_close_button.png',confidence=0.8)
        location_equip_button = pyautogui.locateOnScreen('Moon/moon_equip_button.png',confidence=0.8)
        location_fortune_box = pyautogui.locateOnScreen('Moon/moon_fortune_box.png',confidence=0.8)
        location_grab_button = pyautogui.locateOnScreen('Moon/moon_grab_button.png',confidence=0.8)
        location_loot_button = pyautogui.locateOnScreen('Moon/moon_loot_button.png',confidence=0.8)
        location_open_now_button = pyautogui.locateOnScreen('Moon/moon_open_now_button.png',confidence=0.8)

        if location_2stack_coin is not None:
            pyautogui.leftClick(location_2stack_coin)
        if location_4stack_coin is not None:
            pyautogui.leftClick(location_4stack_coin)
        if location_6stack_coin is not None:
            pyautogui.leftClick(location_6stack_coin)
        if location_crate is not None:
            pyautogui.leftClick(location_crate)
        #if location_close_button is not None:
            #pyautogui.leftClick(location_close_button)
        if location_equip_button is not None:
            pyautogui.leftClick(location_equip_button)
        if location_fortune_box is not None:
            pyautogui.leftClick(location_fortune_box)
        if location_grab_button is not None:
            pyautogui.leftClick(location_grab_button)
        if location_loot_button is not None:
            pyautogui.leftClick(location_loot_button)
        if location_open_now_button is not None:
            pyautogui.leftClick(location_open_now_button)

            pyautogui.click(location_open_now_button)

    elif world_name == 'Earth':
        location_2stack_coin = pyautogui.locateOnScreen('Earth/earth_2stack_coin.png',confidence=0.8)
        location_4stack_coin = pyautogui.locateOnScreen('Earth/earth_4stack_coin.png',confidence=0.8)
        location_6stack_coin = pyautogui.locateOnScreen('Earth/earth_6stack_coin.png',confidence=0.8)
        location_bag = pyautogui.locateOnScreen('Earth/earth_bag.png',confidence=0.8)
        #location_close_button = pyautogui.locateOnScreen('Earth/Earth_close_button.png',confidence=0.8)
        location_equip_button = pyautogui.locateOnScreen('Earth/earth_equip_button.png',confidence=0.8)
        location_fortune_box = pyautogui.locateOnScreen('Earth/earth_fortune_box.png',confidence=0.8)
        location_grab_button = pyautogui.locateOnScreen('Earth/earth_grab_button.png',confidence=0.8)
        location_loot_button = pyautogui.locateOnScreen('Earth/earth_loot_button.png',confidence=0.8)
        location_open_now_button = pyautogui.locateOnScreen('Earth/earth_open_now_button.png',confidence=0.8)

        if location_2stack_coin is not None:
            pyautogui.leftClick(location_2stack_coin)
        if location_4stack_coin is not None:
            pyautogui.leftClick(location_4stack_coin)
        if location_6stack_coin is not None:
            pyautogui.leftClick(location_6stack_coin)
        if location_bag is not None:
            pyautogui.leftClick(location_bag)
        #if location_close_button is not None:
            #pyautogui.leftClick(location_close_button)
        if location_equip_button is not None:
            pyautogui.leftClick(location_equip_button)
        if location_fortune_box is not None:
            pyautogui.leftClick(location_fortune_box)
        if location_grab_button is not None:
            pyautogui.leftClick(location_grab_button)
        if location_loot_button is not None:
            pyautogui.leftClick(location_loot_button)
        if location_open_now_button is not None:
            pyautogui.leftClick(location_open_now_button)

def mars_upgrades():
    if pyautogui.pixelMatchesColor(1030, 479, (212,199,199), tolerance=10):
        pyautogui.leftClick(1030,479)
    elif pyautogui.pixelMatchesColor(847,631, (212,199,199), tolerance=10):
        pyautogui.leftClick(847,631)
    elif pyautogui.pixelMatchesColor(804,483, (212,199,199), tolerance=10):
        pyautogui.leftClick(804,483)
    elif pyautogui.pixelMatchesColor(805,327, (212,199,199), tolerance=10):
        pyautogui.leftClick(805,327)
    elif pyautogui.pixelMatchesColor(1044,388, (212,199,199), tolerance=10):
        pyautogui.leftClick(1044,388)



pyautogui.alert("Start?")
while True:
    clicker()
    world_name = world()
    print(world_name)
    collector(world_name)
    mars_upgrades()

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
        images = ['Mars/mars_2stack_coin.png','Mars/mars_4stack_coin.png','Mars/mars_6stack_coin.png','Mars/mars_chest.png','Mars/mars_close_button.png','Mars/mars_equip_button.png','Mars/mars_fortune_box.png','Mars/mars_grab_button.png','Mars/mars_loot_button.png','Mars/mars_open_now_button.png']
        for i in images:
            tImg = findImage(i)
            if tImg != None:
                pyautogui.leftClick(tImg)
    elif world_name == 'Moon':
        images = ['Moon/moon_2stack_coin.png','Moon/moon_4stack_coin.png','Moon/moon_6stack_coin.png','Moon/moon_crate.png','Moon/moon_close_button.png','Moon/moon_equip_button.png','Moon/moon_fortune_box.png','Moon/moon_grab_button.png','Moon/moon_loot_button.png','Moon/moon_open_now_button.png']
        for i in images:
            tImg = findImage(i)
            if tImg != None:
                pyautogui.leftClick(tImg)
    elif world_name == 'Earth':
        images = ['Earth/earth_2stack_coin.png','Earth/earth_4stack_coin.png','Earth/earth_6stack_coin.png','Earth/earth_bag.png','Earth/earth_equip_button.png','Earth/earth_fortune_box.png','Earth/earth_grab_button.png','Earth/earth_loot_button.png','Earth/earth_open_now_button.png']
        for i in images:
            tImg = findImage(i)
            if tImg != None:
                pyautogui.leftClick(tImg)

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
    mars_upgrades()
    world_name = world()
    print(world_name)
    collector(world_name)

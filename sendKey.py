__author__ = 'Nick Mullen AKA CMDR Eld Ensar'

## This is mostly the work of others...
## the bulk of it being lifted from user Hodka at stackoverflow, who had the best version I saw of sending keyboard ScanCodes rather than VK codes
## his original work is here:   http://stackoverflow.com/a/23468236




import ctypes
import json
import time
import datetime
import winsound
import configparser

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

#######################################################################
#
# DirectInput keyboard scan codes
# Taken from http://www.ionicwind.com/guides/emergence/appendix_a.htm
#
#######################################################################
def SetKeyboardConsts(panel_key):
    with open('keybindings.json') as data_file:
        key_binds = json.load(data_file)
        # print(key_binds["keybindings"][panel_key])
        return int(key_binds["keybindings"][panel_key],16)

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def KeyStroke(hexKeyCode):
    PressKey(hexKeyCode)
    time.sleep(0.1)
    ReleaseKey(hexKeyCode)
    time.sleep(0.1)

def StartCountdown():
    winsound.Beep(500,200)
    print("Setting macro running in 10 seconds....")
    time.sleep(5)
    countdown=5
    while countdown>0:
        print(countdown)
        winsound.Beep(1000,200)
        time.sleep(1)
        countdown-=1
    winsound.Beep(1000,1000)
    return True

def GoToContactsBit():
    KeyStroke(UI_PANEL_SELECT)
    time.sleep(5)
    KeyStroke(UI_PANEL_LEFT)
    KeyStroke(UI_PANEL_DOWN)
    KeyStroke(UI_PANEL_DOWN)
    KeyStroke(UI_PANEL_DOWN)
    KeyStroke(UI_PANEL_DOWN)
    KeyStroke(UI_PANEL_SELECT)
    time.sleep(2)
    return True

def GoToPowerContact():
    KeyStroke(UI_PANEL_LEFT)
    KeyStroke(UI_PANEL_DOWN)
    KeyStroke(UI_PANEL_DOWN)
    KeyStroke(UI_PANEL_DOWN)
    KeyStroke(UI_PANEL_SELECT)
    time.sleep(2)
    return True

def BuyFort():
    KeyStroke(UI_PANEL_DOWN)
    KeyStroke(UI_PANEL_DOWN)
    KeyStroke(UI_PANEL_DOWN)
    time.sleep(1)
    loop=BUY_VOLUME
    while loop>0:
        KeyStroke(UI_PANEL_RIGHT)
        loop-=1
        if(loop%5==0):
            time.sleep(3)
    KeyStroke(UI_PANEL_SELECT)
    time.sleep(3)
    KeyStroke(UI_PANEL_SELECT)
    time.sleep(2)
    return True

def BackToMenu():
    KeyStroke(UI_PANEL_LEFT)
    time.sleep(1)
    KeyStroke(UI_PANEL_DOWN)
    KeyStroke(UI_PANEL_SELECT)
    time.sleep(1)
    KeyStroke(UI_PANEL_LEFT)
    KeyStroke(UI_PANEL_DOWN)
    KeyStroke(UI_PANEL_DOWN)
    KeyStroke(UI_PANEL_DOWN)
    KeyStroke(UI_PANEL_DOWN)
    KeyStroke(UI_PANEL_DOWN)
    KeyStroke(UI_PANEL_DOWN)
    KeyStroke(UI_PANEL_DOWN)
    KeyStroke(UI_PANEL_DOWN)
    KeyStroke(UI_PANEL_DOWN)
    KeyStroke(UI_PANEL_SELECT)
    return True

def ReadConfig():
    config=configparser.ConfigParser()
    config.read("sendKeys.ini")
    global UI_PANEL_LEFT
    UI_PANEL_LEFT=SetKeyboardConsts(config.get("KeyBindings", "UI_PANEL_LEFT"))
    global UI_PANEL_RIGHT
    UI_PANEL_RIGHT=SetKeyboardConsts(config.get("KeyBindings", "UI_PANEL_RIGHT"))
    global UI_PANEL_DOWN
    UI_PANEL_DOWN=SetKeyboardConsts(config.get("KeyBindings", "UI_PANEL_DOWN"))
    global UI_PANEL_SELECT
    UI_PANEL_SELECT=SetKeyboardConsts(config.get("KeyBindings", "UI_PANEL_SELECT"))

    global BUY_VOLUME
    BUY_VOLUME=int(config.get("PurchaseSettings", "BUY_VOLUME"))
    global BUY_CYCLE
    BUY_CYCLE=int(config.get("PurchaseSettings", "BUY_CYCLE"))



print("Started fortification macro at", datetime.datetime.strftime(datetime.datetime.now(), '%H:%M:%S'))

ReadConfig()


buyCycle=int(BUY_CYCLE)
while buyCycle>0:
    buyCycle-=1
    StartCountdown()
    GoToContactsBit()
    GoToPowerContact()
    BuyFort()
    BackToMenu()
    if buyCycle>0:
        print("Next fortification packages will be acquired at", datetime.datetime.strftime(datetime.datetime.now()+ datetime.timedelta(seconds=1840), '%H:%M:%S'))
        print("There are", buyCycle, "buy cycle(s) to go.")
        time.sleep(1840)
    else:
        print("You should be full and good to go. Stay frosty!")

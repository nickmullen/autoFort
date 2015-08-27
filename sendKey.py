__author__ = 'Nick Mullen AKA CMDR Eld Ensar'

## This is mostly the work of others...
## the bulk of it being lifted from user Hodka at stackoverflow, who had the best version I saw of sending keyboard ScanCodes rather than VK codes
## his original work is here:   http://stackoverflow.com/a/23468236




import ctypes
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
def SetKeyboardConsts():
    global DIK_ESCAPE
    DIK_ESCAPE=0x01
    global DIK_1
    DIK_1=0x02
    global DIK_2
    DIK_2=0x03
    global DIK_3
    DIK_3=0x04
    global DIK_4
    DIK_4=0x05
    global DIK_5
    DIK_5=0x06
    global DIK_6
    DIK_6=0x07
    global DIK_7
    DIK_7=0x08
    global DIK_8
    DIK_8=0x09
    global DIK_9
    DIK_9=0x0A
    global DIK_0
    DIK_0=0x0B
    global DIK_MINUS
    DIK_MINUS=0x0C # - on main keyboard #
    global DIK_EQUALS
    DIK_EQUALS=0x0D
    global DIK_BACK
    DIK_BACK=0x0E # backspace #
    global DIK_TAB
    DIK_TAB=0x0F
    global DIK_Q
    DIK_Q=0x10
    global DIK_W
    DIK_W=0x11
    global DIK_E
    DIK_E=0x12
    global DIK_R
    DIK_R=0x13
    global DIK_T
    DIK_T=0x14
    global DIK_Y
    DIK_Y=0x15
    global DIK_U
    DIK_U=0x16
    global DIK_I
    DIK_I=0x17
    global DIK_O
    DIK_O=0x18
    global DIK_P
    DIK_P=0x19
    global DIK_LBRACKET
    DIK_LBRACKET=0x1A
    global DIK_RBRACKET
    DIK_RBRACKET=0x1B
    global DIK_RETURN
    DIK_RETURN=0x1C # Enter on main keyboard #
    global DIK_LCONTROL
    DIK_LCONTROL=0x1D
    global DIK_A
    DIK_A=0x1E
    global DIK_S
    DIK_S=0x1F
    global DIK_D
    DIK_D=0x20
    global DIK_F
    DIK_F=0x21
    global DIK_G
    DIK_G=0x22
    global DIK_H
    DIK_H=0x23
    global DIK_J
    DIK_J=0x24
    global DIK_K
    DIK_K=0x25
    global DIK_L
    DIK_L=0x26
    global DIK_COLON
    DIK_COLON=0x27
    global DIK_APOSTROPHE
    DIK_APOSTROPHE=0x28
    global DIK_GRAVE
    DIK_GRAVE=0x29 # accent grave #
    global DIK_LSHIFT
    DIK_LSHIFT=0x2A
    global DIK_BACKSLASH
    DIK_BACKSLASH=0x2B
    global DIK_Z
    DIK_Z=0x2C
    global DIK_X
    DIK_X=0x2D
    global DIK_C
    DIK_C=0x2E
    global DIK_V
    DIK_V=0x2F
    global DIK_B
    DIK_B=0x30
    global DIK_N
    DIK_N=0x31
    global DIK_M
    DIK_M=0x32
    global DIK_COMMA
    DIK_COMMA=0x33
    global DIK_PERIOD
    DIK_PERIOD=0x34 # . on main keyboard #
    global DIK_SLASH
    DIK_SLASH=0x35 # / on main keyboard #
    global DIK_RSHIFT
    DIK_RSHIFT=0x36
    global DIK_MULTIPLY
    DIK_MULTIPLY=0x37 # * on numeric keypad #
    global DIK_LMENU
    DIK_LMENU=0x38 # left Alt #
    global DIK_SPACE
    DIK_SPACE=0x39
    global DIK_CAPITAL
    DIK_CAPITAL=0x3A
    global DIK_F1
    DIK_F1=0x3B
    global DIK_F2
    DIK_F2=0x3C
    global DIK_F3
    DIK_F3=0x3D
    global DIK_F4
    DIK_F4=0x3E
    global DIK_F5
    DIK_F5=0x3F
    global DIK_F6
    DIK_F6=0x40
    global DIK_F7
    DIK_F7=0x41
    global DIK_F8
    DIK_F8=0x42
    global DIK_F9
    DIK_F9=0x43
    global DIK_F10
    DIK_F10=0x44
    global DIK_NUMLOCK
    DIK_NUMLOCK=0x45
    global DIK_SCROLL
    DIK_SCROLL=0x46 # Scroll Lock #
    global DIK_NUMPAD7
    DIK_NUMPAD7=0x47
    global DIK_NUMPAD8
    DIK_NUMPAD8=0x48
    global DIK_NUMPAD9
    DIK_NUMPAD9=0x49
    global DIK_SUBTRACT
    DIK_SUBTRACT=0x4A # - on numeric keypad #
    global DIK_NUMPAD4
    DIK_NUMPAD4=0x4B
    global DIK_NUMPAD5
    DIK_NUMPAD5=0x4C
    global DIK_NUMPAD6
    DIK_NUMPAD6=0x4D
    global DIK_ADD
    DIK_ADD=0x4E # + on numeric keypad #
    global DIK_NUMPAD1
    DIK_NUMPAD1=0x4F
    global DIK_NUMPAD2
    DIK_NUMPAD2=0x50
    global DIK_NUMPAD3
    DIK_NUMPAD3=0x51
    global DIK_NUMPAD0
    DIK_NUMPAD0=0x52
    global DIK_DECIMAL
    DIK_DECIMAL=0x53 # . on numeric keypad #
    global DIK_OEM_102
    DIK_OEM_102=0x56 # < > | on UK/Germany keyboards #
    global DIK_F11
    DIK_F11=0x57
    global DIK_F12
    DIK_F12=0x58
    global DIK_F13
    DIK_F13=0x64 # (NEC PC98) #
    global DIK_F14
    DIK_F14=0x65 # (NEC PC98) #
    global DIK_F15
    DIK_F15=0x66 # (NEC PC98) #
    global DIK_KANA
    DIK_KANA=0x70 # (Japanese keyboard) #
    global DIK_ABNT_C1
    DIK_ABNT_C1=0x73 # / ? on Portugese (Brazilian) keyboards #
    global DIK_CONVERT
    DIK_CONVERT=0x79 # (Japanese keyboard) #
    global DIK_NOCONVERT
    DIK_NOCONVERT=0x7B # (Japanese keyboard) #
    global DIK_YEN
    DIK_YEN=0x7D # (Japanese keyboard) #
    global DIK_ABNT_C2
    DIK_ABNT_C2=0x7E # Numpad . on Portugese (Brazilian) keyboards #
    global DIK_NUMPADEQUALS
    DIK_NUMPADEQUALS=0x8D #=on numeric keypad (NEC PC98) #
    global DIK_PREVTRACK
    DIK_PREVTRACK=0x90 # Previous Track (global DIK_CIRCUMFLEX on Japanese keyboard) #
    global DIK_AT
    DIK_AT=0x91 # (NEC PC98) #
    # global DIK_COLON
    # DIK_COLON=0x92 # (NEC PC98) #
    global DIK_UNDERLINE
    DIK_UNDERLINE=0x93 # (NEC PC98) #
    global DIK_KANJI
    DIK_KANJI=0x94 # (Japanese keyboard) #
    global DIK_STOP
    DIK_STOP=0x95 # (NEC PC98) #
    global DIK_AX
    DIK_AX=0x96 # (Japan AX) #
    global DIK_UNLABELED
    DIK_UNLABELED=0x97 # (J3100) #
    global DIK_NEXTTRACK
    DIK_NEXTTRACK=0x99 # Next Track #
    global DIK_NUMPADENTER
    DIK_NUMPADENTER=0x9C # Enter on numeric keypad #
    global DIK_RCONTROL
    DIK_RCONTROL=0x9D
    global DIK_MUTE
    DIK_MUTE=0xA0 # Mute #
    global DIK_CALCULATOR
    DIK_CALCULATOR=0xA1 # Calculator #
    global DIK_PLAYPAUSE
    DIK_PLAYPAUSE=0xA2 # Play / Pause #
    global DIK_MEDIASTOP
    DIK_MEDIASTOP=0xA4 # Media Stop #
    global DIK_VOLUMEDOWN
    DIK_VOLUMEDOWN=0xAE # Volume - #
    global DIK_VOLUMEUP
    DIK_VOLUMEUP=0xB0 # Volume + #
    global DIK_WEBHOME
    DIK_WEBHOME=0xB2 # Web home #
    global DIK_NUMPADCOMMA
    DIK_NUMPADCOMMA=0xB3 # , on numeric keypad (NEC PC98) #
    global DIK_DIVIDE
    DIK_DIVIDE=0xB5 # / on numeric keypad #
    global DIK_SYSRQ
    DIK_SYSRQ=0xB7
    global DIK_RMENU
    DIK_RMENU=0xB8 # right Alt #
    global DIK_PAUSE
    DIK_PAUSE=0xC5 # Pause #
    global DIK_HOME
    DIK_HOME=0xC7 # Home on arrow keypad #
    global DIK_UP
    DIK_UP=0xC8 # UpArrow on arrow keypad #
    global DIK_PRIOR
    DIK_PRIOR=0xC9 # PgUp on arrow keypad #
    global DIK_LEFT
    DIK_LEFT=0xCB # LeftArrow on arrow keypad #
    global DIK_RIGHT
    DIK_RIGHT=0xCD # RightArrow on arrow keypad #
    global DIK_END
    DIK_END=0xCF # End on arrow keypad #
    global DIK_DOWN
    DIK_DOWN=0xD0 # DownArrow on arrow keypad #
    global DIK_NEXT
    DIK_NEXT=0xD1 # PgDn on arrow keypad #
    global DIK_INSERT
    DIK_INSERT=0xD2 # Insert on arrow keypad #
    global DIK_DELETE
    DIK_DELETE=0xD3 # Delete on arrow keypad #
    global DIK_LWIN
    DIK_LWIN=0xDB # Left Windows key #
    global DIK_RWIN
    DIK_RWIN=0xDC # Right Windows key #
    global DIK_APPS
    DIK_APPS=0xDD # AppMenu key #
    global DIK_POWER
    DIK_POWER=0xDE # System Power #
    global DIK_SLEEP
    DIK_SLEEP=0xDF # System Sleep #
    global DIK_WAKE
    DIK_WAKE=0xE3 # System Wake #
    global DIK_WEBSEARCH
    DIK_WEBSEARCH=0xE5 # Web Search #
    global DIK_WEBFAVORITES
    DIK_WEBFAVORITES=0xE6 # Web Favorites #
    global DIK_WEBREFRESH
    DIK_WEBREFRESH=0xE7 # Web Refresh #
    global DIK_WEBSTOP
    DIK_WEBSTOP=0xE8 # Web Stop #
    global DIK_WEBFORWARD
    DIK_WEBFORWARD=0xE9 # Web Forward #
    global DIK_WEBBACK
    DIK_WEBBACK=0xEA # Web Back #
    global DIK_MYCOMPUTER
    DIK_MYCOMPUTER=0xEB # My Computer #
    global DIK_MAIL
    DIK_MAIL=0xEC # Mail #
    global DIK_MEDIASELECT
    DIK_MEDIASELECT=0xED # Media Select #
    #
    # Alternate names for keys, to facilitate transition from DOS.
    #
    global DIK_BACKSPACE
    DIK_BACKSPACE=DIK_BACK # backspace #
    global DIK_NUMPADSTAR
    DIK_NUMPADSTAR=DIK_MULTIPLY # * on numeric keypad #
    global DIK_LALT
    DIK_LALT=DIK_LMENU # left Alt #
    global DIK_CAPSLOCK
    DIK_CAPSLOCK=DIK_CAPITAL # CapsLock #
    global DIK_NUMPADMINUS
    DIK_NUMPADMINUS=DIK_SUBTRACT # - on numeric keypad #
    global DIK_NUMPADPLUS
    DIK_NUMPADPLUS=DIK_ADD # + on numeric keypad #
    global DIK_NUMPADPERIOD
    DIK_NUMPADPERIOD=DIK_DECIMAL # . on numeric keypad #
    global DIK_NUMPADSLASH
    DIK_NUMPADSLASH=DIK_DIVIDE # / on numeric keypad #
    global DIK_RALT
    DIK_RALT=DIK_RMENU # right Alt #
    global DIK_UPARROW
    DIK_UPARROW=DIK_UP # UpArrow on arrow keypad #
    global DIK_PGUP
    DIK_PGUP=DIK_PRIOR # PgUp on arrow keypad #
    global DIK_LEFTARROW
    DIK_LEFTARROW=DIK_LEFT # LeftArrow on arrow keypad #
    global DIK_RIGHTARROW
    DIK_RIGHTARROW=DIK_RIGHT # RightArrow on arrow keypad #
    global DIK_DOWNARROW
    DIK_DOWNARROW=DIK_DOWN # DownArrow on arrow keypad #
    global DIK_PGDN
    DIK_PGDN=DIK_NEXT # PgDn on arrow keypad #
    #
    # Alternate names for keys originally not used on US keyboards.
    #
    global DIK_CIRCUMFLEX
    DIK_CIRCUMFLEX=DIK_PREVTRACK # Japanese keyboard #

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
    winsound.Beep(1000,100)
    print("Setting macro running in 10 seconds....")
    time.sleep(5)
    countdown=5
    while countdown>0:
        print(countdown)
        winsound.Beep(1000,100)
        time.sleep(1)
        countdown-=1
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
    loop=50
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
    UI_PANEL_LEFT=config.get("KeyBindings", "UI_PANEL_LEFT")
    global UI_PANEL_RIGHT
    UI_PANEL_RIGHT=config.get("KeyBindings", "UI_PANEL_RIGHT")
    global UI_PANEL_DOWN
    UI_PANEL_DOWN=config.get("KeyBindings", "UI_PANEL_DOWN")
    global UI_PANEL_SELECT
    UI_PANEL_SELECT=config.get("KeyBindings", "UI_PANEL_SELECT")

    global BUY_VOLUME
    BUY_VOLUME=config.get("PurchaseSettings", "BUY_VOLUME")
    global BUY_CYCLE
    BUY_CYCLE=config.get("PurchaseSettings", "BUY_CYCLE")

SetKeyboardConsts()

print("Started fortification macro at", datetime.datetime.strftime(datetime.datetime.now(), '%H:%M:%S'))

ReadConfig()

buyCycle=0
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

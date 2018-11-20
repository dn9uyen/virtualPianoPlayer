import time
import ctypes

timing = 0.2

keyList = """u [8y] t - t [8et] u [to] s
[0ya] - y - [7ra] o [wu] y [60t] - 0 - [6r] u y t
[9ey] | [tu] [tu] - [ti] - [5yo] - y y [9y] - [5qp] a
[80s] - 0 8 [80] 8 [80] 8 [8wf] - [wg] [8wf] [8wf] - [8wd] -
[9qs] | [9qp] [9qp] - q [ws] [9rf] f [9rg] f [9rf] - [9wd] -
[6TS] [yd] - [6uf] [6uf] - [60p] - [9eg] | [6wf] [6wf] - [9qd] -
[9ei] t y t [ip] y e y [9eg] | [6wf] [6wf] [td] [9qd] [qd]
[9yi] [yi] [9yi] [uo] [9uo] [ip] 9 - [5wa] [wa] [5wa] [es] [5es] [rd] [50u] [0u]
[8wyd] [ts] [8wts] - [8wts] [uf] [8oh] [sl] [90ak] - [90] - [70] o [70u] y
[6ey] t [6e] t [6tu] y [6et] y [9y] [ey] 9 [tu] [9tu] [ei] 9 [wo]
[5ro] - [5r] - [5y] - [5ru] u [8wyd] [ts] [8wts] - [8ts] [uf] [8woh] [tsl]
[0yak] - [0y] a [0wf] f [0wf] d [60d] s [60s] - [6e] u [6y] t
[9ey] - 9 [eu] [9eu] - [9ei] - [5ri] - [5ro] [ro] [5qp] [9a] 5 -
[8ws] - [8w] - [8w] w 8 s [8tf] - [8yg] [tf] [8tf] - [E8d] -
[qs] - q [tp] [qtp] - q [uf] [9uf] [uf] [9ig] [uf] [9uf] [yd] [9yd] [yd]
[6TS] [TS] [6TS] [TS] [6yd] [uf] 6 [uf] [9uf] [yd] 9 - [9e] - [9e] [yd]
[6TS] [TS] [6TS] [TS] [6yd] [uf] 6 [ig] [9i] - 9 [ig] [9ig] [uf] [9yd] [ts]
[qps] [qps] [0qps] [qps] [9qps] [qps] [8qps] [qad] [5qad] w [5w] w [5w] w [5w] w
[8tuf] | [9eig] [9eig] - [0roh] - [60s] - 6 [0u] [60u] [0u] [69y] [8t]
[9y] - [9eu] - [9e] - [9e] [9y] [5ru] u [5ro] u [5ru] - [5r] -
[8tuf] | [9eig] [9eig] - [0roh] - [6usl] - [6u] u [6u] u [6y] t
[9ey] - [9yu] - [9e] - [9e] [uf] [6wf] f [6wg] f [6wf] - [6ep] -
[9eg] | [6wf] [6wf] [9qd] | [9qi] i [9i] o [9o] p 9 -
[9eg] | [6wf] [6wf] [9qd] d d [9ei] i [9ei] o [9eo] p [9e] p
[5wa] - [5ra] [wa] [5ts] [rd] 5 [ts] [8qs] | [8qs] [8qs] | [8qs]
[8qs] - [8qs] - [8qs] - [0u] [0u] [8wyd] [ts] [8wts] - [8wts] [uf] [8oh] [sl]
[90ak] - [90] - [70] o [70u] y [6ey] t [6e] t [6tu] y [6et] y
[9y] [ey] 9 [tu] [9tu] [ei] 9 [wo] [5ro] - [5r] - [5y] - [5ru] u
[8wyd] [ts] [8wts] - [8ts] [uf] [8woh] [tsl] [0yak] - [0y] a [0wf] f [0wf] d
[60d] s [60s] - [6e] u [6y] t [9ey] 9 [eu] [9eu] - [9ei] -
[5ri] - [5ro] [ro] [5qp] [9a] 5 - [8ws] - [8w] - [8w] w 8 s
[8tf] - [8yg] [tf] [8tf] - [E8d] - [qs] - q [tp] [qtp] - q [uf]
[9uf] [uf] [9ig] [uf] [9uf] [yd] [9yd] [yd] [6TS] [TS] [6TS] [TS] [6yd] [uf] 6 [uf]
[9uf] [yd] 9 - [9e] - [9e] [yd] [6TS] [TS] [6TS] [TS] [6yd] [uf] 6 [ig]
[9i] - 9 [ig] [9ig] [uf] [9yd] [ts] [qps] [qps] [0qps] [qps] [9qps] [qps] [8qps] [qad]
d | o
i o - o i o - o i o | o
i o - o i o - [oj] [oj] [us] - [ya] [ya] | o
i o - o i o o o P - o - P - o o
i o - o i o u u [8wyd] [ts] [8wts] - [8wts] [uf] [8oh] [sl]
[90ak] - [90] - [70] o [70u] y [6ey] t [6e] t [6tu] y [6et] y
[9y] [ey] 9 [tu] [9tu] [ei] 9 [wo] [5ro] - [5r] - [5y] - [5ru] u
[8wyd] [ts] [8wts] - [8ts] [uf] [8woh] [tsl] [0yak] - [0y] a [0wf] f [0wf] d
[60d] s [60s] - [6e] u [6y] t [9ey] - 9 [eu] [9eu] - [9ei] -
[5ri] - [5ro] [ro] [5qp] [9a] 5 - [8ws] - [8w] - [8w] w 8 s
[8tf] - [8yg] [tf] [8tf] - [E8d] - [qs] - q [tp] [qtp] - q [uf]
[9uf] [uf] [9ig] [uf] [9uf] [yd] [9yd] [yd] [6TS] [TS] [6TS] [TS] [6yd] [uf] 6 [uf]
[9uf] [yd] 9 - [9e] - [9e] [yd] [6TS] [TS] [6TS] [TS] [6yd] [uf] 6 [ig]
[9i] - 9 [ig] [9ig] [uf] [9yd] [ts] [qps] [qps] [0qps] [qps] [9qps] [qps] [8qps] [qad]
d | o
i o - o i o - o i o | o
i o - o i o - [oj] [oj] [us] - [ya] [ya] | o
i o - o i o o o P - o - P - o o
i o - o i o u u [8s] - [8w] - [8w] - [8w]
"""

time.sleep(3)

# Bunch of stuff so that the script can send keystrokes

keyCodes = {
    "A" : "0x1E",
    "B" : "0x30",
    "C" : "0x2E",
    "D" : "0x20",
    "E" : "0x12",
    "F" : "0x21",
    "G" : "0x22",
    "H" : "0x23",
    "I" : "0x17",
    "J" : "0x24",
    "K" : "0x25",
    "L" : "0x26",
    "M" : "0x32",
    "N" : "0x31",
    "O" : "0x18",
    "P" : "0x19",
    "Q" : "0x10",
    "R" : "0x13",
    "S" : "0x1F",
    "T" : "0x14",
    "U" : "0x16",
    "V" : "0x2F",
    "W" : "0x11",
    "X" : "0x2D",
    "Y" : "0x15",
    "Z" : "0x2C",
    "shift" : "0x36",
    "1" : "0x02",
    "2" : "0x03",
    "3" : "0x04",
    "4" : "0x05",
    "5" : "0x06",
    "6" : "0x07",
    "7" : "0x08",
    "8" : "0x09",
    "9" : "0x0A",
    "0" : "0x0B",
    "]" : "0x3B"
}

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


# Actual functions

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

def KeyPressLetter(char):
    # If character is lowercase
    if char.islower():
        PressKey(int(keyCodes[char.upper()], 16)) # press key code
        time.sleep(.05)
        ReleaseKey(int(keyCodes[char.upper()], 16)) #release key code
        print(char)
    # If character is uppercase
    elif char.isupper():
        PressKey(0x36)
        PressKey(int(keyCodes[char.upper()], 16))
        time.sleep(0.05)
        ReleaseKey(0x36)
        ReleaseKey(int(keyCodes[char.upper()], 16))
        print(char)

def KeyPressSymbol(symbol):
    if symbol == "!":
        PressKey(int(keyCodes["shift"], 16))
        PressKey(int(keyCodes["1"], 16))
        time.sleep(.05)
        ReleaseKey(int(keyCodes["shift"], 16))
        ReleaseKey(int(keyCodes["1"], 16))
    elif symbol == "@":
        PressKey(int(keyCodes["shift"], 16))
        PressKey(int(keyCodes["2"], 16))
        time.sleep(.05)
        ReleaseKey(int(keyCodes["shift"], 16))
        ReleaseKey(int(keyCodes["2"], 16))
    elif symbol == "#":
        PressKey(int(keyCodes["shift"], 16))
        PressKey(int(keyCodes["3"], 16))
        time.sleep(.05)
        ReleaseKey(int(keyCodes["shift"], 16))
        ReleaseKey(int(keyCodes["3"], 16))
    elif symbol == "$":
        PressKey(int(keyCodes["shift"], 16))
        PressKey(int(keyCodes["4"], 16))
        time.sleep(.05)
        ReleaseKey(int(keyCodes["shift"], 16))
        ReleaseKey(int(keyCodes["4"], 16))
    elif symbol == "%":
        PressKey(int(keyCodes["shift"], 16))
        PressKey(int(keyCodes["5"], 16))
        time.sleep(.05)
        ReleaseKey(int(keyCodes["shift"], 16))
        ReleaseKey(int(keyCodes["5"], 16))
    elif symbol == "^":
        PressKey(int(keyCodes["shift"], 16))
        PressKey(int(keyCodes["6"], 16))
        time.sleep(.05)
        ReleaseKey(int(keyCodes["shift"], 16))
        ReleaseKey(int(keyCodes["6"], 16))
    elif symbol == "&":
        PressKey(int(keyCodes["shift"], 16))
        PressKey(int(keyCodes["7"], 16))
        time.sleep(.05)
        ReleaseKey(int(keyCodes["shift"], 16))
        ReleaseKey(int(keyCodes["7"], 16))
    elif symbol == "*":
        PressKey(int(keyCodes["shift"], 16))
        PressKey(int(keyCodes["8"], 16))
        time.sleep(.05)
        ReleaseKey(int(keyCodes["shift"], 16))
        ReleaseKey(int(keyCodes["8"], 16))
    elif symbol == "(":
        PressKey(int(keyCodes["shift"], 16))
        PressKey(int(keyCodes["9"], 16))
        time.sleep(.05)
        ReleaseKey(int(keyCodes["shift"], 16))
        ReleaseKey(int(keyCodes["9"], 16))
    elif symbol == ")":
        PressKey(int(keyCodes["shift"], 16))
        PressKey(int(keyCodes["0"], 16))
        time.sleep(.05)
        ReleaseKey(int(keyCodes["shift"], 16))
        ReleaseKey(int(keyCodes["0"], 16))
    print(char)



def KeyPressNumber(number):
    if number == "]":
        return(0)
    PressKey(int(keyCodes[char], 16))  # press key code
    time.sleep(.05)
    ReleaseKey(int(keyCodes[char], 16))  # release key code
    print(char)



def pressKeys(keys):
    for char in keys:
        if char.isalpha():
            KeyPressLetter(char)
        elif char.isnumeric():
            KeyPressNumber(char)
        else:
            KeyPressSymbol(char)
    print(keys)

# Plays the song
keys = []
keyNext = False


for char in keyList:

# Press keys together
    # Check if playing keys together starting or finished
    if char == "[":
        keyNext = True
        continue

    # Play key and clear key
    if char == "]":
        time.sleep(timing)
        keyNext = False
        pressKeys(keys)
        keys = []
        continue

    # If keyNext is true, add char to var key
    if keyNext:
        keys.append(char)
        continue

    # Skip spaces
    if char == " " or char == "\n" or char == "-" or char == "|":
        continue

    # If char.isalpha == True
    if char.isalpha():
        time.sleep(timing)
        KeyPressLetter(char)

    # If char.isalpha == False
    elif char.isalpha() == False:
        time.sleep(timing)
        KeyPressSymbol(char)

    elif char.isnumeric():
        time.sleep(timing)
        KeyPressNumber(char)
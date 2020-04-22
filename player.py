import time
import ctypes
import threading

# C struct redefinitions # Do NOT touch
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
	"]" : "0x39"
}
SendInput = ctypes.windll.user32.SendInput
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

class Song:
    def __init__(self, timing, unfilteredSong):
        self.unfilteredSong = unfilteredSong
        self.timing = timing
        self.song = ""

        # Remove unnecessary characters
        for char in unfilteredSong:
            if char == " " or char == "\n" or char == "-" or char == "|" or char == ":":
                continue
            else:
                self.song += char

    def pressKey(self, hexKeyCode):
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
        x = Input(ctypes.c_ulong(1), ii_)
        ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

    def ReleaseKey(self, hexKeyCode):
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
        x = Input(ctypes.c_ulong(1), ii_)
        ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

    def keyPressChar(self, char, keys):
        # If character is lowercase
        if char.islower():
            self.pressKey(int(keyCodes[char.upper()], 16))  # press key code
            time.sleep(.01)
            self.ReleaseKey(int(keyCodes[char.upper()], 16))  # release key code
        # If character is uppercase
        elif char.isupper():
            if keys:
                time.sleep(0.01)
            self.pressKey(0x36)
            self.pressKey(int(keyCodes[char.upper()], 16))
            time.sleep(0.01)
            self.ReleaseKey(0x36)
            self.ReleaseKey(int(keyCodes[char.upper()], 16))
        if char.isdigit():
            if keys:
                time.sleep(0.01)
            self.pressKey(int(keyCodes[char], 16))  # press key code
            time.sleep(.01)
            self.ReleaseKey(int(keyCodes[char], 16))  # release key code

    def keyPressSymbol(self, symbol, keys):
        if keys:
            time.sleep(0.01)
        if symbol == "!":
            self.pressKey(int(keyCodes["shift"], 16))
            self.pressKey(int(keyCodes["1"], 16))
            time.sleep(.01)
            self.ReleaseKey(int(keyCodes["shift"], 16))
            self.ReleaseKey(int(keyCodes["1"], 16))
        elif symbol == "@":
            self.pressKey(int(keyCodes["shift"], 16))
            self.pressKey(int(keyCodes["2"], 16))
            time.sleep(.01)
            self.ReleaseKey(int(keyCodes["shift"], 16))
            self.ReleaseKey(int(keyCodes["2"], 16))
        elif symbol == "#":
            self.pressKey(int(keyCodes["shift"], 16))
            self.pressKey(int(keyCodes["3"], 16))
            time.sleep(.01)
            self.ReleaseKey(int(keyCodes["shift"], 16))
            self.ReleaseKey(int(keyCodes["3"], 16))
        elif symbol == "$":
            self.pressKey(int(keyCodes["shift"], 16))
            self.pressKey(int(keyCodes["4"], 16))
            time.sleep(.01)
            self.ReleaseKey(int(keyCodes["shift"], 16))
            self.ReleaseKey(int(keyCodes["4"], 16))
        elif symbol == "%":
            self.pressKey(int(keyCodes["shift"], 16))
            self.pressKey(int(keyCodes["5"], 16))
            time.sleep(.01)
            self.ReleaseKey(int(keyCodes["shift"], 16))
            self.ReleaseKey(int(keyCodes["5"], 16))
        elif symbol == "^":
            self.pressKey(int(keyCodes["shift"], 16))
            self.pressKey(int(keyCodes["6"], 16))
            time.sleep(.01)
            self.ReleaseKey(int(keyCodes["shift"], 16))
            self.ReleaseKey(int(keyCodes["6"], 16))
        elif symbol == "&":
            self.pressKey(int(keyCodes["shift"], 16))
            self.pressKey(int(keyCodes["7"], 16))
            time.sleep(.01)
            self.ReleaseKey(int(keyCodes["shift"], 16))
            self.ReleaseKey(int(keyCodes["7"], 16))
        elif symbol == "*":
            self.pressKey(int(keyCodes["shift"], 16))
            self.pressKey(int(keyCodes["8"], 16))
            time.sleep(.01)
            self.ReleaseKey(int(keyCodes["shift"], 16))
            self.ReleaseKey(int(keyCodes["8"], 16))
        elif symbol == "(":
            self.pressKey(int(keyCodes["shift"], 16))
            self.pressKey(int(keyCodes["9"], 16))
            time.sleep(.01)
            self.ReleaseKey(int(keyCodes["shift"], 16))
            self.ReleaseKey(int(keyCodes["9"], 16))
        elif symbol == ")":
            self.pressKey(int(keyCodes["shift"], 16))
            self.pressKey(int(keyCodes["0"], 16))
            time.sleep(.01)
            self.ReleaseKey(int(keyCodes["shift"], 16))
            self.ReleaseKey(int(keyCodes["0"], 16))



    def pressKeys(self, keys):
        thread0Free = True
        thread1Free = True
        thread2Free = True
        thread3Free = True
        thread4Free = True
        for char in keys:
            if char.isalpha():
                if thread0Free:
                    thread0 = threading.Thread(target=self.keyPressChar, args=(char,True))
                    thread0Free = False
                elif thread1Free:
                    thread1 = threading.Thread(target=self.keyPressChar, args=(char,True))
                    thread1Free = False
                elif thread2Free:
                    thread2 = threading.Thread(target=self.keyPressChar, args=(char,True))
                    thread2Free = False
                elif thread3Free:
                    thread3 = threading.Thread(target=self.keyPressChar, args=(char,True))
                    thread3Free = False
                elif thread4Free:
                    thread4 = threading.Thread(target=self.keyPressChar, args=(char,True))
                    thread4Free = False
            elif char.isdigit():
                if thread0Free:
                    thread0 = threading.Thread(target=self.keyPressChar, args=(char,True))
                    thread0Free = False
                elif thread1Free:
                    thread1 = threading.Thread(target=self.keyPressChar, args=(char,True))
                    thread1Free = False
                elif thread2Free:
                    thread2 = threading.Thread(target=self.keyPressChar, args=(char,True))
                    thread2Free = False
                elif thread3Free:
                    thread3 = threading.Thread(target=self.keyPressChar, args=(char,True))
                    thread3Free = False
                elif thread4Free:
                    thread4 = threading.Thread(target=self.keyPressChar, args=(char,True))
                    thread4Free = False
            else:
                if thread0Free:
                    thread0 = threading.Thread(target=self.keyPressSymbol, args=(char,True))
                    thread0Free = False
                elif thread1Free:
                    thread1 = threading.Thread(target=self.keyPressSymbol, args=(char,True))
                    thread1Free = False
                elif thread2Free:
                    thread2 = threading.Thread(target=self.keyPressSymbol, args=(char,True))
                    thread2Free = False
                elif thread3Free:
                    thread3 = threading.Thread(target=self.keyPressChar, args=(char,True))
                    thread3Free = False
                elif thread4Free:
                    thread4 = threading.Thread(target=self.keyPressChar, args=(char,True))
                    thread4Free = False
        if not thread0Free:
            thread0.start()
        if not thread1Free:
            thread1.start()
        if not thread2Free:
            thread2.start()
        if not thread3Free:
            thread3.start()
        if not thread4Free:
            thread4.start()
        thread0.join()
        if not thread1Free:
            thread1.join()
        if not thread2Free:
            thread2.join()
        if not thread3Free:
            thread3.join()
        if not thread4Free:
            thread4.join()
        print(keys)

# Songs
dontStopMeNow = """u [8y] t - t [8et] u [to] s
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
bohemianRhapsody = """[dghPJ] [dghJ] [dghJ] [dghJ] [dghJ] [osfhJ] [sfhJ] [sfhJ] [sfhJ] [psgj] [sgj] [sgj] [shPJ] [sjl] i i
[Pdg] [dg] [Dh] [dg] [sD] [Pid] [E5y] w E y
o y E w
[q] [^W] [Ei] J B
[o@(P] Y o P
[Os] D [oP] D
[Y18o] t [toP] [Yto] [18] [Yto] [@(] [30] [4qip] t [ip] [ip] [4q] [ip] [4] [ZCakn] n [zcPJB] [Lpjxb] b [zcPJB] [ZCakn] n [zcPJB] [Lpjxb] b [zcPJB] [o@P] Y [oPD] Y
[2iP] y [iP] y
[!ETwu] [!ETwu] [!ETwu] [!ETwu] [Y1eti] e t Y
[18i] Y i p
i p s D e E
[^Ey] q E y
[oh] q [ig] q
[^Ey] q E y
[oh] q [ig] q
[^Ey] y q E y
[oh] q [ig] E
[5wt] y y E y
[pj] w [oh] y
[18Y] [(i] Y w y
[tdz] [tsl] y
[18Y] i [(Y] w y
[4qip] Y [4i] s
[^Ey] y q E y
[oh] q [yg] i
[E5p] o o E y
[pj] w [oh] w
[18tYP] [tYP] [tYP] [tYP] [7oh] [YD] [^y] Y y Y y Y y Y y Y y Y
[6t] t Y o
[%WY] o [5wY] o
[(EYwoh] [oh] ( [wEY] (
[wEY] ( [9ig] q E y [oh] [OH] [8oh] ( w t t Y o
[dz] t [sl] t
[4qi] O s g [O4qig] [O30uf] [@(YOD] [YO] [O29yd] [yO] [^Ey] [E] [E] [^EY] [^Ei] [E] [E] [^Eo] [^Eo] [E] [E] [^EO] [^EO] [E] [E] [^EO] [o@(P] Y [o@(D] Y
[29id] y [29iP] y
[Y18o] t [Y18s] t
[r] [%Y] O a
[h@(J] D h J
[Hl] Z [hJ] Z
[Gj] Z [gH] Z
[^Ey] q E y
[oh] q [ig] q
[^Ey] q E y
[oh] q [ig] q
[^Ey] y q E y
[oh] q [ig] E
[5wt] y y E y
[pj] w [oh] y
[18Y] [(i] Y w y
[tdz] [tsl] y
[18Y] i [(Y] w y
[4qip] Y [4i] s
[^Ey] y q E y
[oh] q [yg] i
[E5p] o o E y
[pj] w [oh] w
[18tYP] [tYP] [tYP] [tYP] [7oh] [YD] [^y] Y y Y y Y y Y y Y y Y
[6t] t Y o
[%WY] o [5wY] o
[(EYwoh] [oh] ( [wEY] (
[wEY] ( [9ig] q E y [oh] [OH] [8oh] ( w t t Y o
[dz] t [sl] t
[4qi] O s g [O4qig] [O30uf] [@(YOD] [YO] [O29yd] [yO] [^Ey] [E] [E] [^EY] [^Ei] [E] [E] [^Eo] [^Eo] [E] [E] [^EO] [^EO] [E] [E] [^EO] [o@(P] Y [o@(D] Y
[29id] y [29iP] y
[Y18o] t Y o
[sz] d D [sl] d D
[4qi] O s g [O4qig] [O30uf] [@(ig] [oh] [OH] [PJ] [29sl] [^J] l J H h H h [^g] h g D g D
[^d] D d s d s [^P] [@(] P s [@(d] D g h H J
[29P] P s [29d] D g h H J
[18sl] t Y o
[sz] d D [sl] d D
[4qi] O s g [O4qig] [O30uf] [@(YOD] [YO] [O29isg] [iO] [!*] [gSHL] [gSHL] [gSHL] [!*] [18] [7] S g H L H g S [^] S g H L H g S
[T6eu] [Teu] [Teu] [Teu] [Teu] [Teu] [Teu] [Teu] [eyI] [Teu] [Teu] [etY] [Teu] [eyI] [Teu] [Teu] [etY] [Teu] [Teu] [eyI] [Teu] [Teu] [eyI] [Teu] [Teu] [etY] [etY] [Teu] [eyI] [Teu] [%WTi] [%i] [%i] [%i] [t%WY] [%Y] [5tuo] [5o] [5o] [5o] [3ryO] [3ryO] [T6up] p p P p
e e E e 6 6
^ 6 [6epj] [6epj] [^EPJ] [6epj] [5woh] [4qig] [30uf] [YIakn] [yiPJB] [JB] [Tupjb] [yiPJB] [YIakn] [kn] [yiPJB] [Tupjb] [jb] [JB] [@(YOs] [o@(YP] [o@(YP] [@(YIp] [o@(YP] [@(YOs] [@(YOs] [o@(YP] [@(YIp] [@(YIp] [o@(YP] [%WYOs] [YOs] [%W] [5woYP] [oYP] [5w] [Y4qip] [@(] [Y29ip] [18] [yi^P] P P [Os] D [oP] D
[Ip] D [iO] D [YIakn] [yiPJB] [Tupjb] [yiPJB] [YIakn] [yiPJB] [Tupjb] [^Pid] [w@(EY] [^Eqy] [o@(YP] [^Ey] [^Ey] [^EY] [^Ei] [^EY] [^Ey] [^Pid] [o@(PD] [^Pid] [^Pd] [^Pd] [^PD] [^Pg] [^PD] [^Pd] [^Eqy] [w@(EY] [^Eqy] [^Ey] [^Ey] [^EY] [^Ei] [^EY] [^Ey] [^Pd] [^PD] [^Pg] [^PD] [^Pd] [^Jz] [^JZ] [^Jc] [^JZ] [^Jz] [T] [$I] P S
[7y] d y d [6u] f u f [29I] G I G [!*O] H O H
[$QP] J P J [^d] z d z [@(DZ] [o@(YP] [o@(YP] [%WYOs] [o@(YP] [29y] [18t] [^EP] [o@(YP] [o@(YP] [%YOs] [%YOs] [I29yp] [18] [^Iyp] [6] [5yoP] [5yoP] [^WEqy] [^WEqy] [WEqy] [^WEqy] [WEqy] [^] [^WEqy] [WEqy] [^WEqy] [^WEqy] [WEqy] [^] [^WEqy] [^WEqy] [WEqy] [^WEqy] [WEqy] [^] [^WEqy] [^] [WEqy] [^] [^] [^WEqy] [^] [WEqy] [^] [^] [@(YD] [wo] [@(] [WO] [@(EP] [ts] [@(yd] [YD] [@(YD] [wo] [@(] [WO] [@(EP] [ts] [EP] [@(] [@(YD] [wo] [@(] [WO] [@(EP] [ts] [@(yd] [YD] [4ig] [ep] [4] [EP] [4ts] [yd] [ts] [4] [] [OH] [9qW] [OH] [^OH] [oh] [9qW] [oh] [^oh] [ig] [9qW] [ig] [^ig] [YD] [w(E] [YD] [W9qyd] [YD] [ig] ^
W E W q [*S] [TL] [] [OH] [9qW] [OH] [^OH] [oh] [9qW] [oh] [^oh] [ig] [9qW] [ig] [^ig] [YD] [w(E] [YD] [%OH] [PJ] [(Wtsl] % [(Wt] [4] [OH] [qW] [OH] [8OH] [OH] [qW] [OH] [^oh] [W9qig] ^ [9qW] [4] [OH] [qW] [OH] [8OH] [OH] [qW] [OH] [^oh] [W9qig] ^ [9qW] [@(YD] [YD] [^(w] [YD] [^ig] [^9q] [@(YD] [YD] [^(w] [YD] [^ig] [YD] [^9q] [yd] [@(YD] [wo] [@(] [WO] [@(EP] [ts] [@(yd] [YD] [@(YD] [wo] [@(] [WO] [@(EP] [ts] [EP] [@(] [@(YD] [wo] [@(] [WO] [@(EP] [ts] [@(yd] [YD] [4qig] [ep] [4q] [EP] [4qts] [yd] [ts] [4q] [$Q] W
E W E [%t] E t
[6T] [7Y] u I O p a
S a S D f [%W] E
t T Y i I i I O
P [^EP] [ts] [yd] [ts] [yd] [YD] [ig] [YD] [ig] [oh] [OH] [g^PJ] [^] [18] [29] [18] [29] [@(] [4q] [@(] [4q] [5w] [%W] [5w] [%W] [^E] [8t] [^E] [9y] [^E] [qi] [^E] [o@(P] Y [o@(D] Y [29id] y [29iP] y [Y18o] t [Y18s] t [7ry] w [18tY] w [7ry] w [18tY] w [^Eyi] [%] [5i] [4] [@Yo] E [I29p] y [29oP] [ps] [P5d] 9 w y [5o] 9 w
P [%(Ws] P [%(WO] Y [@^(EYwo] [@^(] [18tYO] o [18Y] w [5E] E [5] [Y18to] i [18Y] y [5wE] [5] [18to] Y Y [18i] o [r%WY] r
[^Wo] t Y i i
Y Y t
y [o@(P] Y o
P [Os] d [Os] d [o@(P] Y o
P [@(YIps] d [@(YIps] d [29yiP] y i
P [i!*TP] s [iTP] s [18tuo] t u
o [TP] O O
o [18to] u t
E [i] 4 p g
i [Pd] g [ps] g [Oa] g [oP] g [4qeti] """
flightOfBumbebee = """[x0] r [ZO] z L z L l k l k J j H h G g [f3] 7 [WD] d S d S s a s a P p O o I i u Y y T y T t r u Y y T y T t r [u6] 0 [tY] y T t i u Y [ut] Y y T [te] T y Y [u6] 0 [tY] y T t i u Y [ut] Y y T [te] T y Y [u6] 0 [tY] y T [yqe] T t r [te0] T y Y [urW90] i u Y [ue80] Y y T [yqe] T t r [te0] T y Y [urW90] I o O [wpe*] O o I [ieQ9] P p O [yqpe] O o I [wri9] I o O [yqpe] O o I i P p O [yqpe] O o I [wri9] I o O [yqpe] O o I [ywoE] I i u [yqie] I o O [wpeT0] P p O [yqpe] O o I [woE9] I i u [qie9] I o O [wpe0*] P p O [qp9] e r e [rp] e r e [PE] W E W E W E W p e r e [rp] e r e [PE] W E W E W E W [pe] P p O [pWE] P p O [pe] P [pWE] O [wrp] P [tpQ] O [qpT] P a s S s a P p P a s S s a P [pQ] y u y [ud] y u y [YSD] T Y T Y T Y T d y u y [ud] y u y [YSD] T Y T Y T Y T [yd] D d S [dYT] D d S [yd] D [dYT] S [utd] D [rid] S [dIE] D f g G g f D d D f g G g f D [yodE] S s a P D d S [yodE] S s a [toYP] a s S [yodE] S s a [tsYQ] a P p [ywPE] a s S [ysqe] S d D [xuW0] Z z L z L l k l k J j H h G g f g f D [uf] g [tf] D [fe] g [qf] D [fe] g [tf] D [uf] g f D [uf] g [tf] D [fe] g [qf] D [fe] g [tf] D [uf] Y y T y T t r t r E e W w Q q 0 q 0 ( [f0] q [s0] ( [p0] q [i0] ( [p0] q [s0] ( [f0] q 0 ( [f0] q [s0] ( [p0] q [i0] ( [p0] q [s0] ( [f0] q Q w W e E r t T y Y u i I o O p P a s S d D f g f D f g f D [fe] u [sD] d S s g f D [sf] D d S [sp] S d D [fe] u [sD] d S s g f D [sf] D d S [sp] S d D [fe] u [sD] d S [pid] S s a [usp] S d D [yufaO] g f D [utpf] D d S [pid] S s a [usp] S d D [yufaO] G h H [pojT] H h G [ypig] J j H [pjid] H h G [yoga] G h H [pjid] H h G g J j H [pjid] H h G [yoga] G h H [pjid] H h G [ohdP] G g f [pigd] G h H [upojS] J j H [pjid] H h G [yqge] G h H [tje0] k l z [xrW0] c x Z [x60] Z [zt0] L l c x Z [xt] Z z L [le] L z Z [x60] Z [zt0] L l c x Z [xute] Z z L [yleQ] L z Z [xute] H j [pJ] k [li] L [zy] L [rl] k [yl] k [iJ] j [utpH] j J k l L z Z [yxuW0] c x Z x c x Z [xute] H j [pJ] k [li] L [zy] L [rl] k [yl] k [iJ] j [utpH] j J k l L z Z [yxuW0] c x Z x C v V [eb] u [sV] v C [veaT] C c x [yiec] x Z z L l k J [j6] 0 [tH] h G [wh6*] G g f [qg96] f D d S s a P [p6] P p O [WPE] O P O [p6] e [aW] e [ws] e [qd] e f g f D g D g D [f0] u [yfG] u [yhf] u [rdH] u 
[sje] u i I o O p P a s S d D [f6] 0 [tg] G h H j J k [l6] 0 [tL] z Z x C v V [b6] 0 t [pe] [ts] [uf] j [e6] """
forTheDamagedCoda = """* E w E 
* E w E 
* E w E 
* E w E 
8 W q W 
8 W q W 
8 W q W 
8 W ( W 
9 W q W 
9 W q W 
9 r W r 
9 r W r 
[wts] o [ts] o 
[*EP] i [EP] i 
[8WO] i [WO] i 
[9wo] i [wo] y 
[(Y] t W t 
( t W t 
[9y] E q E 
9 r w r 
[18] 
t [Yto] [wsl] 8 
[29PJ] y [yiOH] w 9 
[@(oh] t [toYOH] W ( 
[7oh] w [ryiog] [roYD] 7 
[18] t [Yto] [wsl] 8 
[29PJ] y [yiOH] w 9 
[@(oh] t [toYOH] W ( 
[7oh] w [ryiog] [roYD] 7 
[18] 8 [Yto] 8 t 
[18] 8 [Yto] 8 t 
[18] 8 [Yto] 8 t 
[%] % [YO]  %  
5  [5] [yo]  5  
 7 [7] o y 7 Y 
[18] t [Yto] [wsl] 8 
[29PJ] y [yiOH] w 9 
[@(oh] t [oYOH] W ( 
[7oh] w [yiog] [roYD] 7 
[18] t [Yto] [wsl] 8 
[29PJ] y [yiOH] w 9 
[@(oh] t [oYOH] W ( 
[7oh] w [yiog] [roYD] 7 
[18] 8 [Yto] 8 t 
[18] 8 [Yto] 8 t 
[18] 8 [Yto] 8 t 
[%] % [YO]  %  
5  [5] [yo]  5  
 7 [7] o y 7 Y 
[18] t [Yto] [wsl] 8 
[29PJ] y [yiOH] w 9 
[@(oh] t [oYOH] W ( 
[7oh] w [yiog] [roYD] 7 
[18] t [Yto] [wsl] 8 
[29PJ] y [yiOH] w 9 
[@(oh] t [oYOH] W ( 
[7oh] w [yiog] [roYD] 7 
[18s] [ts] [Ytod] [wD] 8 
[29g] [yg] [Oyih] [wD] 9 
[@(s] [ts] [Ytod] [WD] ( 
[7g] [wg] [ryoh] [rD] 7 
[18s] [ts] [Ytod] [wD] 8 
[29g] [yg] [Oyih] [wD] 9 
[@(s] [ts] [Ytod] [WD] ( 
[7g] [wg] [ryoh] [rD] 7 
[8s] s [Ytod] D 
[8g] g [Ytoh] D 
[8s] s [Ytod] D 
[8g] g [Ytoh] D 
s s d D 
g g h D 
s s d D 
g g h D 
s s d D 
g g h D 
s 
[etus] f 
[qets] p 
[0wts] d f 
[3wa] 
p a [etusl] j 
l j l j 
[fl] j [0wtsl] h 
l h l h 
[ol] h [3wak] h 
k h k h 
[dk] h [wryak] h 
k h k """
sonata16 = """st o u o ft o hu o ay o i so d st o u o
jt p i p ht o lu o hr o gy-h-g-o-f g ft o u o
pi a s d f g h j h g f dtq s a p ot0 p a s d f g h g f d st0 a p o
it9 o p a s d f g f d s ar9 p o i ut8 i o p a s d f d s a p08 o i u
yeq u i o p a S d p a S d f g h jq k l k j h gw f ge h j h g f
dQ s a5 7 h9 w f5 8 s0 w d5 7 h9 w f5 8 s0 w d5 hdaw o5
T y T y T y T y t y t y t y t y
zr y kr y hr y r y r y jr ky jr y hr y ht-j-hy-j-hr Gy Ge y r y t y r y t y e y
zr y kr y hr y r y r y jr ky jr y hr y ht-j-hy-j-hr Gy Ge y r y t y r y t y e y
z r y o a z k h f t u o s f h f l e t I p l j G d r y I a d G d
k w r u o k h f s e t u p s f s j Q e y I j G d a w r y o h d a
put ut ut ut aut s ut Dut f ut Hut j ut ut kut j H j lut jut lut jut
ky a ho a zy a o a y a o a ly ka jo ha
jy-k-s-j-kI-j-s-k-jy-k-s-j-kI-j-s-k-jy-k-s-j-kI-j-s-k-jy-k-s-j hI js
hao h d h k z k h k lspy j G j hao o y o a d a o a ste9 p I p orw kdw5 ha5w
ow5 h d h J z J h J lspy j G j hPo o y o P d P o P ste9 p I p o
5 6 ^ 8 9 0 Q w h J j h g f d S 6 7 * 9 0 Q W e L x z L J j h g92
d p d g j g d g huoe f S f diy y e y i p i y i o0w6 u T u q9
y u i o p a S d y i u y t r e W a s d f G H j k W r e W q 0 9 8
j x z l k j h g y p o i u y t r h z l k j h g f t o i u y t r e
g l k j h g f d r i u y t r e W f k j H g f d s e t r e w q 0 9
P d s P p o i uEw8 i o p P s d f gi s p s ji s lp s fo s P gs h gi s p s
zi d P d li s cp s lu s Jo-l-J-s-j-J-ji s p s
dP f g h j J l z l J j hiE g f d sie d f g h j J l J j h gie f d s
Piw s d f g h j J j h g fuw d s P piq P s d f g h j h g f d s P p
jq w e E t y u i u y t jsE e w q hs0 q w e r t y u y t r hse w q 0
gs9 0 q w e r t y t r e gaw q 0 9 fs8 9 0 q w e r t r e w fsq 0 9 8
deq y u i o p a S d p a S d f g h jq k l k j h gw f ge h j h g f dQ s
a5 7 h9 w f5 8 s0 w d5 7 h9 w f5 8 s0 w d5 hdaw o5
I o I o I o I o i o i o i o i o
hu o fu o su o u o u o du fo du o su o si-d-so-d-su ao ay o u o i o u o i o y o
hu o fu o su o u o u o du fo du o su o si-d-so-d-su ao ay o u o i o u o i o y o
h 0 w t u h f s p q e t i p s p g 9 q r y g d a o 0 w r u
h k h x t u p s x l j g y i p d g j g z r y o a z k h f t u o s
l h f d pi pi pi Spi d pi Spi d pi j YtQ YtQ YtQ HYtQ j YtQ HYtQ j YtQ
hw u jt ku lw zu xt zu lw ku jt hu gw fu dt su dw
f-i-d-fr-d-i-f-dw-f-i-d-fr-d-i-f-dw-f-i-d-fr-d-i-f-dw-f-i-d sr di sut
s o s f h f s f giyw d a d sut t w t u o u t u i9q5 y r y t08 lhf8t s18 """
sadThemeOPM = """[ej] [rk] [TL] [yz] [yz7] Q r [*TL] z 5 9 w [aj] z x C v [yz] p d p b [efjx] u Sj C v x C [rkz] I S d [dz] x C [5d] 9 [wz] r L [whz] [9dj] e y e e [y9] [$QSG] J G k G GJL I p f [7ad] Q r y r [QS] d5 9 w r w [9f] G e y I h [QG] 0f[*T] [ud] S [0f] [7ad] Q T y I [rf] y [59od] 9 w r w 9 [QG] e y [ed] I e [yv] e [6pf] 0 e Td S [0d] r Su [od] d S d Q eS I d d f G QfT [QG] [QG] [f0] [QG] [*S] h G [6f] [0d]S[ra]S udo [rf]u[oh] [QG] y I p d y I [wj] y I oG hhhh | [rp] I [ad] p f I [ad] I w [rp] [yd] [po] f [yp] [od] y [9p] [ep] [yd] I f [ye] S e S S a S [ud] [pf] d [rp] I [ad] p f [QI] [ad] [QI] w
[rp] [yd] [po] f [yp] [od] y [9p] [ep] [yd] I f [yp] [ed] [*S] [*T] S a S [5ad] 7 9 w [*TS] [9yd] T 0 e T f [IG] Q r [yd] Q [rh] y [QG] 0fT d S f [5ad] 7 9 w [ep] [uf] [6d] * 0 ed S [QG] e y [ed] e [yh] [$QSG] [QI] [rp] [uf] [7ad] Q r y Q [TS] [yd] [5ry] 9 w r 9 [wf] r G Q e [yd] Q [eh] y G 0 fe [pd] S f [7d] Q r y [QI] [rf] y [5d] 9 w y w [rf] y G 6 9 Q 6 [9h] Q [6f] 0 e * [0d] 6 [*S] 0 [3od] 7 S0 [wod] [3od] 7 S0 [wod] [pd] *SQ [pd] [pd] * [pf] e
G Qfr G G Qfr G S 0 [eh] 0 G e [0f] * [3d]S[7a]S [0d]w r [7f] 0 [wh] [$G] 9 Q e d 9 [Qe] [59wj] y I o y I o I p f [7ad] Q r y r [QS] d 5 9 w r w [9f] G e y I
G 0 f,T [ud] S [0f] [7ad] Q T y Q [rf]y [5od] 9 w r w [9f] G e y [ed] I e [yh] e
[6pf] 0 e Td S [0od] rSu [od] [od] S [od] [pd] eSy [pd] [pd] f G QfT G G
f G S h G [6f] [0d]S[ra]S udo [rf]u [oh] [QG] y I pd y I [wj] y I oG y I o
[eh] y I o y I o"""
pumpedUpKicks = """[Wqti] - [Wqti] [Wqt] i o-[tWYO] - [tWYO] [tWY] P s [oYPD] - [oYPD] [oYP] D s-[yiEP] - [yiEP] [Eyi] P o O : [Wqti] - [Wqti] [Wqt] i o-[tWYO] - [tWYO] [tWY] P s [oYPD] - [oYPD] [oYP] D s-[yiEP] - [yiEP] [Eyi] P o O : [Wqti] - [Wqti] [Wqt] i o-[tWYO] - [tWYO] [tWY] P s [oYPD] - [oYPD] [oYP] D s-[yiEP] - [yiEP] [Eyi] P o O : [Wqti] - [Wqti] [Wqt] i o-[tWYO] - [tWYO] [tWY] P s [oYPD] - [oYPD] [oYP] D s-[yiEP] - [yiEP] [Eyi] P o O : t E E E E-t -- t t E E E E w E t-E E-E-t - E E-E Y t -- E E E E E-w E t E E-E E-t -- E E-E E t -- W W : E E E - w w E t E-E E-t - E E E E-Y t -- W W : E E E E - w E t E E E -- [Wqtio] i i [WYqti] [WYqt] i [to] E [tWYO]-Y [tWYO]-[tWY] [EP] [ts] E : [oYPD]-Y [oYPD] [oYP] D s o [yiEP] i-[yioEP] i [Eyi] P o [oO] : [Wqti] i i [WYqti] [WYqt] i [to] E [tWYO]-Y [tWYO] [tWY] [EP] [ts] E : [oYPD]-Y [oYPD] [oYP] D s i [yiEP] i i [yioEP] [Eyi] [YP] o O : [Wqtio] i i [WYqti] [WYqt] i [to] E [tWYO]-Y [tWYO]-[tWY] [EP] [ts] E : [oYPD]-Y [oYPD] [oYP] D s o [yiEP] i-[yioEP] i [Eyi] P o [oO] : [Wqti] i i [WYqti] [WYqt] i [to] E [tWYO]-Y [tWYO] [tWY] [EP] [ts] E : [oYPD]-Y [oYPD] [oYP] D s i [yiEP] i i [yioEP] [Eyi] [YP] o O : t E E E E-t -- t t E E E E w E t-E E-E-t - E E-E Y t -- E E E E E-w E t E E-E E-t -- E E-E E t -- W W : E E E - w w E t E-E E-t - E E E E-Y t -- W W : E E E E - w E t E E E -- [qtoWP] i i [qtWYP] [WYqt] P [to] [EO] [WYti]-Y [WYti] [tWY] [Ei] [to] E : [YOPo]-Y [YOPo] [YPo] P s o [yiED] i-[yioED] [Eyi] D s o : [qtiWP] i i [qtWYP] [WYqt] P [to] [EO] [tWYP]-Y [tWYP] [tWY] [EP] [to] [EO] : [ioYP]-Y [ioYP] Y [oYP] i o i [yiEO] i i o [yiEO] i [Eyi] Y P s [qtoWD] i i [qtWYD] [WYqt] D [ts] E [tWYP]-Y [tWYP] [tWY] [EP] [to] [EO] : [oYP]-Y [oYP] [oYP] P o [oO] [Eyi] i-[Eyio] [Eyi] i o o : [qtiWO] i i [qtWYO] [WYqt] P [ts] E [tWYD]-Y [tWYD] [tWY] [ED] [ts] E : [oYP]-Y [oYP] [oYP] P o [iO] [Eyi] i i [Eyio] [Eyi] Y - [qYD]-[YD]-[YD]-[wYD]-[8(W] [YD] [EYD] t[YD][oh] : [wEYD]-[YD]-[YD]-t w [9qE] -- ( q : [8q%YD]-[YD]-[YD]-[wYD]-[8(W] - [YD] [EYD] t[YD][oh] : [wEY] - [oh]-[tig] w [9qE]-[ig] [ig]-[ig] ( q : [qh] g g D [Ds] w P [8(WD]-D-D [PE] [st] [oP] : [wEYD]-D D D-t [wh] [E9qg] g-h g-( [qh] : [%8qg] g g D D-[sw] P [8(WD]-D-D [PE] [st] [oP] : [wEYD]-D D D-t [wg] [9qE] g g h g D ( q : w q q ( (-8 ^ (-(-( ^ 8 ^ : (-( ( ( - w q q-w q - w : q q q ( (-8 ^ (-(-( ^ 8 ^ : (-( ( ( - q-q q w q ( - [Wqtih] g g [WDqti] [WDqt] i [so] P [tWYOD]-D [tWYO] [tWYD] P s P : [oYPD]-D [oYPD] [oYPD] D s h [EPyig] g-[yihEP] [Eyig] P o [Oh] : [Wqtig] g g [WDqti] [WDqt] i [so] P [tWYOD]-D [tWYO] [tWYD] P s P : [oYPD]-D [oYPD] [oYPD] D s g [yiEP] g g [yihEP] [Eyig] [DP] o O : [Wqtih] g g D [Wqti] D [Wqt] i [so] P 
[tWYOD] D [tWYO] [tWYD] P s P : [oYPD]-D [oYPD] D [oYP] D s h [EPyig] g h [yiEP] [Eyig] P o [Oh] : [Wqtig] g g [WDqti] [WDqt] i [so] P [tWYOD]-D [tWYO] [tWYD] P s P : [oYPD]-D [oYPD] [oYPD] D s g [yiEP] g g [yihEP] [Eyig] [DP] o O"""
hisTheme = """[qo] d s o a – a – s w o s o a – a – s
[eo] d s o a – a – s t o s f d – s – d
[qto] d s o a – a – s [wy] o s o a – a – s
[euo] d s o a – a – s [wt] o s f d – s – d
[4o] d [8s] o [wa] – a-8 s 5 o [8s] o [ra] – a-w s
[6o] d [0s] o [ra] – a-0 s 8 o [ws] f [yd] – s-t d
[qo] [td] [qs] [to] [qa] t-a-q [ts] w [yo] [ws] [yo] [wa] y-a-w [ys] [eo] [ud] [es] [uo] [ea] u-a-e [us] r [uo] [os] [rf] [ud] o-s-y [rd] [4qo] d s o [qia] – a – s [5w] o s o [woa] – a – s
[6eo] d s o [epa] – a – s [8ts] o s o t |
[4o]-8-[qd]-8-[4s]-8-[qo]-4-[8a]-q-8-[4a]-8-q-[8s]-4-
5-9-[wo]-9-[5s]-9-[wo]-9-[5a]-9-w-[9a]-5-q-[9s]-5-
[6o]-0-[ed]-0-[6s]-e-[0o]-6-[0a]-e-6-[0a]-e-0-[6s]-e-
8-w-[to]-w-[8s]-w-[8f]-w-[td]-w-8-[ws]-8-t-[8d]-w-
[5o]-5-5-5-[6p]-6-6-6-[7a]-7-7-7-[9d]-9-9-9-
[5p] f [9d] p [epS] – [pS]-9 [pd] 6 p [9d] p [pTS] – [pS]-e [pd] [7p] f [Qd] p [pTS] – [pS]-Q [pd] 9 p [ed] G [upf] – [pd]-y [pf] [5p] f [9d] p [epS] – [pS]-9 [pd] 6 p [9d] p [pTS] – [pS]-e [pd] [7p] f [Qd] p [pTS] – [pS]-Q [pd] 9 p [ed] G [upf] – [pd]-y [pf] 5 – 9 – w – [7r] –
[oj] x z j L – L – z p j z j L – L – z
[aj] x z j L – L – z d j z C x – z – x
[oj] x z j L – L – z p j z j L – L – z
[aj] x z j L – L – z d j z C x – z – x
[qh] z l h k – k – l w h l h k – k – l
[eh] z l h k – k – l t h l x z – l – z
[qh] z l h k – k – l w h l h k – k – l
[eh] z l h k – k – l t h l x z l z
[4h] z [8l] h [wk] – k8 l 5 h [8l] h [rk] – k8 l
[6h] z [0l] h [rk] – ke l 8 h [wl] x [yz] – lt z
[qo] d [ts] o [oa] – at s w o [ts] o a – at s
[eo] d [us] o a – ap s t o [os] f d – ss d
[4o] d [8s] o [wa] – a8 s 5 o [8s] o [ra] – a8 s
[6o] d [0s] o [ra] – ae s 8 o [ws] f [yd] – st d
[4o] d [8s] o [wa] – a8 s 5 o [8s] o [ra] – a 8 s
[6o] d [0s] o [ra] – ae s 8 o [ws] f [yd] – st d
[4qo] d [8s] o [woa] – [oa]8 s [5w] o [8s] o [roa] – [oa]8 s
[6eo] d [0s] o [roa] – [oa]e s [8t] o [ws] f [yod] – [os]t [od] [4qo] d [8s] o [woa] – [oa]8 s [5w] o [8s] o [roa] – [oa]8 s
[6eo] d [0s] o [roa] – [oa]e s [8t] o [ws] f [yod] – [os]t [od] [4qo] d [8s] o [woa] – [oa]8 s [5ws] o [8s] o [roa] – [oa]8 s
[6eo] d [0s] o [roa] – [oa]e s [8ts] o [ws] f [yod] – [os]t [od] [4qo] d [8s] o [woa] – [oa]8 s [5ws] o [8s] o [roa] – [oa]8 s
[6eo] d [0s] o [roa] – [oa]e s [8ts] o [ws] f [yod] – [os]t [od]"""
megalovania = """y y d p O o i y i o 
t t d p O o i y i o 
r r d p O o i y i o 
E E d p O o i y i o 
[9y] y [9d] [9p] 9 [9O] [9o] [9i] 9 [9y] [9i] o 
[8t] t [8d] [8p] 8 [8O] [8o] [8i] 8 [8y] [8i] o 
[7r] r [7d] [7p] 7 [7O] [7o] [7i] 7 [7y] [7i] o 
[^E] E [^d] [^p] ^ [8O] [8o] [8i] 8 [8y] [8i] o 
[2yd] [yd] [9dz] [2pj] 2 9 [2OH] [2oh] 9 [2ig] 2 [2yd] [9ig] [oh] 
[1ts] [ts] [8dz] [1pj] 1 8 [1OH] [1oh] 8 [1ig] 1 [1yd] [8ig] [oh] 
[ra] [ra] [7dz] [pj]  7 [OH] [oh] 7 [ig]  [yd] [7ig] [oh] 
[EP] [EP] [^dz] [pj]  ^ [1OH] [1oh] 8 [1ig] 1 [1yd] [8ig] [oh] 
[2yd] [yd] [9dz] [2pj] 2 9 [2OH] [2oh] 9 [2ig] 2 [2yd] [9ig] [oh] 
[1ts] [ts] [8dz] [1pj] 1 8 [1OH] [1oh] 8 [1ig] 1 [1yd] [8ig] [oh] 
[ra] [ra] [7dz] [pj]  7 [OH] [oh] 7 [ig]  [yd] [7ig] [oh] 
[EP] [EP] [^dz] [pj]  ^ [1OH] [1oh] 8 [1ig] 1 [1yd] [8ig] [oh] 
[2g] [9g] g 2 [2g] 9 [2g] [2d] 9 [2d] 2 2 9 
[1g] [8g] g 1 [1h] 8 [1H] [1h] H h [8g] [1d] [1g] [1h] 8 
[g] [7g] g  [h] 7 [H] [j] 7 [l]  [j] 7 
[z] [^z] [z] [j] [^z] [1l] 1 8 1 [1v] 1 8 
[2gj] 2 [9gj] [gj] [26] [2gj] 9 [%2gj] [25dh] 9 [24dh] 2 2 [49] 5 
[1gj] 1 [9gj] [gj] [16] [1gj] 9 [%1dh] [15gj] 9 [14fz] 1 [2dj] [49sh] 5 
[kz] [h] [9dj] f [6gh] [d] [9ag] [%d] l [5d] [9ah] [4d] [ag] [2o] [49af] [5o] 
[P]  [9s] [Pd] [6] [dg] 9 [%1fl] [15] 9 [14] 1 2 [49] 5 
 ^   ^  [dg] [Pd] [^dg] [fh] [gH] [fh] [^dg] [Pd] 
[1H] h g d [8dg] [1fh] 1 8 1 1 8 1 1 [1H] 8 j 
[2l] [9j] H [2h] [2g] [9d] [2f] g 2 [9h] 2 [2j] 2 [9l] 
[!L] [*H] [!H] [!h] [*g] [@h] @ ( @ @ @ ( 
[yi] [^uo] [ip]  [^dg]  [sf]  ^  [pd]  ^ 
[1of] 8 [1pg] 1 8 1 [sh] 1 8 1 [1pf] 1 8 
[2dj] 9 2 2 9 2 j [2H] [9h] [2G] [2g] [2f] [9D] d 
[!OS] * ! ! * @ [PD] @ ( @ @ @ ( 
 ^   ^  [dg] [Pd] [^dg] [fh] [gH] [fh] [^dg] [Pd] 
[1H] h g d [8dg] [1fh] 1 8 1 1 8 1 1 [1H] 8 j 
[2l] [9j] H [2h] [2g] [9d] [2f] g 2 [9h] 2 [2j] 2 [9l] 
[!L] [*H] [!H] [!h] [*g] [@h] @ ( @ @ @ ( 
[yi] [^uo] [ip]  [^dg]  [sf]  ^  [pd]  ^ 
[1of] 8 [1pg] 1 8 1 [sh] 1 8 1 [1pf] 1 8 
[2dj] 9 2 2 9 2 j [2H] [9h] [2G] [2g] [2f] [9D] d 
[!OS] * ! ! * @ [PD] @ ( @ @ @ ( 
[E]       [i]   
[1u] 1 1 1 1 y 1 1 1 1 1 
[i]          
          
[E]       [i]   
[1u] 1 1 1 1 y 1 1 1 1 1 
[2y] 2 2 2 2 y T 2 t r E 2 e [2W] w 2 Q [2q] 0 ( 
[29] 2 2 2 2 2 2 2 2 2 
[9E] 9 [y] [e]  [W] [w] [q] [i] [9] [q] w 
[18u] 8 [1y] [1e] 1 [1W] y [1w] [1q] 1 [19] [1q] w 
[7i] 7 [y] [e]  [W] [w] [q]  [9] [q] w 
[7] w [yi] y [eo]  i [Wt] y [wt] [qe]  [9w] [qe] [wt] 
[9E] 9 [y] [e]  [W] [w] [q] [i] [9] [q] w 
[18u] 8 [1y] [1e] 1 [1W] y [1w] [1q] 1 [19] [1q] w 
[29y] 9 [2yi] [2eu] 2 [W2t] [2wu] [2qy] 2 [29w] [2qe] [wt] 
[29] 9 [2yi] [2eu] 2 [W2t] [2wu] [2qy] 2 [29w] [2qe] [wt] 
[qE] [q^E] [^] [qE] ^ [qE] [qE] ^ [^] [^] [^] [q^E] 
[1wt] [8wt] [18] [1wt] 8 [1wt] [1wt] 8 [18] [18] [18] [8wt] 
[2ey] [9ey] [29] [2ey] 9 [!WT] [!WT] * [!*] [!*] [!*] [*WT] 
[1wt] [8wt] [18] [1wt] 8 [Qr] [Qr] 7 [7] [7] [7] [Q7r] 
[qE] [q^E] [^] [qE] ^ [qE] [qE] ^ [^] [^] [^] [q^E] 
[1wt] [8wt] [18] [1wt] 8 [1wt] [1wt] 8 [18] [18] [18] [8wt] 
[2ey] [9ey] [29] [2ey] 9 [2ey] [2ey] 9 [29] [29] [29] [9ey] 
[2ey] [9ey] [29] [2ey] 9 [2ey] [2ey] 9 [29] [29] [29] [9ey] 
[qE] [q^E] [^] [qE] ^ [qE] [qE] ^ [^] [^] [^] [q^E] 
[1wt] [8wt] [18] [1wt] 8 [1wt] [1wt] 8 [18] [18] [18] [8wt] 
[2ey] [9ey] [29] [2ey] 9 [!WT] [!WT] * [!*] [!*] [!*] [*WT] 
[1wt] [8wt] [18] [1wt] 8 [Qr] [Qr] 7 [7] [7] [7] [Q7r] 
[qE] [q^E] [^] [qE] ^ [qE] [qE] ^ [^] [^] [^] [q^E] 
[1wt] [8wt] [18] [1wt] 8 [1wt] [1wt] 8 [18] [18] [18] [8wt] 
[29y] 9 [9y] [2e] [2y] 9 [W2y] [2wy] 9 [2q] 2 [29] [9qy] w 
[29y] 9 [9y] [2e] [2y] 9 [W2y] [2wy] 9 [2q] 2 [29] [9qy] w 
E E d p O o i y i o 
t t d p O o i y i o 
y y d p O o i y i o 
y y d p O o i y i o 
E E d p O o i y i o 
t t d p O o i y i o 
y y d p O o i y i o 
t t d p O o i y i o 
r r d p O o i y i o 
E E d p O o i y i o """
asgore = """[6s] [6s] [8f] [8f] 
[9d] 
[7a] [7a] [9d] [9d] 
[8s] 
[6p] [6p] [8s] [8s] 
[9a] 8 7 6 
[5o] [4o] [5p] [6p] 
[3u] 
[6s] [6s] [8f] [8f] 
[9d] 
[wh] [wh] [9d] [9d] 
[0f] w 
[0f] [9d] [8f] [0h] 
[0j] [9l] l 
[0k] [9j] [7h] 0 
[6j] 
[2s] 
s [3f] f 
[6d] 6 7 6 [6s] [8f] [6p] 9 
[6p] 6 [7a] 6 6 8 [6s] 9 
[6f] 6 7 6 6 8 6 9 
[6s] 6 8 6 [7f] 7 9 7 
[8d] 8 9 8 [8s] [0f] [8p] w 
[8a] 8 [9h] 8 8 0 [8d] w 
[8f] 8 9 8 8 0 8 w 
[8f] 8 f [7g] 7 g 
[6h] 6 7 6 8 6 [7j] 0 
[6s] 6 7 6 [8p] 6 [7d] 0 
[6h] 6 7 6 8 6 [7j] 0 
[6s] 6 7 6 [8l] 6 [7j] 0 
[6f] 6 7 7 8 8 6 6 
0 0 6 6 9 9 6 6 
[8g] f d 
[2s] s [3f] f 
[6d] 6 7 6 [6s] [8f] [6p] 9 
[6p] 6 [7a] 6 6 8 [6s] 9 
[6f] 6 7 6 6 8 6 9 
[6s] 6 8 6 [7f] 7 9 7 
[8d] 8 9 8 [8s] [0f] [8p] w 
[8a] 8 [9h] 8 8 0 [8d] w 
[8f] 8 9 8 8 0 8 w 
[8f] 8 f [7g] 7 g 
[6h] 6 7 6 8 6 [7j] 0 
[6s] 6 7 6 [8p] 6 [7d] 0 
[6h] 6 7 6 8 6 [7j] 0 
[6s] 6 7 6 [8l] 6 [7j] 0 
[6f] 6 7 7 8 8 6 6 
0 0 6 6 9 9 6 6 
[8g] f d 
[6s] [5a] 
[6p] s p [5f] [6p] 5 
[6p] a [5s] [6h] f 7 5 
[6p] d p [5f] [6p] [5o] 
[6p] a [5s] [6h] f 7 5 
[7p] d p [8f] [7p] [8o] 
[7p] a [8s] [9h] f 0 7 
[6o] [5f] 6 5 [6d] 
[7s] [7a] [7o] [5a] 
[6p] s p [5f] [6p] 5 
[6p] a [5s] [6h] f 7 5 
[6p] d p [5f] [6p] [5o] 
[6p] a [5s] [6h] f 7 5 
[7p] d p [8f] [7p] [8o] 
[7p] a [8s] [9h] f 0 7 
[6o] [5f] 6 5 [6d] 
s a p o 
[6p] [6s] [5p] [5f] [6p] 6 5 5 
[6p] [6a] [5s] [5h] [6f] 7 
[6p] [6d] [5p] [5f] [6p] 6 5 [5o] 
[6p] [6a] [5s] [5h] [6f] 7 
[8p] [8d] [7p] [7f] [8p] 8 7 [7o] 
[8p] [8a] [7s] [7h] [8f] 0 6 
o 6 p 6 f d 
[7s] 7 a 7 p o 5 
[6f] [8a] [6p] [0f] [6p] [5o] 
[6p] [7a] [8s] [wh] [0f] 
[6f] [9a] [6p] [0f] [6p] [5o] 
[6p] [7a] [8s] [wh] [0f] 
[6f] [9a] [6p] [0f] [6p] [5o] 
[6p] [7a] [8s] [wh] [0f] 
[5o] [6p] [0f] [9d] 
[8s] [7a] [6p] [5o] 
[6z] 8 6 0 6 5 
6 7 8 w 0 
6 9 6 0 6 5 
[6x] 7 8 w 0 
[6l] 9 6 0 6 5 
6 7 8 w 0 
5 6 0 9 
8 7 6 5 
[6p] [6s] [5p] [5f] [6p] 6 5 [5o] 
[6p] [6a] [5s] [5h] [6f] 7 
[6p] [6d] [5p] [5f] [6p] 6 5 [5o] 
[6p] [6a] [5s] [5h] [6f] 7 
[8p] [8d] [7p] [7f] [8p] 8 7 [7o] 
[8p] [8a] [7s] [7h] [8f] 0 6 
o 6 p 6 f d 
[7s] 7 a 7 p o 5 
[6d] 6 6 6 6 6 
6 6 6 [6p] [8s] 
[7d] 7 7 7 7 f 7 
[7h] 7 g 7 [7f] [9g] 
[8d] 8 8 8 8 8 
[9p] [6p] [9d] d [8g] 
[6f] 6 6 
[3d] [6f] [8g] 
[48j] 
d f [4g] [8j] 
[60] h g h f 
s [5d] 9 
[6q] f 
g j 0 h 
[8g] h f l 
[48j] 
d f [4g] [8j] 
[60] h g h f 
s [5d] 9 
[6q] 
p d [0s] 
[9c] 
x 
z l z j 
[7k] h d f 
[^g] l 8 j l 
[9j] 
[9c] x z l z j 
[7k] h d f 
[^g] f 8 p f 
[9d] 
[9c] x z l z j 
[7k] h d f 
[^g] l 8 j l 
[9j] 
[9c] x z l z j 
[7k] h d f 
[^g] f 8 p f 
[9d] 
[2c] [x] [2z] [4l] z [3k] [1j] [3l] 
[2j] [d] [1l] z 
[2c] [x] [2z] [4l] d [3c] [1x] [3z] 
[2z] 4 [3x] 5 [6c] [6b] [7n] 
[8m] [7n] [6b] [5v] [7b] [6v] [5b] [7n] 
[6b] [2z] [2z] [3x] 
[4c] [5v] [^B] 
[6b] [4c] [2z] [j] 
[2c] [x] [2z] [4l] z [3k] [1j] [3l] 
[2j] [d] [1l] z 
[2c] [x] [2z] [4l] d [3c] [1x] [3z] 
[2z] 4 [3x] 5 [6c] [6b] [7n] 
[8m] [7n] [6b] [5v] [7b] [6v] [5b] [7n] 
[6b] [2z] [2l] [3z] 
[2c] 3 4 [6x] 4 [3l] 2 
[2z] 3 4 6 4 [3l] [2z] 
[3c] 4 5 [7x] 5 [4l] 3 
[3z] 4 5 7 5 [4l] [3z] 
[2c] 3 4 [6x] 4 [3l] 2 
[2z] 3 4 6 4 [3l] [2z] 
[3c] 4 5 [7x] 5 [4l] 3 
[3z] 4 5 7 l 5 [4z] 3 
9 6 8 
7 5 6 
9 6 8 
7 5 6 
9 """

songNum = input("""What song #? \n
 1. Dont stop me now
 2. Bohemian Rhapsody
 3. Flight of the bumblebee
 4. For the damaged coda
 5. Sonata 16
 6. OPM sad theme
 7. Pumped up Kicks
 8. Megalovania
 9. Asgore Theme
 """)

if int(songNum) == 1:
    song0 = Song(0.3, dontStopMeNow)
elif int(songNum) == 2:
    song0 = Song(0.7, bohemianRhapsody)
elif int(songNum) == 3:
    song0 = Song(0.08, flightOfBumbebee)
elif int(songNum) == 4:
    song0 = Song(0.4, forTheDamagedCoda)
elif int(songNum) == 5:
    song0 = Song(0.3, sonata16)
elif int(songNum) == 6:
    song0 = Song(0.6, sadThemeOPM)
elif int(songNum) == 7:
    song0 = Song(0.27, pumpedUpKicks)
elif int(songNum) == 8:
    song0 = Song(.17, megalovania)
elif int(songNum) == 9:
    song0 = Song(.25, asgore)

for x in range(3):
    print("Starting in %d" % (3-x))
    time.sleep(1)

keys = []
keyNext = False

for char in song0.song:

    # Press keys together
    # Check if playing keys together starting or finished
    if char == "[":
        keyNext = True
        continue

    # Play key and clear key
    if char == "]":
        time.sleep(song0.timing)
        keyNext = False
        song0.pressKeys(keys)
        keys = []
        continue

    # If keyNext is true, add char to var key
    if keyNext:
        keys.append(char)
        continue

    # If char.isalpha == True
    if char.isalpha() or char.isdigit():
        time.sleep(song0.timing)
        song0.keyPressChar(char, False)
        print(char)

    # If char.isalpha == False
    elif not char.isalpha():
        time.sleep(song0.timing)
        song0.keyPressSymbol(char, False)
        print(char)

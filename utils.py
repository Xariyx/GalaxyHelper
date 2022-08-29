import pyautogui
import win32api
import win32con
from pyautogui import *

__confidence__ = 0.8
__region__ = (0, 0, 1920, 1080)
__grayscale__ = True
__loopSleep__ = 0.5
__timeToLive__ = 30
__clickCount__ = 1
__clickSleep__ = 1
__animationSleep__ = 0.5
__callbackSleep__ = 0.1
__moveSleep__ = 0.5
__offsetX__ = 0
__offsetY__ = 0


def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def move(coords):
    win32api.SetCursorPos(coords)


def macroComponent(imagePath, **kwargs) -> bool:
    r"""
    :param imagePath:
        Path to image that you want to reference to
    :type imagePath: ``string``
    Keyword arguments
            * *confidence* -> ``float``
            * *region* -> ``tuple``
            * *grayscale* -> ``float``
            * *loopSleep* -> ``float``
            * *animationSleep* -> ``float``
            * *clickSleep* -> ``float``
            * *callbackSleep* -> ``float``
            * *moveSleep* -> ``float``
            * *timeToLive* -> ``int``
            * *clickCount* -> ``int``
            * *callback* -> ``function``
            * *offsetX* -> ``int``
            * *offsetY* -> ``int``
    :return:
        True if everything went ok, False if TTL was exceeded
    """

    confidence = __confidence__
    region = __region__
    grayscale = __grayscale__
    loopSleep = __loopSleep__
    timeToLive = __timeToLive__
    clickCount = __clickCount__
    animationSleep = __animationSleep__
    clickSleep = __clickSleep__
    callbackSleep = __callbackSleep__
    moveSleep = __moveSleep__
    callback = None

    if "confidence" in kwargs:
        confidence = kwargs["confidence"]

    if "region" in kwargs:
        region = kwargs["region"]

    if "grayscale" in kwargs:
        grayscale = kwargs["grayscale"]

    if "loopSleep" in kwargs:
        loopSleep = kwargs["loopSleep"]

    if "timeToLive" in kwargs:
        timeToLive = kwargs["timeToLive"]

    if "clickCount" in kwargs:
        clickCount = kwargs["clickCount"]

    if "animationSleep" in kwargs:
        animationSleep = kwargs["animationSleep"]

    if "clickSleep" in kwargs:
        clickSleep = kwargs["clickSleep"]

    if "callbackSleep" in kwargs:
        callbackSleep = kwargs["callbackSleep"]

    if "moveSleep" in kwargs:
        moveSleep = kwargs["moveSleep"]

    if "callback" in kwargs:
        callback = kwargs["callback"]

    print("Finding " + imagePath)
    sleep(animationSleep)
    startTime = time.time()
    clickCoord = None
    move((50, 50))
    while True:

        # Protection sleep if loopSleep was ever 0
        sleep(0.05)

        if time.time() > startTime + timeToLive:
            return False

        tempImage = pyautogui.locateOnScreen(imagePath,
                                             confidence=confidence,
                                             region=region,
                                             grayscale=grayscale,
                                             )

        if tempImage is None:
            sleep(loopSleep)
            continue

        print("Found!")
        clickCoord = pyautogui.center(tempImage)
        break

    move(clickCoord)

    sleep(moveSleep)

    for x in range(clickCount):
        click()
        if clickCount != 1:
            sleep(clickSleep)

    move((50, 50))
    if callback is not None:
        if callback() is False:
            return False

    sleep(callbackSleep)

    return True

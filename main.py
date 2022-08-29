import keyboard

from utils import *

# Config
spot1Units = 1
spot2Units = 1
spot3Units = 1
spot4Units = 2

# Initializing window etc

unitsToTrain = spot1Units + spot2Units + spot3Units + spot4Units

windowTemp = pyautogui.getWindowsWithTitle("Galaxy Life")[0]
windowTemp.activate()

windowBox = (windowTemp.left + 50,
             windowTemp.top + 50,
             windowTemp.width - 50,
             windowTemp.height - 50
             )

if __name__ == '__main__':

    # Training Camp
    if not macroComponent(
            "pictures/trainingCamp.png",
            region=windowBox,
            confidence=0.6,
            animationSleep=0.6,
            callbackSleep=1
    ):
        keyboard.press_and_release("F5")

    # Training Soldiers
    if not macroComponent(
            "pictures/soldier.png",
            region=windowBox,
            confidence=0.7,
            animationSleep=0.5,
            clickCount=unitsToTrain,
            clickSleep=0.1,
            callbackSleep=1
    ):
        keyboard.press_and_release("F5")

    # X
    if not macroComponent(
            "pictures/x.png",
            region=windowBox,
            confidence=0.9,
            animationSleep=0.2,
            callbackSleep=1
    ):
        keyboard.press_and_release("F5")

    while True:

        # Galaxy name
        if not macroComponent(
                "pictures/galaxyName.png",
                region=windowBox,
                confidence=0.95,
                moveSleep=2,
                animationSleep=3,
                callbackSleep=3
        ):
            keyboard.press_and_release("F5")
            continue

        # Sparragon
        if not macroComponent(
                "pictures/sparragon.png",
                region=windowBox,
                confidence=0.8,
                animationSleep=5,
                moveSleep=0.2,
                callbackSleep=1
        ):
            keyboard.press_and_release("F5")
            continue

        # Attack
        if not macroComponent(
                "pictures/attack.png",
                region=windowBox,
                confidence=0.9,
                animationSleep=0.2,
                callbackSleep=2
        ):
            keyboard.press_and_release("F5")
            continue

        # Soldier in battle
        if not macroComponent(
                "pictures/soldierInBattle.png",
                region=windowBox,
                confidence=0.55,
                animationSleep=0.2,
                callbackSleep=0.1
        ):
            keyboard.press_and_release("F5")
            continue

        # Spot 1
        if not macroComponent(
                "pictures/spots/1.png",
                region=windowBox,
                confidence=0.8,
                animationSleep=0.3,
                clickCount=spot1Units,
                clickSleep=0.2,
                callbackSleep=0.1
        ):
            keyboard.press_and_release("F5")
            continue

        # Spot 2
        if not macroComponent(
                "pictures/spots/2.png",
                region=windowBox,
                confidence=0.8,
                animationSleep=0.3,
                clickCount=spot2Units,
                clickSleep=0.2,
                callbackSleep=0.1
        ):
            keyboard.press_and_release("F5")
            continue

        # Spot 3
        if not macroComponent(
                "pictures/spots/3.png",
                region=windowBox,
                confidence=0.8,
                animationSleep=0.3,
                clickCount=spot3Units,
                clickSleep=0.2,
                callbackSleep=0.1
        ):
            keyboard.press_and_release("F5")
            continue

        # Spot 4
        if not macroComponent(
                "pictures/spots/4.png",
                region=windowBox,
                confidence=0.8,
                animationSleep=0.3,
                clickCount=spot4Units,
                clickSleep=0.35,
                callbackSleep=0.1
        ):
            keyboard.press_and_release("F5")
            continue

        # Speed
        if not macroComponent(
                "pictures/speed.png",
                region=windowBox,
                confidence=0.8,
                animationSleep=0.2,
                clickCount=2,
                clickSleep=0.1,
                callbackSleep=0.1
        ):
            keyboard.press_and_release("F5")
            continue

        # End battle
        if not macroComponent(
                "pictures/endBattle.png",
                region=windowBox,
                confidence=0.8,
                animationSleep=0.1,
                callbackSleep=0.4,
                moveSleep=25,
        ):
            keyboard.press_and_release("F5")
            continue

        # Go home
        if not macroComponent(
                "pictures/goHome.png",
                region=windowBox,
                confidence=0.8,
                animationSleep=0.1,
                callbackSleep=0.1,
        ):
            keyboard.press_and_release("F5")
            continue

        # Training Camp
        if not macroComponent(
                "pictures/trainingCamp.png",
                region=windowBox,
                confidence=0.6,
                animationSleep=0.6,
                moveSleep=2,
                callbackSleep=1
        ):
            keyboard.press_and_release("F5")
            continue

        # Training Soldiers
        if not macroComponent(
                "pictures/soldier.png",
                region=windowBox,
                confidence=0.7,
                animationSleep=0.5,
                clickCount=unitsToTrain,
                clickSleep=0.1,
                callbackSleep=1
        ):
            keyboard.press_and_release("F5")
            continue

        # X
        if not macroComponent(
                "pictures/x.png",
                region=windowBox,
                confidence=0.9,
                animationSleep=0.2,
                callbackSleep=1
        ):
            keyboard.press_and_release("F5")
            continue

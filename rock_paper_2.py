import random
import cv2
import mediapipe as mp
import HandTrackingModule as htm
import time

wCam, hCam = 640,380
cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
detector = htm.handDetector(detectionCon=1)
tipIds = [4,8,12,16,20]
fingerCount = 0
fingers = []

def getUserChoice(userRightHanded):
    print("Using your Hand and raise up Rock, Paper, or Scissors")
    totalFingers = 0
    startTime = time.time()
    while time.time() - startTime < 8:
        success, img = cap.read()
        if userRightHanded == 1:
            img = cv2.flip(img, flipCode=1)
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        # print(lmList)
        if len(lmList) != 0:
            fingers = []
            if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            for id in range(1,5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                    fingers.append(1)

            totalFingers = fingers.count(1)
            cv2.imshow("Screen",img)
            cv2.waitKey(2)
    return totalFingers

def winnerDecide(num1, num2):
    if((num1 == 0 and num2 == 1) or (num1 == 2 and num2 == 3) or (num1 == 5 and num2 == 2)):
        return "TIE!"
    elif (num1 == 0 and num2 == 3) or (num1 == 2 and num2 == 2)or (num1 == 5 and num2 == 1):
        return "You Win!"
    else:
        return "Computer Wins!"

def main():
    userRightHanded = 0
    playGame = True
    print("WELCOME TO ROCK PAPER SCISSORS GAME!")
    # userHand = input("Which hand will you be playing with today? ('L' or 'R')")
    # userHand = userHand.lower()
    # print(userHand)
    # while userHand != "l" or userHand != "r":
    #     userHand = input("INVALID INPUT! Which hand to play with? ('L' or 'R')")
    #     userHand = userHand.lower()
    #     if(userHand == 'l'):
    #         userRightHanded = 1
    #         break
    #     elif(userHand == 'r'):
    #         userRightHanded = 0
    #         break
    while True:
        user_hand_preference = input("Are you right-handed or left-handed? ('L' or 'R')").lower()
        if user_hand_preference == "r":
            userRightHanded = 0
            break
        elif user_hand_preference == "l":
            userRightHanded = 1
            break
        else:
            print("Invalid input. Please enter 'l' or 'r'.")

    while playGame:
        while True:
            userChoice = getUserChoice(userRightHanded)
            if (userChoice == 0):
                print("Your Choice: ROCK")
                break
            elif (userChoice == 5):
                print("Your Choice: PAPER")
                break
            elif (userChoice == 2):
                print("Your Choice: SCISSORS ")
                break
            else:
                print("INVALID INPUT! Press raise 5 fingers for Paper, 2 for Scissors, and 0 for Rock \n")


        computerChoice = random.randint(1,3)


        if (computerChoice == 1):
            print("Computer Choice: ROCK")
        elif (computerChoice == 2):
            print("Computer Choice: PAPER")
        elif (computerChoice == 3):
            print("Computer Choice: SCISSORS ")

        result = winnerDecide(userChoice, computerChoice)
        print(result)
        print("Would you like to play again? ('Y' or 'N')")
        playAgain = input()
        playAgain = playAgain.lower()
        while playAgain != "y" or playAgain != "n":
            print("INVALID INPUT! Play Again? ('Y' or 'N')")
            playAgain = input()
            playAgain = playAgain.lower()
        if (playAgain == "N"):
             playGame = False


        for i in range(3, -1, -1):
            print(f"Countdown: {i} seconds")
            time.sleep(1)

if __name__ == "__main__":
    main()


# Divyansh Goyal's Mini Word Scramble Game

import math
import time
import random
import colorama
from colorama import Fore, Back, Style

colorama.init()

start = time.time()
# Intro.
print(
    f"{Fore.YELLOW}\
This is a game where you have 5 scrambled words which you need to unscramble.\n\
In the end, you will receive a score out of 15.\n\
If you get it right in the first attempt, you will get 3 points, then 2, then 1, then 0. {Style.RESET_ALL}\n\
"
)

score = 0
input1 = ""

# Word bank class for each level.
class WordBank:

    six_letters = [
        "invest",
        "debate",
        "family",
        "global",
        "leader",
        "normal",
        "obtain",
        "nearly",
        "played",
        "school",
    ]

    seven_letters = [
        "ability",
        "courage",
        "awesome",
        "element",
        "learned",
        "mission",
        "prepare",
        "section",
        "working",
        "booking",
    ]

    eight_letters = [
        "achieved",
        "champion",
        "hardware",
        "purposes",
        "websites",
        "advisory",
        "explorer",
        "premises",
        "workflow",
        "airports",
    ]

    nine_letters = [
        "batteries",
        "different",
        "liability",
        "addiction",
        "instances",
        "residence",
        "bandwidth",
        "directing",
        "ignorance",
        "ministers",
    ]

    ten_letters = [
        "functional",
        "connection",
        "accounting",
        "physicians",
        "brightness",
        "disconnect",
        "renovation",
        "cafeterias",
        "delicacies",
        "vegetarian",
    ]


def scramble(user_input):
    """Checks whether input in correct or incorrect and displays message accordingly."""

    input1 = input("Enter Answer: ")
    input1 = input1.lower()
    user_input = user_input.lower()
    count = 1
    global score
    while input1 != user_input:
        count += 1
        print(
            f"{Fore.RED}Incorrect! You have {4-count} attempt(s) left.{Style.RESET_ALL}"
        )
        input1 = input("Try again: ")
        if count > 2 and input1 != user_input:
            count = 0
            return f"{Fore.RED}Incorrect!{Style.RESET_ALL}\n\
{Fore.YELLOW}Correct Answer is: {user_input}\n{Style.RESET_ALL}\
.\n\
.\n\
.\n\
{Style.RESET_ALL}"
    if input1 == user_input:
        if count == 1:
            score += 3
        elif count == 2:
            score += 2
        else:
            score += 1
        return f"{Fore.GREEN}Well Done! Next Level!\n\
.\n\
.\n\
.\n\
{Style.RESET_ALL}"


def scrambler(user_input):
    """Takes the word and scrambles it a unique way each time the game is played."""

    l = []
    length = len(user_input)
    randomnum = random.sample(range(length), length)
    for i in range(length):
        l.append(user_input[randomnum[i]].lower())
    print(l)


# Object for the WordBank class
word = WordBank()

# Generates a random integer
random_word = random.randint(0, 9)

# Level One
print(Fore.WHITE + "This is Level One")
scrambler(word.six_letters[random_word])
print(scramble(word.six_letters[random_word]))

# Level Two
print("This is Level Two")
scrambler(word.seven_letters[random_word])
print(scramble(word.seven_letters[random_word]))

# Level Three
print("This is Level Three")
scrambler(word.eight_letters[random_word])
print(scramble(word.eight_letters[random_word]))

# Level Four
print("This is Level Four")
scrambler(word.nine_letters[random_word])
print(scramble(word.nine_letters[random_word]))

# Level Five
print("This is Level Five")
scrambler(word.ten_letters[random_word])
print(scramble(word.ten_letters[random_word]))

# Conclusion Screen
print("\n . \n . \n .")
if score >= 7:
    print(
        Back.BLACK
        + Fore.GREEN
        + f"The game has concluded, your score is: {str(score)}/15! {Style.RESET_ALL}"
    )
else:
    print(
        Back.BLACK
        + Fore.RED
        + f"The game has concluded, your score is: {str(score)}/15! {Style.RESET_ALL}"
    )

time = time.time() - start
seconds = math.modf(time)

if time <= 60.00:
    print(f"You played this game for about {round(time, 2)} seconds")
else:
    print(
        f"You played this game for about {int(time/60)} mins:{int((seconds[0]*60))} seconds"
    )

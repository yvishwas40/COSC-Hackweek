import random
import time
import os

# Optional: clear screen function for better visuals
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# ASCII frames for animation
dice_animation = [
    "[       ]",
    "[ *     ]",
    "[   *   ]",
    "[     * ]",
    "[ *   * ]",
    "[  ***  ]"
]

def roll_dice():
    clear()
    print("Rolling the dice...")
    for i in range(6):
        print(dice_animation[i % len(dice_animation)])
        time.sleep(0.2)
        clear()
    
    # suspense countdown
    for i in range(3, 0, -1):
        print(f"Revealing in {i}...")
        time.sleep(0.5)
        clear()
    
    result = random.randint(1, 6)
    print(f"You rolled a 🎲 {result}!\n")

while True:
    input("Press ENTER to roll the dice (or Ctrl+C to quit) ")
    roll_dice()

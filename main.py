import os
import time
from dotenv import load_dotenv
from openai import OpenAI
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key and base URL from environment variables
api_key = os.getenv('OPENAI_API_KEY')
base_url = os.getenv('BASE_URL', 'https://api.openai.com')

# Initialize the OpenAI client with the custom base URL if provided
client = OpenAI(api_key=api_key, base_url=base_url)


def get_openai_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()


def select_theme():
    themes = {
        '1': "🚀 Space Adventure: You find yourself on a spaceship drifting through the vast emptiness of space. There are control panels to your left and right, and a door leading to the cockpit. What do you do?",
        '2': "🏰 Medieval Quest: You stand in a medieval village square. To the north, there's a castle, and to the east, a dark forest. What do you do?",
        '3': "🧙‍♂️ Wizard's Journey: You are a wizard in a mystical land. In front of you is an ancient spellbook and a path leading to a hidden cave. What do you do?",
        '4': "🔍 Detective Mystery: You are a detective in 1940s New York. There's a crime scene to investigate and a suspect to interrogate. What do you do?",
        '5': "🌋 Volcano Expedition: You are an explorer on a volcanic island. There's a path leading to the volcano's summit and another to a hidden cave. What do you do?",
        '6': "🏜️ Desert Survival: You are stranded in a vast desert. There's an oasis to the north and a sand dune to the east. What do you do?",
        '7': "🎢 Amusement Park Adventure: You are in a haunted amusement park. There's a spooky roller coaster to the north and a haunted house to the east. What do you do?",
        '8': "🐉 Dragon's Lair: You are a knight standing before a dragon's lair. There's a path leading inside and another to a nearby village. What do you do?",
        '9': "🧛 Vampire Hunt: You are a vampire hunter in a dark, foggy town. There's a crypt to the north and a tavern to the east. What do you do?",
        '10': "🌌 Galactic War: You are a commander in a galactic war. There are enemy ships approaching and an allied base to defend. What do you do?",
        '11': "Custom Theme"
    }

    print(Fore.CYAN + "Select a theme for your adventure:")
    for key, description in themes.items():
        print(f"{key}: {description.split(':')[0]}")

    choice = input(Fore.YELLOW + "Enter the number corresponding to your choice: ")

    if choice == '11':
        custom_theme = input(Fore.YELLOW + "Enter a custom theme description: ")
        print(Fore.MAGENTA + "-" * 50)
        print(Fore.CYAN + "Generating custom theme...")
        intro_prompt = f"This is a text-based game, and you need to write a short introduction for the following theme: {custom_theme}. Make it short, 30 words max."
        intro = get_openai_response(intro_prompt)
        print(Fore.GREEN + f"\n{intro}\n")
        input(Fore.CYAN + "Press Enter to continue...")
        return intro

    return themes.get(choice, themes['1'])


def generate_options(prompt):
    options_prompt = f"Based on the following scenario, provide four different short actions the player can take: {prompt}. Make sure the 4 actions are short, 10 words max, and don't use numbers. Add emojis at the start."
    print(Fore.CYAN + "Generating options...")
    response = get_openai_response(options_prompt)
    options = response.split("\n")
    return [option.strip() for option in options if option.strip()]


def select_game_mode():
    print(Fore.CYAN + "Select a game mode:")
    print("1: Play with generated options")
    print("2: Play by typing your own actions")
    print("3: Enter a custom prompt")

    choice = input(Fore.YELLOW + "Enter the number corresponding to your choice: ")
    return choice


def main():
    divider = Fore.MAGENTA + "-" * 50

    logo = r"""
   ___   ____  ______        __      ___                  __  _____              
  / _ | /  _/ /_  __/____ __/ /_____/ _ )___ ____ ___ ___/ / / ___/__ ___ _  ___ 
 / __ |_/ /    / / / -_) \ / __/___/ _  / _ `(_-</ -_) _  / / (_ / _ `/  ' \/ -_)
/_/ |_/___/   /_/  \__/_\_\\__/   /____/\_,_/___/\__/\_,_/  \___/\_,_/_/_/_/\__/
        """
    print("--------------------------------------------------")
    print(logo)
    print("AI Text-Based Game")
    print("Made by 💜 from Zigao Wang.")
    print("This project is licensed under MIT License.")
    print("GitHub Repo: https://github.com/ZigaoWang/ai-text-based-game/")
    print("--------------------------------------------------")
    print(Fore.MAGENTA + "You can type your actions to interact with the game world.")
    print(Fore.MAGENTA + "Type 'quit' to exit the game.")
    print(divider)

    # Select the game mode
    game_mode = select_game_mode()

    if game_mode == '3':
        custom_prompt = input(Fore.YELLOW + "Enter your custom prompt: ")
        print(Fore.MAGENTA + "-" * 50)
        print(Fore.GREEN + custom_prompt)
        print(divider)
        input(Fore.CYAN + "Press Enter to continue...")

        # Maintain context of the game
        context = custom_prompt

        # Ask the player how they want to play the custom prompt
        game_mode = select_game_mode()
    else:
        # Select and display the initial prompt based on the chosen theme
        initial_prompt = select_theme()
        print(Fore.GREEN + initial_prompt)
        print(divider)
        input(Fore.CYAN + "Press Enter to continue...")

        # Maintain context of the game
        context = initial_prompt

    while True:
        if game_mode == '1':
            # Generate options for the player
            options = generate_options(context)
            for i, option in enumerate(options, 1):
                print(Fore.YELLOW + f"{i}. {option}")

            # User input for the next action
            user_choice = input(Fore.YELLOW + "Select an action by entering the number: ")

            if user_choice.lower() == 'quit':
                print(Fore.MAGENTA + "Thanks for playing! See you next time! 🎮")
                break

            # Validate user choice
            try:
                user_action = options[int(user_choice) - 1]
            except (IndexError, ValueError):
                print(Fore.RED + "Invalid choice. Please select a valid option.")
                continue

        else:
            # User input for the next action
            user_action = input(Fore.YELLOW + "Your action: ")

            if user_action.lower() == 'quit':
                print(Fore.MAGENTA + "Thanks for playing! See you next time! 🎮")
                break

        # Append the user's action to the context
        context += f"\nYou: {user_action}\nGame:"

        # Get the response from OpenAI
        print(Fore.CYAN + "Generating description...")
        response_prompt = f"{context} Keep the description short, 30 words max. Ask the player what they want to do next."
        response = get_openai_response(response_prompt)

        # Append the response to the context for further context
        context += f" {response}"

        print(divider)
        print(Fore.GREEN, end='')
        print(response)
        print(divider)

        input(Fore.CYAN + "Press Enter to continue...")


if __name__ == "__main__":
    main()
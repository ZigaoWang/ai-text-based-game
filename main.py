import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')

# Initialize the OpenAI client
client = OpenAI(api_key=api_key)


def get_openai_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150,
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

    print("Select a theme for your adventure:")
    for key, description in themes.items():
        print(f"{key}: {description.split(':')[0]}")

    choice = input("Enter the number corresponding to your choice: ")

    if choice == '11':
        custom_theme = input("Enter a custom theme description: ")
        intro_prompt = f"Create an introduction for the following theme: {custom_theme}"
        intro = get_openai_response(intro_prompt)
        print(f"\n{intro}\n")
        return intro

    return themes.get(choice, themes['1'])


def generate_options(prompt):
    options_prompt = f"Based on the following scenario, provide four different short actions the player can take: {prompt}. Make sure the 4 actions are short, 10 words max, and dont use numbers. Add emojis at the start."
    response = get_openai_response(options_prompt)
    options = response.split("\n")
    return [option.strip() for option in options if option.strip()]


def main():
    print("Welcome to the OpenAI Text Adventure Game! 🌟")
    print("You can type your actions to interact with the game world.")
    print("Type 'quit' to exit the game.\n")

    # Select and display the initial prompt based on the chosen theme
    initial_prompt = select_theme()
    print(initial_prompt)

    # Maintain context of the game
    context = initial_prompt

    while True:
        print("\nGenerating options...")
        # Generate options for the user
        options = generate_options(context)

        print("\nWhat do you want to do?")
        for i, option in enumerate(options[:4], 1):
            print(f"{i}. {option}")
        print("5. 📝 Custom")

        user_choice = input("Enter the number corresponding to your choice: ")

        if user_choice.lower() == 'quit':
            print("Thanks for playing! 🎮")
            break

        if user_choice == '5':
            user_input = input("Enter your custom action: ")
        else:
            user_input = options[int(user_choice) - 1]

        # Append the user's action to the context
        context += f"\nYou: {user_input}\nGame:"

        # Get the response from OpenAI
        response = get_openai_response(context)

        # Append the response to the context for further context
        context += f" {response}"

        # Print the response for the user to see
        print(response)


if __name__ == "__main__":
    main()
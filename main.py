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

def main():
    print("Welcome to the OpenAI Text Adventure Game!")
    print("You can type your actions to interact with the game world.")
    print("Type 'quit' to exit the game.\n")

    # Initial prompt to start the adventure
    initial_prompt = "You find yourself on a spaceship drifting through the vast emptiness of space. There are control panels to your left and right, and a door leading to the cockpit. What do you do?"

    print(initial_prompt)

    # Maintain context of the game
    context = initial_prompt

    while True:
        user_input = input("\nYour action: ")

        if user_input.lower() == 'quit':
            print("Thanks for playing!")
            break

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
# AI Text-Based Game

Welcome to the AI Text-Based Game! This is a text-based adventure game powered by OpenAI's models. You can choose different themes and interact with the game world by typing your actions or selecting from generated options.

## Features

- Multiple adventure themes to choose from.
- Play by selecting from generated options or typing your own actions.
- Customizable prompts for a personalized gaming experience.
- Powered by OpenAI's language models.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- An OpenAI API key

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/ZigaoWang/ai-text-based-game.git
    cd ai-text-based-game
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv .venv
    ```

3. **Activate the virtual environment:**

    - On Windows:

        ```sh
        .venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```sh
        source .venv/bin/activate
        ```

4. **Install the required dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

5. **Set up your environment variables:**

    - Copy the example environment file:

        ```sh
        cp .env.example .env
        ```

    - Open the `.env` file and add your OpenAI API key:

        ```plaintext
        # .env

        # OpenAI API key
        OPENAI_API_KEY=your_openai_api_key_here
        ```

## Usage

Run the game by executing the following command:

```sh
python main.py
```

### Game Modes

1. **Play with generated options:**
    - Select actions from a list of generated options.

2. **Play by typing your own actions:**
    - Type your own actions to interact with the game world.

3. **Enter a custom prompt:**
    - Enter a custom prompt to start the game and then choose how you want to play.

### Example

```sh
python main.py
```

```
--------------------------------------------------

   ___   ____  ______        __      ___                  __  _____              
  / _ | /  _/ /_  __/____ __/ /_____/ _ )___ ____ ___ ___/ / / ___/__ ___ _  ___ 
 / __ |_/ /    / / / -_) \ / __/___/ _  / _ `(_-</ -_) _  / / (_ / _ `/  ' \/ -_)
/_/ |_/___/   /_/  \__/_\_\\__/   /____/\_,_/___/\__/\_,_/  \___/\_,_/_/_/_/\__/
        
AI Text-Based Game
Made by 💜 from Zigao Wang.
This project is licensed under MIT License.
GitHub Repo: https://github.com/ZigaoWang/ai-text-based-game/
--------------------------------------------------
You can type your actions to interact with the game world.
Type 'quit' to exit the game.
--------------------------------------------------
Select a game mode:
1: Play with generated options
2: Play by typing your own actions
3: Enter a custom prompt
Enter the number corresponding to your choice: 1
Select a theme for your adventure:
1: 🚀 Space Adventure
2: 🏰 Medieval Quest
3: 🧙‍♂️ Wizard's Journey
4: 🔍 Detective Mystery
5: 🌋 Volcano Expedition
6: 🏜️ Desert Survival
7: 🎢 Amusement Park Adventure
8: 🐉 Dragon's Lair
9: 🧛 Vampire Hunt
10: 🌌 Galactic War
11: Custom Theme
Enter the number corresponding to your choice: 1
🚀 Space Adventure: You find yourself on a spaceship drifting through the vast emptiness of space. There are control panels to your left and right, and a door leading to the cockpit. What do you do?
--------------------------------------------------
Press Enter to continue...
```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please contact Zigao Wang.
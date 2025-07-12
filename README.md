# Wordle
Play the game to sharp your brain
# Pygame Wordle Game

A simple Wordle-inspired game built using Pygame.

## Features

* **Classic Wordle Gameplay:** Guess the 5-letter word within a limited number of attempts.
* **Visual Feedback:** Letters are colored green (correct letter, correct position), yellow (correct letter, wrong position), or gray (letter not in word).
* **Dynamic Word List Loading:** The game loads its target words from a `word_list.txt` file, making it easy to customize.

## Setup and Installation

To run this game, you'll need Python and Pygame installed.

1.  **Clone the repository (or download the files):**
    ```bash
    git clone [https://github.com/YourGitHubUsername/Pygame-Wordle-Game.git](https://github.com/YourGitHubUsername/Pygame-Wordle-Game.git)
    cd Pygame-Wordle-Game
    ```
    (Replace `YourGitHubUsername/Pygame-Wordle-Game` with your actual repository path if you're setting up a new repo.)

2.  **Install dependencies:**
    It's recommended to use a virtual environment.
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    
    pip install -r requirements.txt
    ```

3.  **Ensure `word_list.txt` exists:**
    Make sure you have a file named `word_list.txt` in the same directory as `Exp5.py`. This file should contain one 5-letter word per line. A large sample word list is usually provided with the game or can be created from various online resources.

    Example `word_list.txt` content:
    ```
    apple
    baker
    crane
    slate
    ```

## How to Run

After setting up, run the game using:

```bash
python Exp5.py

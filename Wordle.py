import pygame
import random
from collections import Counter

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 650, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
GRAY = (169, 169, 169)
FONT = pygame.font.Font(None, 50)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wordle Game")

# Function to load words from a file
def load_words(filename):
    with open(filename, 'r') as file:
        words = file.read().splitlines()
    return [word for word in words if len(word) == 5]  # Filter for 5-letter words

# Load the word list dynamically
WORD_LIST = load_words('word_list.txt')  # Ensure you have a file named 'word_list.txt'
TARGET_WORD = random.choice(WORD_LIST)
MAX_ATTEMPTS = 5
attempts = []

# Wordle feedback function
def wordle_feedback(guess, target):
    feedback = []
    target_counter = Counter(target)
    for i in range(len(guess)):
        if guess[i] == target[i]:
            feedback.append(GREEN)  # Correct letter in correct position
            target_counter[guess[i]] -= 1
        elif guess[i] in target and target_counter[guess[i]] > 0:
            feedback.append(YELLOW)  # Correct letter in wrong position
            target_counter[guess[i]] -= 1
        else:
            feedback.append(GRAY)  # Wrong letter
    return feedback

# Draw the game screen
def draw_screen(current_guess, game_over):
    screen.fill(WHITE)
    for i, (guess, feedback) in enumerate(attempts):
        for j in range(5):
            letter = guess[j] if j < len(guess) else " "
            color = feedback[j] if j < len(feedback) else GRAY
            pygame.draw.rect(screen, color, (j * 100 + 50, i * 100 + 50, 90, 90))
            text = FONT.render(letter.upper(), True, BLACK)
            screen.blit(text, (j * 100 + 75, i * 100 + 75))
    
    # Display the current guess
    for j, letter in enumerate(current_guess):
        text = FONT.render(letter.upper(), True, BLACK)
        screen.blit(text, (j * 100 + 75, len(attempts) * 100 + 75))
    
    # Display game over message if applicable
    if game_over:
        game_over_text = FONT.render(f"Game Over! The word was: {TARGET_WORD}", True, BLACK)
        screen.blit(game_over_text, (50, HEIGHT - 100))
    
    pygame.display.flip()

# Main function
def main():
    running = True
    current_guess = ""
    clock = pygame.time.Clock()
    game_over = False
    
    while running:
        draw_screen(current_guess, game_over)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and len(current_guess) == 5 and not game_over:
                    feedback = wordle_feedback(current_guess, TARGET_WORD)
                    attempts.append((current_guess, feedback))
                    if current_guess == TARGET_WORD:
                        print(f"Congratulations! You guessed the word: {TARGET_WORD}")
                        game_over = True
                    elif len(attempts) >= MAX_ATTEMPTS:
                        print(f"Game Over! The word was: {TARGET_WORD}")
                        game_over = True
                    current_guess = ""
                elif event.key == pygame.K_BACKSPACE:
                    current_guess = current_guess[:-1]
                elif len(current_guess) < 5 and event.unicode.isalpha():
                    current_guess += event.unicode.lower()
        clock.tick(30)
    pygame.quit()

if __name__ == "__main__":
    main()

import pygame
import random

pygame.init()

# Window dimensions
WIDTH, HEIGHT = 600, 400  # Width and height of the game window
GRID_SIZE = 20  # Grid size (snake and food move on this grid)
SPEED = 8  # Initial speed
SCORE_TO_LEVEL_UP = 4  # How many points are needed to level up

# Define colors (in RGB format)
WHITE = (255, 255, 255)  # White color
GREEN = (0, 255, 0)  # Green color
DARK_GREEN = (0, 150, 0)  # Dark green color
RED = (255, 0, 0)  # Red color (food)
BLACK = (0, 0, 0)  # Black color (background color)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Create a window
pygame.display.set_caption("Snake Game")  # Set the window title

# Initial snake coordinates
snake = [(100, 100), (90, 100), (80, 100)]  # The first three segments of the snake
snake_dir = (GRID_SIZE, 0)  # Snake movement direction (to the right)

# Generate random food coordinates
food = (random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
        random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)

score = 0  # Score
level = 1  # Initial level
running = True  # Is the game running?
game_over = False  # Is the game over?
menu = True  # Should the menu be displayed?
paused = False  # Is the game paused?
clock = pygame.time.Clock()  # Clock to control game frames

# Function to randomly place food
def generate_food():
    while True:
        new_food = (random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
                    random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)
        if new_food not in snake:  # Food should not overlap with the snake's body
            return new_food

# Function to display text on the screen
def draw_text(text, size, color, x, y):
    font = pygame.font.Font(None, size)  # Set font size
    render_text = font.render(text, True, color)  # Render text as an image
    text_rect = render_text.get_rect(center=(x, y))  # Set center coordinates
    screen.blit(render_text, text_rect)  # Display on screen

# Function to show the main menu
def show_menu():
    screen.fill(BLACK)  # Fill screen with black color
    draw_text("SNAKE GAME", WIDTH // 10, GREEN, WIDTH // 2, HEIGHT // 4)  # Display game title
    start_button = pygame.Rect(WIDTH // 2 - 75, HEIGHT // 2 - 20, 150, 50)  # Start button dimensions
    pygame.draw.rect(screen, WHITE, start_button)  # Draw start button
    draw_text("Start", WIDTH // 15, BLACK, WIDTH // 2, HEIGHT // 2 + 5)  # Display button text
    pygame.display.flip()  # Update screen
    return start_button  # Return button

# Wait while the menu is displayed
while menu:
    start_button = show_menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Close the game
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:  # When mouse button is pressed
            if start_button.collidepoint(event.pos):  # If the start button is clicked
                menu = False

# Main game loop
while running:
    screen.fill(BLACK)  # Clear screen
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Close the game
        elif event.type == pygame.KEYDOWN:  # When a key is pressed
            if game_over:
                if event.key == pygame.K_q:  # Pressing Q exits
                    running = False
            else:
                # Control snake direction
                if event.key == pygame.K_UP and snake_dir != (0, GRID_SIZE):
                    snake_dir = (0, -GRID_SIZE)
                elif event.key == pygame.K_DOWN and snake_dir != (0, -GRID_SIZE):
                    snake_dir = (0, GRID_SIZE)
                elif event.key == pygame.K_LEFT and snake_dir != (GRID_SIZE, 0):
                    snake_dir = (-GRID_SIZE, 0)
                elif event.key == pygame.K_RIGHT and snake_dir != (-GRID_SIZE, 0):
                    snake_dir = (GRID_SIZE, 0)
                elif event.key == pygame.K_p:
                    paused = not paused  # Pause or resume the game
    
    if paused: # If the game is paused
        draw_text("PAUSED", WIDTH // 10, WHITE, WIDTH // 2, HEIGHT // 2) # Display text
        pygame.display.flip() # Update screen
        continue  # Skip to the next cycle if paused
    
    if game_over:  # If the game is over
        draw_text("YOU LOSE", WIDTH // 10, RED, WIDTH // 2, HEIGHT // 3) # Display text
        pygame.display.flip() # Update screen
        continue # Skip to the next cycle
    
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1]) # New snake head position
    new_head = (new_head[0] % WIDTH, new_head[1] % HEIGHT)  # Wrap around screen edges
    
    if new_head in snake:  # If snake collides with itself
        game_over = True # Game over
    
    if not game_over: # If the game is not over
        snake.insert(0, new_head) # Insert new head position
        if new_head == food: # If snake eats the food
            score += 1 # Increase score
            food = generate_food() # Generate new food
            if score % SCORE_TO_LEVEL_UP == 0: # Level up condition
                level += 1 # Increase level
                SPEED += 1 # Increase speed
        else: 
            snake.pop() # Remove the last segment
    
    pygame.draw.rect(screen, DARK_GREEN, (snake[0][0], snake[0][1], GRID_SIZE, GRID_SIZE)) # Draw snake head
    for segment in snake[1:]: # Draw snake body segments
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE)) # Draw snake body
    
    pygame.draw.rect(screen, RED, (food[0], food[1], GRID_SIZE, GRID_SIZE)) # Draw food
    
    draw_text(f"Score: {score}", WIDTH // 25, WHITE, 70, 15)
    draw_text(f"Level: {level}", WIDTH // 25, WHITE, 70, 35)
    
    pygame.display.flip()
    clock.tick(SPEED)  # Control speed

pygame.quit()
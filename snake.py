import pygame
import random

# Set up the display
width, height = 640, 480
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

pygame.init()

# Define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)

# Set up the snake and food
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_position = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
food_spawned = True

# Initial direction
direction = 'RIGHT'
change_to = direction

# Set up game settings
game_over = False
score = 0
clock = pygame.time.Clock()
snake_speed = 15

# Function to display score
def show_score(choice=1):
    font = pygame.font.SysFont('monaco', 24)
    score_surface = font.render('Score: {}'.format(score), True, white)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (80, 10)
    else:
        score_rect.midtop = (320, 100)
    display.blit(score_surface, score_rect)

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        # Change the direction of the snake with arrow keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            if event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'

    # Update the snake's direction
    direction = change_to

    # Update the snake's position
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Snake body mechanism
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 1
        food_spawned = False
    else:
        snake_body.pop()

    # Respawn food
    if not food_spawned:
        food_position = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
        food_spawned = True

    # Check for game over conditions
    if snake_position[0] < 0 or snake_position[0] > width - 10:
        game_over = True
    if snake_position[1] < 0 or snake_position[1] > height - 10:
        game_over = True
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over = True
    
    # Clear the display
    display.fill(black)

    # Draw the snake
    for pos in snake_body:
        pygame.draw.rect(display, white, pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw the food
    pygame.draw.rect(display, red, pygame.Rect(food_position[0], food_position[1], 10, 10))

    # Show the score
    show_score()

    # Refresh the display
    pygame.display.update()

    # Frame rate
    clock.tick(snake_speed)
    
pygame.quit()


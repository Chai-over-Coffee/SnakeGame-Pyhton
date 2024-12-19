import pygame
import random
pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Screen dimensions
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game with Grid")

# Grid settings
grid_size = 20
grid_width = screen_width // grid_size
grid_height = screen_height // grid_size

# Snake properties
snake_block_size = grid_size
snake_speed = 6

# Font for displaying score
font_style = pygame.font.SysFont(None, 30)

# Function to display the score
def display_score(score):
    value = font_style.render("Your Score: " + str(score), True, white)
    screen.blit(value, [0, 0])

# Function to draw the snake
def draw_snake(snake_block_size, snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, green, [x, y, snake_block_size, snake_block_size])

# Function to display a message on the screen
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width / 6, screen_height / 3])

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    x1 = screen_width / 2
    y1 = screen_height / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    clock = pygame.time.Clock()

    foodx = round(random.randrange(0, screen_width - snake_block_size) / grid_size) * grid_size
    foody = round(random.randrange(0, screen_height - snake_block_size) / grid_size) * grid_size

    while not game_over:
        while game_close == True:
            screen.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block_size
                    x1_change = 0

        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(black)

        # Draw grid
        for x in range(0, screen_width, grid_size):
            pygame.draw.line(screen, white, (x, 0), (x, screen_height))
        for y in range(0, screen_height, grid_size):
            pygame.draw.line(screen, white, (0, y), (screen_width, y))

        pygame.draw.rect(screen, red, [foodx, foody, snake_block_size, snake_block_size])
        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(snake_block_size, snake_list)
        display_score(snake_length - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - snake_block_size) / grid_size) * grid_size
            foody = round(random.randrange(0, screen_height - snake_block_size) / grid_size) * grid_size
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()

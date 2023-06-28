import pygame
from pygame.locals import *
import sys
import random

# Set up the screen
WIDTH, HEIGHT = 1280, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Load the red heart soul image
SOUL_IMAGE = pygame.image.load("assets/rheart.png")

# Import the Soul class from the soul module
from soul import Soul

# Define colors
DARK_ORANGE = (255, 140, 0)

# Define the movement speed
MOVE_SPEED = 5

# Create the soul object
soul = Soul(0, 0, SOUL_IMAGE)  # Initial position doesn't matter for now

# Create the box object
box_x = 400
box_y = 150
box_width = 400
box_height = 200

# Calculate the maximum position for the soul to spawn inside the box
max_soul_x = box_x + box_width - soul.image.get_width()
max_soul_y = box_y + box_height - soul.image.get_height()

# Randomly position the soul inside the box
soul.x = random.randint(box_x, max_soul_x)
soul.y = random.randint(box_y, max_soul_y)

# Game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Handle keyboard events
    dx, dy = 0, 0
    if keys[K_UP]:
        dy -= MOVE_SPEED
    if keys[K_DOWN]:
        dy += MOVE_SPEED
    if keys[K_LEFT]:
        dx -= MOVE_SPEED
    if keys[K_RIGHT]:
        dx += MOVE_SPEED

    # Calculate the potential new position of the soul
    new_x = soul.x + dx
    new_y = soul.y + dy

    # Check if the potential new position is inside the box
    if (
        box_x <= new_x <= max_soul_x
        and box_y <= new_y <= max_soul_y
    ):
        soul.move(dx, dy)  # Update soul's position

    SCREEN.fill((0, 0, 0))  # Black background

    # Draw the box
    pygame.draw.rect(SCREEN, DARK_ORANGE, (box_x, box_y, box_width, box_height), 1)

    # Draw the soul
    soul.draw(SCREEN)

    pygame.display.flip()
    clock.tick(60)  # Limit frame rate to 60 FPS

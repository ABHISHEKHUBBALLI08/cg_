import pygame
import sys
import math
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Virtual Cricket Ground")

# Colors
GREEN = (34, 139, 34)    # Green color for the ground
BROWN = (139, 69, 19)    # Brown color for the pitch
WHITE = (255, 255, 255)  # White color for boundary and stumps
RED = (255, 0, 0)        # Red color for players
GRAY = (192, 192, 192)   # Gray color for 30-yard circle

# Constants for ground dimensions
GROUND_RADIUS = 300
INNER_CIRCLE_RADIUS = GROUND_RADIUS - 80
OUTER_CIRCLE_RADIUS = GROUND_RADIUS - 40
PITCH_WIDTH = 160
PITCH_HEIGHT = 280
STUMP_HEIGHT = 40
STUMP_WIDTH = 5
BOUNDARY_RADIUS = GROUND_RADIUS + 10  # Boundary extends just beyond the ground radius

# Positions
center_x, center_y = WIDTH // 2, HEIGHT // 2

# Player positions (example initial positions, you can adjust these)
player_positions = []

def randomize_player_positions():
    global player_positions
    player_positions = []
    for _ in range(7):
        # Generate players within the inner circle
        angle = random.uniform(0, 2 * math.pi)
        x = center_x + int(INNER_CIRCLE_RADIUS * math.cos(angle))
        y = center_y + int(INNER_CIRCLE_RADIUS * math.sin(angle))
        player_positions.append((x, y))
    
    for _ in range(4):
        # Generate players outside the inner circle but within the outer circle
        angle = random.uniform(0, 2 * math.pi)
        x = center_x + int(OUTER_CIRCLE_RADIUS * math.cos(angle))
        y = center_y + int(OUTER_CIRCLE_RADIUS * math.sin(angle))
        player_positions.append((x, y))

# Initial random positioning of players
randomize_player_positions()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o:
                # Option 'o' - 7 players within 1st circle, 4 players within 2nd circle
                player_positions = []
                for _ in range(7):
                    # Generate players within the inner circle
                    angle = random.uniform(0, 2 * math.pi)
                    x = center_x + int(INNER_CIRCLE_RADIUS * math.cos(angle))
                    y = center_y + int(INNER_CIRCLE_RADIUS * math.sin(angle))
                    player_positions.append((x, y))
                
                for _ in range(4):
                    # Generate players outside the inner circle but within the outer circle
                    angle = random.uniform(0, 2 * math.pi)
                    x = center_x + int(OUTER_CIRCLE_RADIUS * math.cos(angle))
                    y = center_y + int(OUTER_CIRCLE_RADIUS * math.sin(angle))
                    player_positions.append((x, y))
            elif event.key == pygame.K_p:
                # Option 'p' - 9 players within 1st circle, 2 players outside 1st circle but within 2nd circle
                player_positions = []
                for _ in range(9):
                    # Generate players within the inner circle
                    angle = random.uniform(0, 2 * math.pi)
                    x = center_x + int(INNER_CIRCLE_RADIUS * math.cos(angle))
                    y = center_y + int(INNER_CIRCLE_RADIUS * math.sin(angle))
                    player_positions.append((x, y))
                
                for _ in range(2):
                    # Generate players outside the inner circle but within the outer circle
                    angle = random.uniform(0, 2 * math.pi)
                    x = center_x + int(OUTER_CIRCLE_RADIUS * math.cos(angle))
                    y = center_y + int(OUTER_CIRCLE_RADIUS * math.sin(angle))
                    player_positions.append((x, y))

    # Fill the screen with green for the ground
    screen.fill(GREEN)

    # Draw the circular ground
    pygame.draw.circle(screen, GREEN, (center_x, center_y), GROUND_RADIUS)

    # Draw the pitch (brown area)
    pitch_x = center_x - PITCH_WIDTH // 2
    pitch_y = center_y - PITCH_HEIGHT // 2
    pygame.draw.rect(screen, BROWN, (pitch_x, pitch_y, PITCH_WIDTH, PITCH_HEIGHT))

    # Draw the boundary line (white)
    pygame.draw.circle(screen, WHITE, (center_x, center_y), BOUNDARY_RADIUS, 5)  # Cricket boundary

    # Draw stumps on both sides of the pitch
    stump_y = center_y - PITCH_HEIGHT // 2 - STUMP_HEIGHT

    # Off-stump (left side)
    pygame.draw.rect(screen, WHITE, (pitch_x - STUMP_WIDTH // 2, stump_y, STUMP_WIDTH, STUMP_HEIGHT))  # Off stump

    # Middle-stump (center)
    pygame.draw.rect(screen, WHITE, (center_x - STUMP_WIDTH // 2, stump_y, STUMP_WIDTH, STUMP_HEIGHT))  # Middle stump

    # Leg-stump (right side)
    pygame.draw.rect(screen, WHITE, (pitch_x + PITCH_WIDTH - STUMP_WIDTH // 2, stump_y, STUMP_WIDTH, STUMP_HEIGHT))  # Leg stump

    # Stumps on the other side of the pitch (mirrored positions)
    pygame.draw.rect(screen, WHITE, (pitch_x - STUMP_WIDTH // 2, stump_y + PITCH_HEIGHT + STUMP_HEIGHT, STUMP_WIDTH, STUMP_HEIGHT))  # Off stump
    pygame.draw.rect(screen, WHITE, (center_x - STUMP_WIDTH // 2, stump_y + PITCH_HEIGHT + STUMP_HEIGHT, STUMP_WIDTH, STUMP_HEIGHT))  # Middle stump
    pygame.draw.rect(screen, WHITE, (pitch_x + PITCH_WIDTH - STUMP_WIDTH // 2, stump_y + PITCH_HEIGHT + STUMP_HEIGHT, STUMP_WIDTH, STUMP_HEIGHT))  # Leg stump

    # Draw players (red circles)
    for position in player_positions:
        pygame.draw.circle(screen, RED, position, 10)

    # Draw the 30-yard circle (gray)
    pygame.draw.circle(screen, GRAY, (center_x, center_y), GROUND_RADIUS - 80, 5)

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()
sys.exit()

import pygame
import time

# Bus stop data (bus stops and their times)
bus_stops = [
    {"stop": "Digman", "time": "11:00 AM"},
    {"stop": "Mohawk","time": "12:00 PM"},
    {"stop": "Rafuse", "time": "1:00 PM"},
    {"stop": "East Gym", "time": "2:00 PM"},
]

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bus Route Time")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# Font
font = pygame.font.Font(None, 36)

# Clock for managing frame rate
clock = pygame.time.Clock()

def draw_bus_route(current_stop_index):
    """Draws the bus route and highlights the current stop."""
    screen.fill(WHITE)

    # Draw the bus stops
    y_offset = 50  # Starting vertical position
    for i, stop in enumerate(bus_stops):
        stop_text = f"{stop['stop']} - {stop['time']}"
        color = BLUE if i == current_stop_index else BLACK
        text_surface = font.render(stop_text, True, color)
        screen.blit(text_surface, (50, y_offset))
        y_offset += 50

    # Draw the "bus" indicator
    bus_y = 50 + current_stop_index * 50 - 10
    pygame.draw.circle(screen, GREEN, (30, bus_y), 10)

    # Update the display
    pygame.display.flip()

def main():
    running = True
    current_stop_index = 0

    # Time tracking for bus stop progression
    start_time = time.time()
    stop_duration = 5  # seconds to stay at each stop for demo purposes

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update the current stop based on time
        elapsed_time = time.time() - start_time
        if elapsed_time >= stop_duration:
            current_stop_index += 1
            if current_stop_index >= len(bus_stops):
                current_stop_index = 0  # Reset to the first stop
            start_time = time.time()

        # Draw the bus route
        draw_bus_route(current_stop_index)

        # Cap the frame rate
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    main()


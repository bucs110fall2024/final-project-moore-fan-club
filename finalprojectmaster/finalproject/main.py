import pygame
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 1300, 4300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Shuttle Overview")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = { #colors from https://www.rapidtables.com/web/color/RGB_Color.html
    "CS": (30, 255, 90),  #greenish lime color
    "DCL": (255, 102, 102),  #light red color
    "IU": (251, 102, 255),  #majenta color
    "MS": (0, 255, 250),  #teal color
    "OC": (255, 255, 51),  #yellow color
    "RRT": (255, 0, 127),  #darkish pink
    "UDC": (255, 128, 0),  #plain orange
    "WS": (0, 0, 255),  #regular blue
    "Map": (128, 128, 128),  #gray
    "Status": (224, 224, 224), #plain black
    "Tips": (224, 224, 224), #lighter grey
}

# Font
font = pygame.font.Font(None, 36)

# Section data (positions and labels)
sections = [
    {"label": "CS\nCampus Shuttle", "color": COLORS["CS"], "pos": (50, 50)}, #row 1 column 1

    {"label": "DCL\nDowntown Center - Leroy Shuttle", "color": COLORS["DCL"], "pos": (450, 50)}, #row 1 column 2

    {"label": "IU\nITC - UClub Shuttle", "color": COLORS["IU"], "pos": (850, 50)}, #row 1 column 3

    {"label": "MS\nMain Street Shuttle", "color": COLORS["MS"], "pos": (50, 250)}, #row 2 column 1

    {"label": "OC\nOakdale Commons Shuttle", "color": COLORS["OC"], "pos": (450, 250)}, #row 2 column 2

    {"label": "RRT\nRiviera Ridge - Town Sq Mall Shuttle", "color": COLORS["RRT"], "pos": (850, 250)}, #row 2 column 3

    {"label": "UDC\nUniversity Downtown Center Shuttle", "color": COLORS["UDC"], "pos": (50, 450)}, #row 3 column 1

    {"label": "WS\nWestside Shuttle", "color": COLORS["WS"], "pos": (450, 450)}, #row 3 column 2

    {"label": "Map\nSee locations, Track buses", "color": COLORS["Map"], "pos": (850, 450)}, #row 3 column 3

    {"label": "Status\nCheck service status", "color": COLORS["Status"], "pos": (50, 650)}, #row 4 column 1

    {"label": "Tips\nPassenger tips", "color": COLORS["Tips"], "pos": (450, 650)}, #row 4 column 2
]

# Draw a section
def draw_section(label, color, pos, size=(250, 100)):
    pygame.draw.rect(screen, color, (*pos, *size), border_radius=10)
    lines = label.split("\n")
    for i, line in enumerate(lines):
        text = font.render(line, True, BLACK)
        text_rect = text.get_rect(center=(pos[0] + size[0] // 2, pos[1] + size[1] // 2 + i * 20))
        screen.blit(text, text_rect)

# Main loop
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw background
        screen.fill(WHITE)

        # Draw all sections
        for section in sections:
            draw_section(section["label"], section["color"], section["pos"])

        # Update display
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

import pygame
import time
from src import campus_shuttle, DCL, uclub, mainstreet, oakdale_commons, rrt, udc, ws, map, status, tips

pygame.init()

#screen dimensions set to these
width, height = 1300, 4300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Shuttle Overview")

#Color constants so it will be easier to call instead of its rgb value
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

#created a list with objects of each bus label 
sections = [
    {"label": "CS\nCampus Shuttle", "color": COLORS["CS"], "pos": (50, 50), "box": campus_shuttle}, #row 1 column 1

    {"label": "DCL\nDowntown Center - Leroy Shuttle", "color": COLORS["DCL"], "pos": (450, 50), "box": DCL}, #row 1 column 2

    {"label": "IU\nITC - UClub Shuttle", "color": COLORS["IU"], "pos": (850, 50), "box": uclub}, #row 1 column 3

    {"label": "MS\nMain Street Shuttle", "color": COLORS["MS"], "pos": (50, 250), "box": mainstreet}, #row 2 column 1

    {"label": "OC\nOakdale Commons Shuttle", "color": COLORS["OC"], "pos": (450, 250), "box": oakdale_commons}, #row 2 column 2

    {"label": "RRT\nRiviera Ridge - Town Sq Mall Shuttle", "color": COLORS["RRT"], "pos": (850, 250), "box": rrt}, #row 2 column 3

    {"label": "UDC\nUniversity Downtown Center Shuttle", "color": COLORS["UDC"], "pos": (50, 450), "box": udc}, #row 3 column 1

    {"label": "WS\nWestside Shuttle", "color": COLORS["WS"], "pos": (450, 450), "box": ws}, #row 3 column 2

    {"label": "Map\nSee locations, Track buses", "color": COLORS["Map"], "pos": (850, 450), "box": map}, #row 3 column 3

    {"label": "Status\nCheck service status", "color": COLORS["Status"], "pos": (50, 650), "box": status}, #row 4 column 1

    {"label": "Tips\nPassenger tips", "color": COLORS["Tips"], "pos": (450, 650), "box": tips}, #row 4 column 2
]

# Draw a section
def draw_box(label, color, pos, size=(250, 100)):
    pygame.draw.rect(screen, color, (*pos, *size), border_radius=10)
    lines = label.split("\n")
    for i, line in enumerate(lines):
        text = font.render(line, True, BLACK)
        text_rect = text.get_rect(center=(pos[0] + size[0] // 2, pos[1] + size[1] // 2 + i * 20))
        screen.blit(text, text_rect)

def display_module(box): #added this function to have it so that if a box is clicked, it will take you to another window
    screen.fill(BLACK)
    box_name = box.__name__.split('.')[-1]  #this gets the module name -> from stacked overflow
    text = font.render(f"This is the {box_name} shuttle !", True, WHITE) #adds the text of the shuttle based on the box name
    screen.blit(text, (100, 100))
    pygame.display.flip()
    pygame.time.wait(2000)  #2000 time to wait for 2 seconds before returning to main menu -> will be adjusted

# Main loop
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN: #event listener for mouse button down
                mouse_pos = pygame.mouse.get_pos()
                for section in sections:
                    x, y = section["pos"]
                    if x <= mouse_pos[0] <= x + 250 and y <= mouse_pos[1] <= y + 100:
                        display_module(section["box"])  #this elif calls the function for the correct box when clicked on

        #main menu background color white
        screen.fill(WHITE)

        #draw all sections
        for section in sections:
            draw_box(section["label"], section["color"], section["pos"])

        #update display
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

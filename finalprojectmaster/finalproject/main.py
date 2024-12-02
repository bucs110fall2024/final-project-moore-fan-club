import pygame
#import your controller
from src.main_menu import Main_menu

def main():
    pygame.init()
    width, height = 400, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pygame Window")

    # Define the main loop
    def mainloop():
        running = True
        while running:
            # 1. Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # 2. Detect collisions and update models (placeholder for now)

            # 3. Redraw next frame
            screen.fill((0, 0, 0))  
            # Add any drawing code here

            # 4. Display next frame
            pygame.display.flip()
            pygame.time.wait(2000)

        pygame.quit()  # Quit pygame when loop ends

    # Call your mainloop
    mainloop()

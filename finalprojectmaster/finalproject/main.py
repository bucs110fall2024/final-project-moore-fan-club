import pygame
#import your controller
from src.main_menu import Main_menu

def main():
    pygame.init()
    pygame.display.set_mode()
    def mainloop(self):
        """
        docstring
        """
        while(True): #this can also be a variable instead of just True
      #1. Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

      #2. detect collisions and update models

      #3. Redraw next frame

      #4. Display next frame
    pygame.display.flip()
    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()

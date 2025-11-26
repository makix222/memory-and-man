import pygame
from game import Game


def main():
    pygame.init()

    game = Game()
    game.create_characters() # todo: move to world

    while game.running:

        game.update()
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
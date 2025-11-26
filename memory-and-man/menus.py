import pygame


class Menus:
    def __init__(self, screen):
        self.menus = {"start": Menu(screen, "start"),
                      "pause": Menu(screen, "pause")}


class Menu:
    def __init__(self, surface, name="default"):
        self.surface = surface
        self.name = name
        self.elements = [MenuElement(self.click_quit, None)]

    def click_quit(self):
        print(f'quit was clicked from menu: {self.name}')

    def draw(self):
        for each_element in self.elements:
            self.surface.blit(each_element.draw())


class MenuElement:
    def __init__(self,
                 click_func,
                 click_func_args,
                 size=(20, 20),
                 center_pos=(0, 0),
                 color=(100, 100, 100),
                 text_color=(250, 250, 250)):

        self.surface = pygame.Surface(size)
        self.func = click_func
        self.func_args = click_func_args

        self.exists = False
        self.rect = None

        self.size = size
        self.center = center_pos

        self.color = color
        self.text_color = text_color
        self.border_color = (140, 140, 140)
        self.border_color_click = (170, 170, 170)
        self.border_width = 2
        self.border_radius = 2

        self.text_size = 12
        self.font_surface = self.set_font()
        self.text_surface = self.draw_new_font("Menu Element")

        self.rect = pygame.Rect((self.center[0] - self.size[0] / 2,
                                 self.center[1] - self.size[1] / 2),
                                self.size)

        pygame.draw.rect(self.surface,
                         self.color,
                         self.rect,
                         0,
                         self.border_radius)

        pygame.draw.rect(self.surface,
                         self.border_color,
                         self.rect,
                         self.border_width,
                         self.border_radius)

    def set_font(self):
        font_str = "verdana"
        system_fonts = pygame.font.get_fonts()
        if font_str not in system_fonts:
            font_str = pygame.font.get_default_font()
        font_path = pygame.font.match_font(font_str)
        if font_path is None:
            raise SystemError(f'Unable to find {font_str} or a default font.')
        return pygame.font.Font(font_path, self.text_size)

    def draw_new_font(self, text):
        return self.font_surface.render(text,
                                        True,
                                        self.text_color,
                                        bgcolor=self.color)

    def click(self):
        self.func(self.func_args)
        pygame.draw.rect(self.surface,
                         self.border_color_click,
                         self.rect,
                         self.border_width + 2,
                         self.border_radius)

    def draw(self):
        self.surface.blit(self.text_surface)
        return self.surface

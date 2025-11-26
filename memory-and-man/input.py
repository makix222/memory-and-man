import pygame
from world import World
from events import EventHandler
from pygame.locals import *


class LocalInput:
    def __init__(self, world: World, event_handler: EventHandler):
        self.mouse = Mouse(world, event_handler)
        self.keyboard = Keyboard(world, event_handler)
        self.input_map = {"mouse": {1: "walk",
                                    2: "run"},
                          "keyboard": {"left shift": "run",
                                       "w": "forward",
                                       "a": "left",
                                       "s": "back",
                                       "d": "right",
                                       "q": "q",
                                       "e": "e",
                                       "escape": "escape",
                                       "tab": "tab", }}
        self.commands = {"walk": 0,
                         "run": 0,
                         "forward": 0,
                         "left": 0,
                         "back": 0,
                         "right": 0,
                         "q": 0,
                         "e": 0,
                         "escape": 0,
                         "tab": 0}
        self.mouse_pos = (0, 0)

    def update(self):
        # self.mouse.update()
        # self.keyboard.update()
        self.check_inputs_for_commands()

    def check_inputs_for_commands(self):
        for k, v in self.input_map["mouse"].items():
            self.commands[v] = self.mouse.state.get(k, 0)
        for k, v in self.input_map["keyboard"].items():
            self.commands[v] = self.keyboard.keys.get(k, 0)
        self.mouse_pos = self.mouse.state['pos']

    def draw(self):
        self.mouse.draw()
        self.keyboard.draw()

    def get_commands(self):
        return [k for k, v in self.commands.items() if v != 0]


class Mouse:
    def __init__(self, world: World, event_handler: EventHandler):
        self.world = world
        self.event_handler = event_handler
        self.state = {1: 0,
                      2: 0,
                      3: 0,
                      "pos": self.world.center.pos()}

        self.event_handler.register_events({pygame.MOUSEBUTTONDOWN: self._button_down,
                                            pygame.MOUSEBUTTONUP: self._button_up,
                                            pygame.MOUSEMOTION: self._motion})
        self.btn_duration = 0
        self._max_radius = 30

    #
    # def update(self):
    #     self.event_handler.handle_events(self.event_map)

    def draw(self):
        # if self.btn_duration > 1:
        pygame.draw.circle(surface=self.world.screen,
                           color=(154, 65, 123),
                           center=self.state['pos'],
                           radius=2,
                           width=1)

    def _button_down(self, event):
        self.state[event.button] = 1
        self.btn_duration += .1 * (self._max_radius - self.btn_duration)

    def _button_up(self, event):
        self.state[event.button] = 0
        self.btn_duration = 0

    def _motion(self, event):
        self.state["pos"] = event.pos


class Keyboard:
    def __init__(self, world: World, event_handler: EventHandler):
        self.world = world
        self.event_handler = event_handler
        self.keys = {}
        self.event_handler.register_events({KEYDOWN: self._keydown,
                                            pygame.KEYUP: self._keyup})
    #
    # def update(self):
    #     self.event_handler.handle_events(self.event_map)

    def draw(self):
        pass

    def _keydown(self, event):
        key_name = pygame.key.name(event.key)
        self.keys[key_name] = 1

    def _keyup(self, event):
        key_name = pygame.key.name(event.key)
        self.keys[key_name] = 0

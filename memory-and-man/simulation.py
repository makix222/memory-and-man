import pygame

class Simulation:
    def __init__(self):
        """rates are Hz"""
        self.sim_tick_rate = 120
        self.render_tick_rate = 60
        self.fps_update_rate = 1
        self.clock = pygame.time.Clock()
        self.paused = False
        self.update_list = []
        self.fps_draw_time = 0

    def add_objects_to_update(self, update_object):
        if not hasattr(update_object, "update"):
            raise ValueError(f"provided object {update_object} does not have a draw function")
        self.update_list.append(update_object)

    def tick(self):
        self.clock.tick(self.sim_tick_rate)
        if not self.paused:
            for each_entity in self.update_list:
                each_entity.update()

    def print_fps(self):
        self.fps_draw_time += self.clock.get_time()
        if self.fps_draw_time > 1000 / self.fps_update_rate :
            self.fps_draw_time = 0
            print(self.clock.get_fps())

    def pause(self):
        self.paused = True


    def unpause(self):
        self.paused = False

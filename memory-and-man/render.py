import pygame
from events import EventUser, EventHandler
from world import World

class Renderer:
    def __init__(self, world: World, event_handler: EventHandler):
        """Sets up the render pipeline. Sets fps, sets render event timer."""
        self.fps = world.sim.render_tick_rate
        render_event = event_handler.make_event(EventUser.render,
                                                EventUser.game,
                                                {})
        pygame.time.set_timer(render_event, millis=int(1000/self.fps))
        self.objects_to_draw = [world] # Must draw the world first.
        self.objects_to_draw.extend([x for x in world.characters.values()])

    def add_objets_to_draw(self, draw_object):
        if not hasattr(draw_object, "draw"):
            raise ValueError(f"provided object {draw_object} does not have a draw function")
        self.objects_to_draw.append(draw_object)

    def render_update(self):
        for each_obj in self.objects_to_draw:
            each_obj.draw()

import pygame
from enum import Enum


class EventUser(Enum):
    any = 0
    render = 1
    game = 2
    player = 3
    beast = 4


class EventHandler:
    def __init__(self):
        self.event_counts = 0
        self.custom_event_types = {}
        self.event_map = {}

    def process_event(self, event: pygame.Event):
        for event_type, event_func_list in self.event_map.items():
            if event_type == event.type:
                for event_func in event_func_list:
                    event_func(event=event)

    def register_events(self, event_map: dict):
        """functions can add an event they care about.
        When that event happens, all the functions added will run.
        """
        for k, v in event_map.items():
            if k in self.event_map.keys():
                self.event_map[k].append(v)
            else:
                self.event_map[k] = [v]

    def make_event(self,
                   producer: EventUser,
                   consumer: EventUser,
                   data: dict):
        self.event_counts += 1

        event_id = f"{producer}:{consumer}"
        event_type = self.custom_event_types.get(event_id)
        if not event_type:
            event_type = pygame.event.custom_type()
            self.custom_event_types[event_id] = event_type
            self.event_map[event_type] = []
        return pygame.event.Event(event_type, data)

    def register_custom_event(self,
                              producer: EventUser,
                              consumer: EventUser,
                              func):
        event_id = f"{producer}:{consumer}"
        event_type = self.custom_event_types.get(event_id)
        existing_event_func = self.event_map.get(event_type)
        if existing_event_func is list:
            self.event_map[event_type].append(func)
        else:
            raise AttributeError("registering a custom event that has not been created yet.")

    def add_event(self,
                  producer: EventUser,
                  consumer: EventUser,
                  data: dict):
        pygame.event.post(self.make_event(producer, consumer, data))

    def get_custom_event_type(self,
                       producer: EventUser,
                       consumer: EventUser) -> list:
        event_id = f"{producer}:{consumer}"
        event_type = self.custom_event_types.get(event_id)
        if event_type is None:
            return []
        return [x.dict for x in pygame.event.get(event_type)]

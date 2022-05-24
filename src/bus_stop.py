from os import remove
from src.person import Person


class BusStop:
    def __init__(self, name,):
        self.name = name
        self.queue_len = 0
        self.queue_for_bus = []

    def queue_length(self):
        return self.queue_len

    def add_to_queue(self, person):
        self.queue_for_bus.append(person)
        self.queue_len += 1 

    def clear(self):
        self.queue_for_bus.clear()
        self.queue_len = 0
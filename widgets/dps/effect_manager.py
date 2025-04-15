from widgets.dps.enums import *

from bisect import insort
import numpy as np


class EffectManager:
    def __init__(self, party):
        self.party = party

    def init_simulation(self):
        self.effect_queue = []

    def update_next_update(self, time):
        self.party.next_update[9] = time


    def add_effect_reserv(self, effect):
        """
        Add a reservation for the effect.
        """
        insort(self.effect_queue, effect)
        self.update_next_update(self.effect_queue[0].time)

    
    def resolve_effect_reserv(self, current_time):
        """
        Apply reserved effects.
        """

        while self.effect_queue and self.effect_queue[0].time <= current_time:
            effect = self.effect_queue.pop(0)
            effect.effect_fn()
        self.party.next_update[9] = (self.effect_queue[0].time
                                     if len(self.effect_queue) > 0 else np.inf)
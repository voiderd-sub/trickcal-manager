from dps.enums import *

from bisect import insort
import numpy as np
from collections import defaultdict
import math

class ActionManager:
    def __init__(self, party):
        self.party = party

    def init_simulation(self):
        # Priority queue for actions (sorted by time)
        self.action_queue = []
        
        # Pending effect queue for delayed effects (sorted by time)
        self.pending_effect_queue = []  # (execution_time, action)
        
        # Index for fast lookup of actions by various criteria
        self.actions_by_hero = defaultdict(list)  # hero_id -> list of actions
        self.actions_by_movement = defaultdict(list)  # movement_type -> list of actions
        self.actions_by_type = defaultdict(list)  # action_type -> list of actions

    def update_next_update(self):
        next_action_time = self.action_queue[0][0] if self.action_queue else float('inf')
        next_effect_time = self.pending_effect_queue[0][0] if self.pending_effect_queue else float('inf')
        next_time = min(next_action_time, next_effect_time)
        self.party.next_update[9] = next_time if next_time == float('inf') else round(next_time)

    def add_action_reserv(self, time, action, on_complete_callback=None):
        """
        Add a reservation for the action.
        Also index the action for fast lookup.
        """
        action_tuple = (round(time), action, on_complete_callback)
        insort(self.action_queue, action_tuple, key=lambda x: x[0])
        self.update_next_update()
        
        self.actions_by_hero[action.hero.party_idx].append(action_tuple)
        if action.source_movement:
            self.actions_by_movement[action.source_movement].append(action_tuple)
        self.actions_by_type[action.action_type].append(action_tuple)

    def add_pending_effect(self, base_time, action, delay=0):
        """
        Add a pending effect to the queue.
        The effect will be executed at base_time + delay.
        """
        execution_time = round(base_time + delay * SEC_TO_MS)
        insort(self.pending_effect_queue, (execution_time, action))
        self.update_next_update()

    def resolve_all_actions(self, current_time):
        """
        Resolve all actions in the action queue and pending effect queue.
        """
        while self.action_queue and self.action_queue[0][0] <= current_time:
            time, action, callback = self.action_queue.pop(0)
            action_tuple = (time, action, callback)
            self._remove_from_indices(action_tuple)
            action.action_fn(time)
            if callback:
                callback()
        while self.pending_effect_queue and self.pending_effect_queue[0][0] <= current_time:
            execution_time, action = self.pending_effect_queue.pop(0)
            action.action_fn(execution_time)
        self.update_next_update()
    
    def _remove_from_indices(self, action_tuple):
        _, action, _ = action_tuple
        self.actions_by_hero[action.hero.party_idx].remove(action_tuple)
        if action.source_movement:
            self.actions_by_movement[action.source_movement].remove(action_tuple)
        self.actions_by_type[action.action_type].remove(action_tuple)
    
    def get_actions_by_hero(self, hero_id):
        """Get all actions for a specific hero"""
        return self.actions_by_hero[hero_id]
    
    def get_actions_by_movement(self, movement_type):
        """Get all actions of a specific movement type"""
        return self.actions_by_movement[movement_type]
    
    def get_actions_by_type(self, action_type):
        """Get all actions of a specific action type"""
        return self.actions_by_type[action_type]
    
    def get_pending_actions_count(self, hero_id=None, movement_type=None, action_type=None):
        """Get count of pending actions with optional filters"""
        if hero_id is not None:
            return len(self.actions_by_hero[hero_id])
        elif movement_type is not None:
            return len(self.actions_by_movement[movement_type])
        elif action_type is not None:
            return len(self.actions_by_type[action_type])
        else:
            return len(self.action_queue)
    
    def cancel_actions_by_hero(self, hero_id):
        """Cancel all pending actions for a specific hero"""
        hero_actions = self.actions_by_hero[hero_id]
        for action_tuple in hero_actions[:]:
            if action_tuple in self.action_queue:
                self.action_queue.remove(action_tuple)
                self._remove_from_indices(action_tuple)
    
    def cancel_actions_by_movement(self, movement_type):
        """Cancel all pending actions of a specific movement type"""
        movement_actions = self.actions_by_movement[movement_type]
        for action_tuple in movement_actions[:]:
            if action_tuple in self.action_queue:
                self.action_queue.remove(action_tuple)
                self._remove_from_indices(action_tuple)
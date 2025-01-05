from widgets.dps.enums import *
import heapq

class BuffManager:
    def __init__(self, party):
        self.party = party
        self.buff_heap = []
        self.debuff_heap = []
        self.active_buffs = dict()
        self.active_debuffs = {debuff_name: 0 for debuff_name in DebuffType}

    def add_buff(self, buff):
        buff_id = f"{buff['content']['type']}_{buff['content']['targets']}"
        stacking_mode = buff.get("stacking_mode", "separate")

        if stacking_mode == "refresh" and buff_id in self.active_buffs:
            existing_buff = self.active_buffs[buff_id]
            self.buff_heap.remove(Buff(existing_buff.time, -1, existing_buff.content, buff_id))
            heapq.heapify(self.buff_heap)

            new_buff_end = Buff(buff["end_time"], -1, existing_buff.content, buff_id, stacking_mode)
            heapq.heappush(self.buff_heap, new_buff_end)

            existing_buff.time = buff["end_time"]
            self.active_buffs[buff_id] = existing_buff

        else:
            new_buff_start = Buff(buff["start_time"], 1, buff["content"], buff_id, stacking_mode)
            new_buff_end = Buff(buff["end_time"], -1, buff["content"], buff_id, stacking_mode)
            heapq.heappush(self.buff_heap, new_buff_start)
            heapq.heappush(self.buff_heap, new_buff_end)

            self.active_buffs[buff_id] = new_buff_start

        self.party.next_update[-1] = self.buff_heap[0].time
    

    def add_debuff(self, time, duration, debuff_name):
        new_debuff_end = int(time + duration * MS_IN_SEC)
        heapq.heappush(self.debuff_heap, (new_debuff_end, debuff_name))
        self.active_debuffs[debuff_name] += 1


    def apply_buffs(self, t):
        while self.buff_heap and self.buff_heap[0].time == t:
            buff_data = heapq.heappop(self.buff_heap)
            event_type, buff = buff_data.apply_or_remove, buff_data.content
            buff_id = buff_data.buff_id

            if event_type == -1:
                if buff_id in self.active_buffs and self.active_buffs[buff_id].time == t:
                    del self.active_buffs[buff_id]

            for i in range(9):
                if buff["targets"] & (1 << i):
                    character = self.party.character_list[i]
                    if character:
                        self.apply_buff_effect(character, buff["type"], buff["value"] * event_type)

        while self.debuff_heap and self.debuff_heap[0][0] == t:
            _, debuff_name = heapq.heappop(self.debuff_heap)
            self.active_debuffs[debuff_name] -= 1


    def apply_buff_effect(self, target, buff_type, buff_value):
        if buff_type == BuffType.AttackSpeedAdd:
            self.update_as(target, buff_value)

    def update_as(self, target, value):
        target.attack_speed_coeff += value
        # target.aa_cd = int(300 * MS_IN_SEC / (target.attack_speed * target.attack_speed_coeff))


class Buff:
    def __init__(self, start_time, duration, content, buff_id, stacking_mode="refresh"):
        self.start_time = start_time
        self.duration = duration
        self.content = content      # [fn, target, duration]
        self.buff_id = buff_id
        self.stacking_mode = stacking_mode  # "separate" or "refresh"

    def __lt__(self, other):
        return self.start_time < other.start_time

    def apply(self):
        for fn, target in self.content:
            fn(target, "apply")
    
    def remove(self):
        for fn, target in self.content:
            fn(target, "remove")
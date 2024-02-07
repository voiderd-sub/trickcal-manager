from collections import defaultdict


class ResourceManager:
    def __init__(self, main):
        self.main = main
        self._resourceMaster = dict()
        self._resourceUser = dict()

        self.masterInit()

    def userGet(self, resource_name):
        if resource_name in self._resourceUser:
            return self._resourceUser[resource_name]
        else:
            return getattr(self, f"get{resource_name}")()

    def masterGet(self, resource_name):
        return self._resourceMaster[resource_name]

    def delete(self, resource_name):
        if resource_name in self._resourceUser:
            del self._resourceUser[resource_name]
        elif resource_name in self._resourceMaster:
            del self._resourceMaster[resource_name]
    
    def deleteAll(self, user=False, master=False):
        if user:
            self._resourceUser.clear()
        if master:
            self._resourceMaster.clear()

    
    def getHeroIdToStarExtrinsic(self):
        cur_user = self.main.conn_user.cursor()
        cur_user.execute("SELECT hero_id, star_extrinsic FROM user_hero")
        star_extrinsic = {idx: star for (idx, star) in cur_user}
        self._resourceUser["HeroIdToStarExtrinsic"] = star_extrinsic
        return star_extrinsic
        

    def getCurEquip(self):
        user_equip = dict()

        cur_master = self.main.conn_master.cursor()
        cur_master.execute("SELECT max(_rowid_) FROM hero")
        max_hero_id = cur_master.fetchone()[0]

        cur_user = self.main.conn_user.cursor()
        cur_user.execute("SELECT * FROM user_cur_equip")
        for (idx, rank, equips) in cur_user:
            user_equip[idx] = (rank, set((int(i) for i in equips.split(",")))
                                if equips is not None else set())
        
        for i in range(1, max_hero_id+1):
            if i not in user_equip:
                user_equip[i] = (1, set())
        
        self._resourceUser["user_equip"] = user_equip
        return user_equip
    

    def getGoalList(self):
        cur_user = self.main.conn_user.cursor()
        cur_user.execute("SELECT name FROM user_goal_equip_names order by id asc;")
        goal_list = [name for (name,) in cur_user]
        self._resourceUser["goal_list"] = goal_list
        return goal_list
    

    def masterInit(self):
        cur = self.main.conn_master.cursor()

        # MaxRank
        cur.execute("SELECT MAX(rank) FROM equipment")
        max_rank = cur.fetchone()[0]
        self._resourceMaster["MaxRank"] = max_rank

        # HeroNameToId, HeroIdToMetadata
        hero_name_to_id = dict()
        hero_id_to_metadata = dict()
        meta_names = ["name_kr", "name_en", "star_in", "attack_type", "pos", "class", "personality", "race"]
        cur.execute("SELECT * FROM hero") # idx, name_kr, name_en, star_in, attack_type, pos, class, personality, race
        for data in cur:
            idx = data[0]
            hero_name_to_id[data[1]] = idx
            hero_id_to_metadata[idx] = dict()
            for meta_name, meta_val in zip(meta_names, data[1:]):
                hero_id_to_metadata[idx][meta_name] = meta_val

        self._resourceMaster["HeroNameToId"] = hero_name_to_id
        self._resourceMaster["HeroIdToMetadata"] = hero_id_to_metadata


        # HeroIdToEquipNames, HeroIdToEquipIds, HeroNameToEquipNames
        hero_id_to_equip_names = defaultdict(lambda: defaultdict(list))
        hero_id_to_equip_ids = defaultdict(lambda: defaultdict(list))
        hero_name_to_equip_names = defaultdict(lambda: defaultdict(list))
        cur.execute("""SELECT h.id, h.name_kr, he.rank, e.id, e.name
                        FROM hero h
                        JOIN hero_equip he ON (h.id = he.hero_id)
                        JOIN equipment e ON (he.equipment_id = e.id)""")
        for (hero_id, hero_name_kr, rank, equip_id, equip_name) in cur:
            hero_id_to_equip_names[hero_id][rank].append(equip_name)
            hero_id_to_equip_ids[hero_id][rank].append(equip_id)
            hero_name_to_equip_names[hero_name_kr][rank].append(equip_name)
        self._resourceMaster["HeroIdToEquipNames"] = hero_id_to_equip_names
        self._resourceMaster["HeroIdToEquipIds"] = hero_id_to_equip_ids
        self._resourceMaster["HeroNameToEquipNames"] = hero_name_to_equip_names
        
        # HeroDefaultOrder
        hero_default_order = list()
        cur.execute("SELECT id FROM hero ORDER BY personality ASC, star_intrinsic DESC, name_kr ASC")
        for (idx,) in cur:
            hero_default_order.append(idx)
        self._resourceMaster["HeroDefaultOrder"] = hero_default_order
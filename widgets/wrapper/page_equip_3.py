from widgets.ui.page_equip_3 import Ui_page_equip_3
from widgets.wrapper.equip_dialog import EquipDialog
from widgets.wrapper.resource_manager import ResourceManager

from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtGui import QIntValidator
from PySide6.QtGui import QValidator

import sqlite3
import pandas as pd
import numpy as np
import pulp
from collections import defaultdict
from copy import deepcopy



class PageEquip3(Ui_page_equip_3, QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        self.setupUi(self)
        self.setInitialState()

    def setInitialState(self):
        self.reload = {"account": True}
        self.setting_name_list = ["auto_update_yes", "use_equip_yes", "hallow_13_yes",
                                  "research_level","candy_buying", "use_standard_yes",
                                  "daily_elleaf_yes", "lecture_level", "cur_standard",
                                  "daily_candy_yes", "auto_update_yes", "round_yes"]

        self.research_level.setValidator(QIntValidator(0, 10, self.research_level))
        self.candy_buying.setValidator(QIntValidator(0, 10, self.candy_buying))
        
        max_lecture_level = self.window().resource.masterGet("MaxLectureLevel")
        self.lecture_level.setValidator(QIntValidator(0, max_lecture_level, self.lecture_level))
        self.lecture_level.setPlaceholderText(f"0 ~ {max_lecture_level}")
        
        self.cur_standard.setValidator(QIntValidator(0, 999999, self.cur_standard))

        self.update_btn.clicked.connect(self.window().updateDropTable)
        self.calc_btn.clicked.connect(self.calculate)

        self.dialog = EquipDialog()


    def loadUserData(self):
        self.updateGoalList()
        self.loadCalcSettings()


    def loadCalcSettings(self):
        calc_settings = self.window().resource.userGet("CalcSettings")
        for setting_name in self.setting_name_list:
            if setting_name not in calc_settings:
                # Initialize default value
                if len(setting_name.split("_yes"))==2:
                    value = 0 if setting_name.split("_yes")[0] == "auto_update" else 1
                else:
                    value = ""
            else:
                value = calc_settings[setting_name]
            widget = getattr(self, setting_name)
            if len(setting_name.split("_yes"))==2:
                if value:
                    widget.setChecked(True)
                else:
                    getattr(self, setting_name.split("_yes")[0]+"_no").setChecked(True)
            else:
                widget.setText(str(value))


    def updateGoalList(self):
        res = self.window().resource
        goal_list = list(name for (name, type) in self.window().resource.userGet("GoalIdToName").values())

        self.goal_list.clear()
        self.goal_list.addItems(goal_list)
        self.goal_list.setCurrentIndex(0)
    

    def updateDropTable(self):
        main_window = self.window()
        path_item_table = main_window.config["path_item_table"]
        url=f'https://docs.google.com/spreadsheet/ccc?key={path_item_table}&output=xlsx'

        # make dict of drop item list
        drop_item_list = dict()
        self.stage_to_drop = dict()
        df = pd.read_excel(url, sheet_name="아이템 이름", usecols="A,E:F")
        df = df.replace({np.nan: None})
        for (_, row) in df.iterrows():
            stage_name, item_1, item_2 = row
            drop_item_list[stage_name] = (item_1, item_2)

        df = pd.read_excel(url, sheet_name="드랍률", header=2, usecols="A:B,K:L")
        for (_, row) in df.iterrows():
            stage_name, count, prob_1, prob_2 = row
            if count < 100:
                continue
            prob_1 = None if type(prob_1)==str else prob_1
            prob_2 = None if type(prob_2)==str else prob_2
            item_1, item_2 = drop_item_list[stage_name]
            self.stage_to_drop[stage_name] = dict()
            self.stage_to_drop[stage_name][item_1] = prob_1
            self.stage_to_drop[stage_name][item_2] = prob_2
            self.stage_to_drop[stage_name].pop(None, None)

        data = []
        for stage_name, item_dict in self.stage_to_drop.items():
            item_1, item_2 = drop_item_list[stage_name]
            data.append((stage_name, item_1, item_dict.get(item_1, None), item_2, item_dict.get(item_2, None)))

        cur_master: sqlite3.Cursor = main_window.conn_master.cursor()
        cur_master.executemany("""INSERT OR REPLACE INTO
                           drop_table(area, item_1_name, item_1_drop_rate, item_2_name, item_2_drop_rate)
                           VALUES (?, ?, ?, ?, ?)""", data)
        main_window.conn_master.commit()


    # function to remove unusual stages
    def remove_dominated_stages(self, stage_to_drop):
        stage_keys = list(stage_to_drop.keys())
        keys_to_remove = set()

        for i in range(len(stage_keys)):
            if stage_keys[i] in keys_to_remove:
                continue
            for j in range(i + 1, len(stage_keys)):
                if stage_keys[j] in keys_to_remove:
                    continue

                A = stage_keys[i]
                B = stage_keys[j]

                if self.is_A_dominates_B(stage_to_drop[A], stage_to_drop[B], A, B):
                    keys_to_remove.add(B)
                elif self.is_A_dominates_B(stage_to_drop[B], stage_to_drop[A], B, A):
                    keys_to_remove.add(A)

        for key in keys_to_remove:
            del stage_to_drop[key]

    def is_A_dominates_B(self, dict_A, dict_B, key_A, key_B):
        if not set(dict_B.keys()).issubset(set(dict_A.keys())):
            return False
        
        for k in dict_B.keys():
            if dict_A[k] < dict_B[k]:
                return False
        
        if dict_A == dict_B:
            a1, a2 = map(int, key_A.split("-"))
            b1, b2 = map(int, key_B.split("-"))
            if a1 == b1:
                return a2 > b2
            else:
                return a1 > b1
        
        return True


    def calculate(self):
        try:
            self.saveCurrentSettings()
        except:
            QMessageBox.critical(self, "Error", "입력값이 범위에 맞는지 확인해주세요.")
            return
        
        main = self.window()
        res: ResourceManager = main.resource

        if self.auto_update_yes.isChecked():
            main.updateDropTable()
        stage_to_drop = deepcopy(res.masterGet("StageToDrop"))
        if self.round_yes.isChecked():
            for _, item_dict in stage_to_drop.items():
                for item_name, drop_rate in item_dict.items():
                    item_dict[item_name] = round(drop_rate * 2, 1) / 2

        self.remove_dominated_stages(stage_to_drop)

        # Calculate needs
        hero_id_to_equip_ids = res.masterGet("HeroIdToEquipIds")
        recipe = res.masterGet("Recipe")
        rank_to_standard = res.masterGet("RankToStandard")
        needs_each_equip = defaultdict(int)
        needs_each_type = defaultdict(lambda: defaultdict(int))
        needs_each_item = defaultdict(int)

        goal_id = self.goal_list.currentIndex() + 1
        goal_equip = res.userGet("GoalEquip")[goal_id]
        cur_equip = res.userGet("CurEquip")

        for hero_id, (goal_rank, goal_equips) in goal_equip.items():
            cur_rank, cur_equips = cur_equip.get(hero_id, (1, set()))
            for item_rank in range(cur_rank, goal_rank+1):
                goal_equips_this_rank = goal_equips if item_rank == goal_rank else set(range(1,7))
                cur_equips_this_rank = cur_equips if item_rank == cur_rank else set()
                for order_idx in list(goal_equips_this_rank - cur_equips_this_rank):
                    equip_id = hero_id_to_equip_ids[hero_id][item_rank][order_idx - 1]
                    needs_each_equip[equip_id] += 1

        if self.use_equip_yes.isChecked():
            bag_equips = res.userGet("BagEquips")
            for equip_id, count in bag_equips.items():
                needs_each_equip[equip_id] -= count
        
        for equip_id in list(needs_each_equip.keys()):
            if needs_each_equip[equip_id] <= 0:
                needs_each_equip.pop(equip_id)

        equip_id_to_rank_and_type = res.masterGet("EquipIdToRankAndType")

        for equip_id, count in needs_each_equip.items():
            item_rank, type_id = equip_id_to_rank_and_type[equip_id]
            needs_each_type[item_rank][type_id] += count
        for item_rank in needs_each_type:
            for type_id, count in needs_each_type[item_rank].items():
                for item_name, item_count in recipe[(item_rank, type_id)].items():
                    needs_each_item[item_name] += item_count * count

        user_items = res.userGet("UserItems")
        for name, count in user_items.items():
            needs_each_item[name] -= count
        for name in list(needs_each_item.keys()):
            if needs_each_item[name] <= 0:
                needs_each_item.pop(name)

        # Candy settings
        hallow_level = 2 if self.hallow_13_yes.isChecked() else 1
        research_level = self.research_level.text()
        research_level = 0 if research_level == "" else int(research_level)
        candy_buying = self.candy_buying.text()
        candy_buying = 0 if candy_buying == "" else int(candy_buying)
        daily_candy = 1600 / 14 if self.daily_candy_yes.isChecked() else 0

        # Standard settings
        lecture_level = self.lecture_level.text()
        lecture_level = 0 if lecture_level == "" else int(lecture_level)
        cur_standard = self.cur_standard.text()
        cur_standard = 0 if cur_standard == "" else int(cur_standard)
        num_lecture = 3 if self.daily_elleaf_yes.isChecked() else 2
        use_standard = self.use_standard_yes.isChecked()
        
        candy_per_day = 200 + 24 * (10 + 6 * hallow_level * (1 + 0.1 * research_level)) \
                        + 100 * candy_buying + daily_candy
        standard_per_day = 0 if lecture_level == 0 else num_lecture * (lecture_level + 29)

        # Set LpProblem
        model = pulp.LpProblem('test_lp', pulp.LpMinimize)
        x = pulp.LpVariable.dicts('면제 횟수', stage_to_drop, lowBound=0)
        if use_standard:
            y = pulp.LpVariable.dicts('정석 개수', needs_each_item, lowBound=0)
        
        constraints = dict()
        for item_name, count in needs_each_item.items():
            exp = pulp.LpAffineExpression()
            for stage_name, prob_dict in stage_to_drop.items():
                if item_name in prob_dict:
                    exp += prob_dict[item_name] * x[stage_name]
            if use_standard:
                item_rank = int(item_name.split("(")[1].rstrip("티어)"))
                exp += (1 / rank_to_standard[item_rank]) * y[item_name]
            constraints[item_name] = exp
            model += exp >= needs_each_item[item_name]
        candy_days = pulp.LpVariable('왕사탕', lowBound=0)
        if use_standard:
            standard_days = pulp.LpVariable('정석', lowBound=0)
        
        model += candy_days * candy_per_day >= pulp.lpSum([10 * v  for _,v in x.items()])
        if use_standard:
            model += standard_days * standard_per_day + cur_standard >= pulp.lpSum([y[name] for name in needs_each_item.keys()])
        
        if use_standard:
            tmp_bin = pulp.LpVariable('binary', cat="Binary")
            M = 100_000
            days = pulp.LpVariable('days', lowBound=0)

            # Constraint for binary
            model += candy_days - standard_days <= M * tmp_bin
            model += standard_days - candy_days <= M * (1-tmp_bin)

            # Constraint for min_x = min(x1, x2)
            model += days >= candy_days
            model += days >= standard_days
            model += days <= candy_days + M * (1-tmp_bin)
            model += days <= standard_days + M * tmp_bin

        else:
            days = pulp.LpVariable('days', lowBound=0)
            model += days == candy_days

        # objective function : max(candy_days, standard_days)
        model += days
        model.solve(pulp.apis.PULP_CBC_CMD(msg=False))

        if model.status != 1:
            QMessageBox.critical(self, "Error", "해가 존재하지 않습니다.")
            return

        # print result
        result = []
        partial_res=f"""소요 시간 : {pulp.value(model.objective):.2f}일
사용한 왕사탕 개수 : {pulp.value(candy_days * candy_per_day):.0f}개
"""
        if use_standard:
            partial_res+=f"사용한 정석 개수 : {pulp.value(pulp.lpSum([y[name] for name in needs_each_item.keys()])):.0f}개\n"
        partial_res+="\n[남는 재료 개수]\n"

        for k, v in constraints.items():
            val = pulp.value(v)
            if val >= needs_each_item[k] + 1:
                partial_res+=f"{k} - {val - needs_each_item[k]:.0f}개 남음\n"

        no_data_cnt = needs_each_type[0][0]
        if no_data_cnt != 0:
            partial_res+="\n"+"="*30+"\n"
            partial_res+=f"데이터 없음 : {no_data_cnt}개\n"
            partial_res+="DB에 사도 착용 장비 정보가 없는 경우, 계산에서 제외됩니다.\n"

        result.append(partial_res)

        partial_res = ""
        for k, v in x.items():
            val = pulp.value(v)
            if val != 0:
                partial_res+=(f"{k} : {val:.0f}회 면제\n")
        result.append(partial_res)

        partial_res = ""
        for k in sorted(needs_each_item.keys(), key=lambda x: self.material_name_to_id(x)):
            if not k in constraints:
                continue
            v = constraints[k]
            expval = pulp.value(v)
            partial_res+=f"[{k}]: 총 {expval:.0f}개 파밍"
            if expval >= needs_each_item[k] + 1:
                partial_res += f" ({expval - needs_each_item[k]:.0f}개 남음)\n"
            else:
                partial_res += "\n"
            tmp_res = []
            for a in v:
                val = a.varValue
                if val != 0:
                    name = a.name
                    if len(name.split('면제_횟수_')) > 1:
                        stage = True
                        name = name.split('면제_횟수_')[-1].replace("_", "-")
                    else:
                        stage = False

                    if stage:
                        num_item = val* stage_to_drop[name][k]
                        percent = val * stage_to_drop[name][k]/expval * 100
                        tmp_res.append((name, f"{num_item:.0f}개", percent))
                    else:
                        rank = int(k.split("(")[1].rstrip("티어)"))
                        num_item = val / rank_to_standard[rank]
                        percent = num_item / expval * 100
                        tmp_res.append(("정석", f"재료 {num_item:.0f}개 대체, 정석 {val:.0f}개 사용", percent))
            tmp_res.sort(key=lambda x: x[-1], reverse=True)
            for name, val, percent in tmp_res:
                partial_res+=f"{name} : {val} ({percent:.0f}%)\n"
            partial_res+="\n"
        result.append(partial_res)

        partial_res = ""
        if use_standard:
            for k, v in y.items():
                val = pulp.value(v)
                if val != 0:
                    partial_res+=f"{k} : 정석 {val:.0f}개 사용\n"
        result.append(partial_res)

        self.dialog.tabWidget.setCurrentIndex(0)
        self.dialog.show()
        self.dialog.setResultValues(result)



    def saveCurrentSettings(self):
        main = self.window()
        res = main.resource
        calc_settings = res.userGet("CalcSettings")
        calc_settings.clear()

        for setting_name in self.setting_name_list:
            widget = getattr(self, setting_name)
            if len(setting_name.split("_yes"))==2:
                value = int(widget.isChecked())
            else:
                text = widget.text()
                if text == "":
                    text = "0"
                criteria = widget.validator().validate(text, 0)[0]
                if criteria != QValidator.State.Acceptable:
                    raise Exception
                value = int(text)
            calc_settings[setting_name] = value
    

    def material_name_to_id(self, name):
        name = name.split("(")
        rank = int(name[1].rstrip("티어)"))

        name_w_o_rank = name[0].split(" ")
        prefix = " ".join(name_w_o_rank[:-1])
        suffix = name_w_o_rank[-1]

        prefix = self.window().type_name_to_type_id[prefix]
        suffix = self.window().pr_to_id[suffix]
        
        return (-rank, prefix, suffix)
    

    def reloadPage(self):
        if not any(self.reload.values()):
            return
        
        if self.reload.get("account", False):
            self.loadUserData()

        elif self.reload.get("goal", False):
            self.updateGoalList()
        
        self.reload = dict()
    

    def savePageData(self):
        self.saveCurrentSettings()
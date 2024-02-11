from PySide6.QtCore import QRunnable, Slot, Signal, QObject
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel

import sqlite3, sys
import pandas as pd



# def updateDropTable(main):
#     path_item_table = main.config["path_item_table"]
#     url=f'https://docs.google.com/spreadsheet/ccc?key={path_item_table}&output=xlsx'

#     # make dict of drop item list
#     drop_item_list = dict()
#     self.stage_to_prob = dict()
#     df = pd.read_excel(url, sheet_name="아이템 이름", usecols="A,E:F")
#     df = df.replace({np.nan: None})
#     for (_, row) in df.iterrows():
#         stage_name, item_1, item_2 = row
#         drop_item_list[stage_name] = (item_1, item_2)

#     df = pd.read_excel(url, sheet_name="드랍률", header=2, usecols="A:B,K:L")
#     for (_, row) in df.iterrows():
#         stage_name, count, prob_1, prob_2 = row
#         if count < 100:
#             continue
#         prob_1 = None if type(prob_1)==str else prob_1
#         prob_2 = None if type(prob_2)==str else prob_2
#         item_1, item_2 = drop_item_list[stage_name]
#         self.stage_to_prob[stage_name] = dict()
#         self.stage_to_prob[stage_name][item_1] = prob_1
#         self.stage_to_prob[stage_name][item_2] = prob_2
#         self.stage_to_prob[stage_name].pop(None, None)

#     data = []
#     for stage_name, item_dict in self.stage_to_prob.items():
#         item_1, item_2 = drop_item_list[stage_name]
#         data.append((stage_name, item_1, item_dict.get(item_1, None), item_2, item_dict.get(item_2, None)))

#     cur_master: sqlite3.Cursor = main.conn_master.cursor()
#     cur_master.executemany("""INSERT OR REPLACE INTO
#                         drop_table(area, item_1_name, item_1_drop_rate, item_2_name, item_2_drop_rate)
#                         VALUES (?, ?, ?, ?, ?)""", data)
#     main.conn_master.commit()


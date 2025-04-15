from widgets.ui.dps_graph_window import Ui_DpsGraphWindow
from widgets.dps.enums import DMG_TYPE_LABELS_KR

from PySide6.QtWidgets import QMainWindow, QVBoxLayout
from PySide6.QtCore import Qt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import matplotlib

import numpy as np
import pandas as pd


class DpsGraphWindow(Ui_DpsGraphWindow, QMainWindow):
    def __init__(self, main_window):
        super(DpsGraphWindow, self).__init__()
        matplotlib.rcParams['font.family'] = 'ONE Mobile POP'  # font setting
        matplotlib.rcParams['axes.unicode_minus'] = False      # prevent breaking minus signs
        self.setupUi(self)
        self.setWindowTitle("시뮬레이션 결과")
        self.window = lambda: main_window
        self.setInitialState()
        self.hide()
        
    

    def setInitialState(self):
        # self.reload = {"master": True}
        # Since the 1st tab is always activated when showing this window, idx 0 is not used.
        self.tab_initialized = {i:False for i in range(self.tabWidget.count())}
        self.tab_initialized[0] = True
        
        self.summary_figure = Figure()
        self.summary_canvas = FigureCanvas(self.summary_figure)
        self.summary_canvas_container.layout().addWidget(self.summary_canvas)

        self.analysis_figure = Figure()
        self.analysis_canvas = FigureCanvas(self.analysis_figure)
        self.analysis_canvas_container.layout().addWidget(self.analysis_canvas)

        self.tabWidget.currentChanged.connect(self.lazyInitialize)
        self.hero_name_combobox.currentIndexChanged.connect(self.drawAnalysis)
    

    def lazyInitialize(self):
        tab_idx = self.tabWidget.currentIndex()
        if not self.tab_initialized[tab_idx]:
            match tab_idx:
                case 1:
                    self.hero_name_combobox.setCurrentIndex(0)
                case 2:
                    pass    # fill table
                case 3:
                    pass    # load/save and compare builds
                case _:
                    raise ValueError("Invalid tab index")


    def showGraph(self, df: pd.DataFrame):
        # df : {name : {dmg_type : [val]}}
        res = self.window().resource
        self.df = df

        # initialize hero list
        names = df["name"].unique().tolist()
        self.hero_name_combobox.clear()
        self.hero_name_combobox.addItems(names)

        # draw summary figure
        self.tabWidget.setCurrentIndex(0)
        self.drawSummary()

        # show window to the top
        flags = self.windowFlags()
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        self.show()
        self.raise_()
        self.activateWindow()

        self.setWindowFlags(flags)
        self.show()

    
    def drawSummary(self):
        df = self.df

        df_total = df[df["dmg_type"] == "Total"]

        summary = df_total.groupby("name")["dmg"].agg(
            mean="mean",
            p10=lambda x: np.percentile(x, 10),
            p90=lambda x: np.percentile(x, 90)
        ).reset_index()
        summary["upper_err"] = np.maximum(summary["p90"] - summary["mean"], 0)
        summary["lower_err"] = np.maximum(summary["mean"] - summary["p10"], 0)
        summary = summary.sort_values("mean", ascending=False)

        self.summary_figure.clear()
        ax = self.summary_figure.add_subplot(111)
        yerr = np.array([
            summary["lower_err"].to_numpy(),
            summary["upper_err"].to_numpy()
        ])

        ax.bar(
            summary["name"],
            summary["mean"],
            yerr=yerr,
            capsize=5
        )
        ax.set_title("캐릭터별 평균 Total 대미지 (상/하위 10%)")
        ax.set_ylabel("평균 대미지")
        ax.set_xticks(range(len(summary["name"])))
        ax.set_xticklabels(summary["name"])

        self.summary_canvas.draw()

        df_total = df_total.reset_index(drop=True)
        character_order = df_total["name"].unique()
        num_characters = len(character_order)
        df_total["run_id"] = df_total.index // num_characters
        run_sums = df_total.groupby("run_id")["dmg"].sum()
        self.mean_val.setText(f"{int(run_sums.mean()):,}")
        self.p90_val.setText(f"{int(np.percentile(run_sums, 90)):,}")
        self.p10_val.setText(f"{int(np.percentile(run_sums, 10)):,}")

    

    def drawAnalysis(self):
        df = self.df
        name = self.hero_name_combobox.currentText()

        analysis = df[(df["name"] == name) & (df["dmg_type"] != "Total")]
        analysis = analysis.groupby("dmg_type")["dmg"].agg(
            mean="mean",
            p10=lambda x: np.percentile(x, 10),
            p90=lambda x: np.percentile(x, 90)
        ).reset_index()

        analysis["upper_err"] = np.maximum(analysis["p90"] - analysis["mean"], 0)
        analysis["lower_err"] = np.maximum(analysis["mean"] - analysis["p10"], 0)
        analysis = analysis.sort_values("mean", ascending=False)

        analysis["label"] = analysis["dmg_type"].map(DMG_TYPE_LABELS_KR).fillna(analysis["dmg_type"])

        self.analysis_figure.clear()
        ax = self.analysis_figure.add_subplot(111)
        yerr = np.array([
            analysis["lower_err"].to_numpy(),
            analysis["upper_err"].to_numpy()
        ])

        ax.bar(
            analysis["label"],
            analysis["mean"],
            yerr=yerr,
            capsize=5
        )
        ax.set_title("캐릭터별 평균 Total 대미지 (상/하위 10%)")
        ax.set_ylabel("평균 대미지")
        ax.set_xticks(range(len(analysis["label"])))
        ax.set_xticklabels(analysis["label"])

        self.analysis_canvas.draw()
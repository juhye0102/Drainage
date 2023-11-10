# -*- coding: utf-8 -*-

from importlib import util
import os
from qgis.PyQt import uic, QtWidgets, QtGui
from qgis.PyQt.QtCore import pyqtSignal

# import Qtree
from .Watershed_dialog import WatershedDialog
from .Batch_Processor_dialog import BatchProcessor

# from SetupGRM_dialog import SetupGRMDialog

FORM_CLASS, _ = uic.loadUiType(
    os.path.join(os.path.dirname(__file__), "Drainage_dockwidget_base.ui")
)


# 아이콘 경로들 임 추후에 변경 할것임
path = os.path.dirname(os.path.realpath(__file__))
Drainage_icon = path + "\\image\\internet.png"
Cube = path + "\\image\\cube.png"
_util = util()


class DrainageDockWidget(QtWidgets.QDockWidget, FORM_CLASS):
    closing_plugin = pyqtSignal()

    def __init__(self, parent=None, iface=None):
        """Constructor."""
        super(DrainageDockWidget, self).__init__(parent)
        self.iface = iface
        self.setupUi(self)
        # 트리 위젯에 메뉴 항목을 넣는 부분임
        self.initUI()

    def init_ui(self):
        self.setWindowTitle("Drainage")
        # 배경 색상 회색
        # self.treeWidget.setStyleSheet("background-color: gray;")
        self.treeWidget.setItemsExpandable(True)
        self.treeWidget.setAnimated(True)
        self.treeWidget.setItemsExpandable(True)
        self.treeWidget.setColumnCount(1)
        self.treeWidget.setHeaderLabels([""])

        # Qtree 박스에 헤더 부분 제거
        self.treeWidget.setHeaderHidden(True)
        result = _util.CheckTaudem()
        if result is False:
            _util.messagebox_show_error("Drainage", "Taudem is not installed.")
        item10 = QtWidgets.QTreeWidgetItem(self.treeWidget, ["Drainage"])
        item16 = QtWidgets.QTreeWidgetItem(item10, ["Batch Processor"])
        icon = QtGui.QIcon(Cube)
        item16.setIcon(0, icon)
        item17 = QtWidgets.QTreeWidgetItem(
            item10, ["Create OutletPoint Layer and Draw OutletPoint"]
        )
        icon = QtGui.QIcon(Cube)
        item17.setIcon(0, icon)
        item18 = QtWidgets.QTreeWidgetItem(item10, ["Watershed"])
        icon = QtGui.QIcon(Cube)
        item18.setIcon(0, icon)

        self.treeWidget.expandAll()

        self.mainLayout = QtWidgets.QGridLayout(self)
        self.mainLayout.addWidget(self.treeWidget)
        # 더블 클릭 했을대 메뉴 명칭 확인
        self.treeWidget.itemDoubleClicked.connect(self.onDoubleClick)

    def on_double_click(self, item):
        select_item = item.text(0)

        if select_item == "Batch Processor":
            results_dialog = BatchProcessor(iface=self.iface)
            results_dialog.exec_()
        elif select_item == "Create OutletPoint Layer and Draw OutletPoint":
            _util.messagebox_show_info(
                "info",
                "The base layer and coordinate",
                "information must be created identically.",
            )
            self.iface.actionNewVectorLayer().trigger()
            # Edit 상태로 변환
            # layer = self.iface.activeLayer()
            # ADD 상태
            self.iface.actionAddFeature().trigger()
        elif select_item == "Watershed":
            results_dialog = WatershedDialog()
            results_dialog.exec_()
        elif select_item == "Helps":
            results_dialog = Watershed_StetupDialog()
            results_dialog.exec_()

    def close_event(self, event):
        self.closingPlugin.emit()
        event.accept()

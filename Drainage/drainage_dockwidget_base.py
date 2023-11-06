from qgis.PyQt import QtCore, QtWidgets


class Ui_DrainageDockWidgetBase(object):
    def setupUi(self, DrainageDockWidgetBase):
        DrainageDockWidgetBase.setObjectName("DrainageDockWidgetBase")
        DrainageDockWidgetBase.resize(373, 449)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.tree_widget = QtWidgets.QTreeWidget(self.dockWidgetContents)
        self.tree_widget.setHeaderHidden(False)
        self.tree_widget.setObjectName("tree_widget")
        self.tree_widget.headerItem().setText(0, "1")
        self.gridLayout.addWidget(self.tree_widget, 0, 0, 1, 1)
        DrainageDockWidgetBase.setWidget(self.dockWidgetContents)

        self.retranslateUi(DrainageDockWidgetBase)
        QtCore.QMetaObject.connectSlotsByName(DrainageDockWidgetBase)

    def retranslateUi(self, DrainageDockWidgetBase):
        _translate = QtCore.QCoreApplication.translate
        DrainageDockWidgetBase.setWindowTitle(
            _translate("DrainageDockWidgetBase", "Drainage")
        )


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    DrainageDockWidgetBase = QtWidgets.QDockWidget()
    ui = Ui_DrainageDockWidgetBase()
    ui.setupUi(DrainageDockWidgetBase)
    DrainageDockWidgetBase.show()
    sys.exit(app.exec_())

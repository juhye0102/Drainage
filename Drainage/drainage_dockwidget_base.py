from qgis.PyQt import QtCore, QtWidgets


class UiDrainageDockWidgetBase(object):
    def setupUi(self, drainage_dockwidget_base):
        drainage_dockwidget_base.setObjectName("drainage_dockwidget_base")
        drainage_dockwidget_base.resize(373, 449)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.tree_widget = QtWidgets.QTreeWidget(self.dockWidgetContents)
        self.tree_widget.setHeaderHidden(False)
        self.tree_widget.setObjectName("tree_widget")
        self.tree_widget.headerItem().setText(0, "1")
        self.gridLayout.addWidget(self.tree_widget, 0, 0, 1, 1)
        drainage_dockwidget_base.setWidget(self.dockWidgetContents)

        self.retranslateUi(drainage_dockwidget_base)
        QtCore.QMetaObject.connectSlotsByName(drainage_dockwidget_base)

    def retranslate_ui(self, drainage_dockwidget_base):
        _translate = QtCore.QCoreApplication.translate
        drainage_dockwidget_base.setWindowTitle(
            _translate("drainage_dockwidget_base", "Drainage")
        )


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    drainage_dockwidget_base = QtWidgets.QDockWidget()
    ui = UiDrainageDockWidgetBase()
    ui.setupUi(drainage_dockwidget_base)
    drainage_dockwidget_base.show()
    sys.exit(app.exec_())

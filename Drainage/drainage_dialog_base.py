from qgis.PyQt import QtCore, QtWidgets


class Ui_DrainageDialogBase(object):
    def setupUi(self, DrainageDialogBase):
        DrainageDialogBase.setObjectName("DrainageDialogBase")
        DrainageDialogBase.resize(400, 300)
        self.button_box = QtWidgets.QDialogButtonBox(DrainageDialogBase)
        self.button_box.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok
        )
        self.button_box.setObjectName("button_box")

        self.retranslateUi(DrainageDialogBase)
        self.button_box.accepted.connect(DrainageDialogBase.accept)
        self.button_box.rejected.connect(DrainageDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(DrainageDialogBase)

    def retranslateUi(self, DrainageDialogBase):
        _translate = QtCore.QCoreApplication.translate
        DrainageDialogBase.setWindowTitle(_translate("DrainageDialogBase", "Drainage"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    DrainageDialogBase = QtWidgets.QDialog()
    ui = Ui_DrainageDialogBase()
    ui.setupUi(DrainageDialogBase)
    DrainageDialogBase.show()
    sys.exit(app.exec_())

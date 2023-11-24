from qgis.PyQt import QtCore, QtWidgets


class UiDrainageDialogBase(object):
    def setupUi(self, drainage_dialog_base: str) -> str:
        drainage_dialog_base.setObjectName("drainage_dialog_base")
        drainage_dialog_base.resize(400, 300)
        self.button_box = QtWidgets.QDialogButtonBox(drainage_dialog_base)
        self.button_box.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok
        )
        self.button_box.setObjectName("button_box")

        self.retranslateUi(drainage_dialog_base)
        self.button_box.accepted.connect(drainage_dialog_base.accept)
        self.button_box.rejected.connect(drainage_dialog_base.reject)
        QtCore.QMetaObject.connectSlotsByName(drainage_dialog_base)

    def retranslate_ui(self, drainage_dialog_base: str) -> str:
        _translate = QtCore.QCoreApplication.translate
        drainage_dialog_base.setWindowTitle(
            _translate("drainage_dialog_base", "Drainage")
        )


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    drainage_dialog_base = QtWidgets.QDialog()
    ui = UiDrainageDialogBase()
    ui.setupUi(drainage_dialog_base)
    drainage_dialog_base.show()
    sys.exit(app.exec_())

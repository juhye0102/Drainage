from qgis.PyQt import QtCore, QtWidgets


class Ui_WatershedDialogBase(object):
    def setupUi(self, WatershedDialogBase):
        WatershedDialogBase.setObjectName("WatershedDialogBase")
        WatershedDialogBase.resize(465, 167)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            WatershedDialogBase.sizePolicy().hasHeightForWidth()
        )
        WatershedDialogBase.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(WatershedDialogBase)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(WatershedDialogBase)
        self.label_3.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.cmbShape = QtWidgets.QComboBox(WatershedDialogBase)
        self.cmbShape.setObjectName("cmbShape")
        self.gridLayout.addWidget(self.cmbShape, 1, 1, 1, 4)
        self.label_2 = QtWidgets.QLabel(WatershedDialogBase)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.btnOpenDialog = QtWidgets.QPushButton(WatershedDialogBase)
        self.btnOpenDialog.setObjectName("btnOpenDialog")
        self.gridLayout.addWidget(self.btnOpenDialog, 2, 4, 1, 1)
        self.label = QtWidgets.QLabel(WatershedDialogBase)
        self.label.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.cmbLayers = QtWidgets.QComboBox(WatershedDialogBase)
        self.cmbLayers.setObjectName("cmbLayers")
        self.gridLayout.addWidget(self.cmbLayers, 0, 1, 1, 4)
        self.btnCancel = QtWidgets.QPushButton(WatershedDialogBase)
        self.btnCancel.setObjectName("btnCancel")
        self.gridLayout.addWidget(self.btnCancel, 3, 4, 1, 1)
        self.btnOK = QtWidgets.QPushButton(WatershedDialogBase)
        self.btnOK.setObjectName("btnOK")
        self.gridLayout.addWidget(self.btnOK, 3, 3, 1, 1)
        self.txt_output = QtWidgets.QLineEdit(WatershedDialogBase)
        self.txt_output.setObjectName("txt_output")
        self.gridLayout.addWidget(self.txt_output, 2, 1, 1, 3)

        self.retranslateUi(WatershedDialogBase)
        QtCore.QMetaObject.connectSlotsByName(WatershedDialogBase)

    def retranslateUi(self, WatershedDialogBase):
        _translate = QtCore.QCoreApplication.translate
        WatershedDialogBase.setWindowTitle(
            _translate("WatershedDialogBase", "Watershed")
        )
        self.label_3.setText(_translate("WatershedDialogBase", "Outlet point :"))
        self.label_2.setText(_translate("WatershedDialogBase", "Output :"))
        self.btnOpenDialog.setText(_translate("WatershedDialogBase", "...."))
        self.label.setText(_translate("WatershedDialogBase", "Flow direction :"))
        self.btnCancel.setText(_translate("WatershedDialogBase", "Cancel"))
        self.btnOK.setText(_translate("WatershedDialogBase", "OK"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    WatershedDialogBase = QtWidgets.QDialog()
    ui = Ui_WatershedDialogBase()
    ui.setupUi(WatershedDialogBase)
    WatershedDialogBase.show()
    sys.exit(app.exec_())

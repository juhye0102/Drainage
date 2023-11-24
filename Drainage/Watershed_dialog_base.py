from qgis.PyQt import QtCore, QtWidgets


class UiWatershedDialogBase(object):
    def setupUi(self, watershed_dialog_base):
        watershed_dialog_base.setObjectName("watershed_dialog_base")
        watershed_dialog_base.resize(465, 167)
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            watershed_dialog_base.size_policy().hasHeightForWidth()
        )
        watershed_dialog_base.setSizePolicy(size_policy)
        self.gridLayout = QtWidgets.QGridLayout(watershed_dialog_base)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(watershed_dialog_base)
        self.label_3.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.cmbShape = QtWidgets.QComboBox(watershed_dialog_base)
        self.cmbShape.setObjectName("cmbShape")
        self.gridLayout.addWidget(self.cmbShape, 1, 1, 1, 4)
        self.label_2 = QtWidgets.QLabel(watershed_dialog_base)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.btnOpenDialog = QtWidgets.QPushButton(watershed_dialog_base)
        self.btnOpenDialog.setObjectName("btnOpenDialog")
        self.gridLayout.addWidget(self.btnOpenDialog, 2, 4, 1, 1)
        self.label = QtWidgets.QLabel(watershed_dialog_base)
        self.label.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.cmbLayers = QtWidgets.QComboBox(watershed_dialog_base)
        self.cmbLayers.setObjectName("cmbLayers")
        self.gridLayout.addWidget(self.cmbLayers, 0, 1, 1, 4)
        self.btnCancel = QtWidgets.QPushButton(watershed_dialog_base)
        self.btnCancel.setObjectName("btnCancel")
        self.gridLayout.addWidget(self.btnCancel, 3, 4, 1, 1)
        self.btnOK = QtWidgets.QPushButton(watershed_dialog_base)
        self.btnOK.setObjectName("btnOK")
        self.gridLayout.addWidget(self.btnOK, 3, 3, 1, 1)
        self.txt_output = QtWidgets.QLineEdit(watershed_dialog_base)
        self.txt_output.setObjectName("txt_output")
        self.gridLayout.addWidget(self.txt_output, 2, 1, 1, 3)

        self.retranslateUi(watershed_dialog_base)
        QtCore.QMetaObject.connectSlotsByName(watershed_dialog_base)

    def retranslate_ui(self, watershed_dialog_base):
        _translate = QtCore.QCoreApplication.translate
        watershed_dialog_base.setWindowTitle(
            _translate("watershed_dialog_base", "Watershed")
        )
        self.label_3.setText(
            _translate(
                "watershed_dialog_base",
                "Outlet point :",
            )
        )
        self.label_2.setText(_translate("watershed_dialog_base", "Output :"))
        self.btnOpenDialog.setText(_translate("watershed_dialog_base", "...."))
        self.label.setText(
            _translate(
                "watershed_dialog_base",
                "Flow direction :",
            )
        )
        self.btnCancel.setText(_translate("watershed_dialog_base", "Cancel"))
        self.btnOK.setText(_translate("watershed_dialog_base", "OK"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    watershed_dialog_base = QtWidgets.QDialog()
    ui = UiWatershedDialogBase()
    ui.setupUi(watershed_dialog_base)
    watershed_dialog_base.show()
    sys.exit(app.exec_())

from qgis.PyQt import QtCore, QtWidgets


class UiWatershedDialogBase(object):
    def setupUi(self, watershed_dialog_base: str) -> str:
        watershed_dialog_base.setObjectName("watershed_dialog_base")
        watershed_dialog_base.resize(400, 320)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            watershed_dialog_base.sizePolicy().hasHeightForWidth()
        )
        watershed_dialog_base.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(watershed_dialog_base)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(watershed_dialog_base)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lblCatchment = QtWidgets.QLabel(self.groupBox_3)
        self.lblCatchment.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.lblCatchment.setObjectName("lblCatchment")
        self.gridLayout_3.addWidget(self.lblCatchment, 15, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 11, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.txtSlope = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtSlope.sizePolicy().hasHeightForWidth())
        self.txtSlope.setSizePolicy(sizePolicy)
        self.txtSlope.setObjectName("txtSlope")
        self.gridLayout_3.addWidget(self.txtSlope, 11, 1, 1, 2)
        self.cmbLayer = QtWidgets.QComboBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbLayer.sizePolicy().hasHeightForWidth())
        self.cmbLayer.setSizePolicy(sizePolicy)
        self.cmbLayer.setObjectName("cmbLayer")
        self.gridLayout_3.addWidget(self.cmbLayer, 0, 1, 1, 2)
        self.txtFD = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.txtFD.sizePolicy().hasHeightForWidth(),
        )
        self.txtFD.setSizePolicy(sizePolicy)
        self.txtFD.setObjectName("txtFD")
        self.gridLayout_3.addWidget(self.txtFD, 2, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.txtCatchment = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtCatchment.sizePolicy().hasHeightForWidth())
        self.txtCatchment.setSizePolicy(sizePolicy)
        self.txtCatchment.setObjectName("txtCatchment")
        self.gridLayout_3.addWidget(self.txtCatchment, 15, 1, 1, 2)
        self.txtFAC = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtFAC.sizePolicy().hasHeightForWidth())
        self.txtFAC.setSizePolicy(sizePolicy)
        self.txtFAC.setObjectName("txtFAC")
        self.gridLayout_3.addWidget(self.txtFAC, 4, 1, 1, 2)
        self.txtFill = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtFill.sizePolicy().hasHeightForWidth())
        self.txtFill.setSizePolicy(sizePolicy)
        self.txtFill.setObjectName("txtFill")
        self.gridLayout_3.addWidget(self.txtFill, 1, 1, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.txtCellValue = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtCellValue.sizePolicy().hasHeightForWidth())
        self.txtCellValue.setSizePolicy(sizePolicy)
        self.txtCellValue.setMinimumSize(QtCore.QSize(60, 0))
        self.txtCellValue.setObjectName("txtCellValue")
        self.gridLayout_2.addWidget(self.txtCellValue, 0, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 3)
        self.txtStream = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtStream.sizePolicy().hasHeightForWidth())
        self.txtStream.setSizePolicy(sizePolicy)
        self.txtStream.setObjectName("txtStream")
        self.gridLayout_2.addWidget(self.txtStream, 2, 4, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 5, 1, 1)
        self.txtStreamVector = QtWidgets.QLineEdit(self.groupBox)
        self.txtStreamVector.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.txtStreamVector.sizePolicy().hasHeightForWidth()
        )
        self.txtStreamVector.setSizePolicy(sizePolicy)
        self.txtStreamVector.setReadOnly(False)
        self.txtStreamVector.setObjectName("txtStreamVector")
        self.gridLayout_2.addWidget(self.txtStreamVector, 3, 4, 1, 2)
        self.lblStream = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblStream.sizePolicy().hasHeightForWidth())
        self.lblStream.setSizePolicy(sizePolicy)
        self.lblStream.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblStream.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.lblStream.setObjectName("lblStream")
        self.gridLayout_2.addWidget(self.lblStream, 3, 2, 1, 1)
        self.chkStream = QtWidgets.QCheckBox(self.groupBox)
        self.chkStream.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chkStream.setText("")
        self.chkStream.setObjectName("chkStream")
        self.gridLayout_2.addWidget(self.chkStream, 3, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 1, 1, 2)
        self.gridLayout_3.addWidget(self.groupBox, 14, 0, 1, 3)
        self.gridLayout.addWidget(self.groupBox_3, 0, 0, 1, 3)
        self.btnCancel = QtWidgets.QPushButton(watershed_dialog_base)
        self.btnCancel.setObjectName("btnCancel")
        self.gridLayout.addWidget(self.btnCancel, 1, 2, 1, 1)
        self.btnOK = QtWidgets.QPushButton(watershed_dialog_base)
        self.btnOK.setObjectName("btnOK")
        self.gridLayout.addWidget(self.btnOK, 1, 1, 1, 1)
        self.lblStream.setBuddy(self.chkStream)

        self.retranslate_ui(watershed_dialog_base)
        QtCore.QMetaObject.connectSlotsByName(watershed_dialog_base)

    def retranslate_ui(self, watershed_dialog_base: str) -> str:
        _translate = QtCore.QCoreApplication.translate
        watershed_dialog_base.setWindowTitle(
            _translate("watershed_dialog_base", "Batch Processor")
        )
        self.lblCatchment.setText(
            _translate(
                "watershed_dialog_base",
                "Catchment : ",
            )
        )
        self.label_7.setText(
            _translate("watershed_dialog_base", "Flow Accumulation : ")
        )
        self.label_5.setText(
            _translate(
                "watershed_dialog_base",
                "Flow Direction : ",
            )
        )
        self.label_8.setText(
            _translate(
                "watershed_dialog_base",
                "Slope : ",
            )
        )
        self.label_2.setText(
            _translate(
                "watershed_dialog_base",
                "Fill Sink : ",
            )
        )
        self.label.setText(
            _translate(
                "watershed_dialog_base",
                "Elevation : ",
            )
        )
        self.groupBox.setTitle(
            _translate(
                "watershed_dialog_base",
                "Stream",
            )
        )
        self.label_4.setText(
            _translate(
                "watershed_dialog_base",
                "Threshold Value : ",
            )
        )
        self.label_6.setText(
            _translate(
                "watershed_dialog_base",
                "(Flow accumulation value)",
            )
        )
        self.lblStream.setText(
            _translate(
                "watershed_dialog_base",
                "Make polyline : ",
            )
        )
        self.label_9.setText(
            _translate(
                "watershed_dialog_base",
                "Raster file : ",
            )
        )
        self.btnCancel.setText(
            _translate(
                "watershed_dialog_base",
                "Cancel",
            )
        )
        self.btnOK.setText(
            _translate(
                "watershed_dialog_base",
                "OK",
            )
        )

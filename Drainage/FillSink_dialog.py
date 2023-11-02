# -*- coding: utf-8 -*-
"""
/***************************************************************************
 FillSinkDialog
                                 A QGIS plugin
 FillSink plug-in
                             -------------------
        begin                : 2017-03-13
        git sha              : $Format:%H$
        copyright            : (C) 2017 by Hermesys
        email                : shpark@hermesys.co.kr
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt5.QtWidgets import QFileDialog, QDialog
from PyQt5.QtCore import QFileInfo
import os
from PyQt5 import QtGui, uic
from .Util import *
from qgis.core import QgsProject, QgsRasterLayer

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'FillSink_dialog_base.ui'))

_layerPath=""
_util = util()
class FillSinkDialog(QDialog, FORM_CLASS):

    # 저장 위치 출력 다이얼 로그
    def Select_Ouput_File(self):
        self.txtOutput.clear();
        dir = os.path.dirname(_layerPath)
        filename = QFileDialog.getSaveFileName(self, "select output file ", dir, "*.tif")
        self.txtOutput.setText(filename)

    # 콤보 박스에서 선택한 레이어의 경로 받아오기, 받아온 경로에 한글이 있으면 메시지 창 출력
    def Get_ComboBox_LayerPath(self, combo , txt):
        if combo.currentIndex() != 0:
            if txt =="tif":
                self.TifPath = _util.GetcomboSelectedLayerPath(combo)
            elif txt =="shp":
                self.Shape = _util.GetcomboSelectedLayerPath(combo)
        # 선택된 레이어 한글 경로 있는지 확인
        if _util.CheckKorea(_layerPath) :
            self.cmbLayers.setCurrentIndex(0)
            _util.MessageboxShowInfo("FillSink", "\n The selected layer contains Korean paths. \n")

    # 레이어 목록 Qgis에 올리기
    def Addlayer_OutputFile(self, outputpath):
        if (os.path.isfile(outputpath)):
            fileName = outputpath
            fileInfo = QFileInfo(fileName)
            baseName = fileInfo.baseName()
            layer = QgsRasterLayer(fileName, baseName, "gdal")
            QgsProject.instance().addMapLayer(layer)
            
    def Click_Okbutton(self):
        self.Get_ComboBox_LayerPath(self.cmbLayers ,"tif")
        self.Get_ComboBox_LayerPath(self.cmbShape , "shp")
        arg = "C:\Program Files\TauDEM\TauDEM5Exe\GageWatershed.exe -p " + self.TifPath  + " -o " + self.Shape.split('|')[0] + " -gw " + self.txtOutput.text()
        _util.MessageboxShowInfo("arg", arg)
        returnValue=_util.Execute(arg)


        # 콤보박스 레이어 선택 하지 않았을때
        #index = self.cmbLayers.currentIndex()
        #if index == 0:
        #    _util.MessageboxShowInfo("FillSink", "\n No layer selected. \n")
        #    self.cmbLayers.setFocus()
        #    return

        ## 텍스트 박스에 결과 파일 경로가 없을때 오류 메시지 출력
        #if self.txtOutput.text() == '':
        #    _util.MessageboxShowInfo("FIllSink", "\n File path not selected. \n")
        #    self.txtOutput.setFocus()
        #    return

        ## 확장자 TIF 만 허용
        #filename = os.path.splitext(self.txtOutput.text())[1]
        #if filename.upper() !=".TIF":
        #    _util.MessageboxShowInfo("FIllSink", "\n Only TIF extensions are allowed. \n")
        #    self.txtOutput.setFocus()
        #    return


        ## True 면 한글 포함 하고 있음, False 면 한글 없음
        #if _util.CheckKorea(self.txtOutput.text()):
        #    _util.MessageboxShowInfo("FIllSink", "\n The file path contains Korean. \n")
        #    return

        #if _util.CheckFile(self.txtOutput.text()):
        #    # True 이면 기존 파일 존재함
        #    _util.MessageboxShowInfo("FIllSink", "\n A file with the same name already exists. \n")
        #    return

        ## 타우프로그램 실행 시킬 arg 문자열 받아 오기
        #arg = _util.GetTaudemArg(_layerPath, self.txtOutput.text(), _util.tauDEMCommand.SK, False,0)
        #returnValue=_util.Execute(arg)
        #if returnValue==0:
        #    self.Addlayer_OutputFile(self.txtOutput.text())
        #    _util.MessageboxShowInfo("FIllSink", "processor complete")
        #    self.close()



    # 프로그램 종료
    def Close_Form(self):
        self.close()

    def __init__(self, parent=None):

        """Constructor."""
        super(FillSinkDialog, self).__init__(parent)
        self.setupUi(self)

        #다이얼 로그 창 사이즈 조절 못하게 고정
        self.setFixedSize(self.size())

        # LineEdit 컨트롤러 초기화
        self.txtOutput.clear()

        # LineEdit 컨트롤러 비 활성화
        self.txtOutput.setDisabled(True)

        # 레이어목록 콤보 박스 리스트 넣기 이벤트
        layers = QgsProject.instance().mapCanvas().values()

        # 전달인자 layer 목록, 콤보박스,layertype("tif" or "shp" or ""-->전체 목록)
        _util.SetCommbox(layers, self.cmbLayers, "tif")

        _util.SetCommbox(layers, self.cmbShape, "shp")

        # 선택 레이어 경로 받아서 글로벌 변수에 넣어서 사용
        self.cmbLayers.activated.connect(self.Get_ComboBox_LayerPath)

        # 다이얼 로그 버튼 눌렀을때 파일 저장 경로 설정 이벤트
        self.btnOpenDialog.clicked.connect(self.Select_Ouput_File)

        # OK버튼 눌렀을때 처리 부분
        self.btnOK.clicked.connect(self.Click_Okbutton)

        # Cancle버튼 클릭 이벤트
        self.btnCancel.clicked.connect(self.Close_Form)

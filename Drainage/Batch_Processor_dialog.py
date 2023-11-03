# -*- coding: utf-8 -*-
from qgis.PyQt.QtWidgets import QDialog
from qgis.PyQt.QtCore import QFileInfo
from qgis.core import QgsProject, QgsRasterLayer
from qgis.utils import iface
import os
from qgis.PyQt import uic
from .Util import *

FORM_CLASS, _ = uic.loadUiType(
    os.path.join(os.path.dirname(__file__), "Batch_Processor_dialog_base.ui")
)

_util = util()


class BatchProcessor(QDialog, FORM_CLASS):
    # 레이어 목록 콤보 박스 셋팅
    def set_combobox(self):
        layers = QgsProject.instance().mapLayers().values()
        _util.SetCommbox(layers, self.cmbLayer, "tif")

    # 콤보 박스 선택시 이벤트 처리
    def select_combobox_event(self):
        index = self.cmbLayer.currentIndex()
        if index > 0:
            self.LayerPath = _util.GetcomboSelectedLayerPath(self.cmbLayer)
            self.Layername = _util.GetFilename(self.LayerPath)
            self.txtFill.setText(self.Layername + "_Hydro")
            # self.txtFlat.setText(self.Layername + "_Flat")
            self.txtFD.setText(self.Layername + "_Fdr")
            self.txtFAC.setText(self.Layername + "_Fac")
            self.txtSlope.setText(self.Layername + "_Slope")
            self.txtStream.setText(self.Layername + "_Stream")
            self.txtStreamVector.setText(self.Layername + "_Stream_polyline")
            self.txtCatchment.setText(self.Layername + "_Catchment")

    def is_int(self, anyNumberOrString):
        try:
            int(
                anyNumberOrString
            )  # to check float and int use "float(anyNumberOrString)"
            return True
        except ValueError:
            return False

    def click_okbutton(self):
        # 레이어 경로에 한글이 있으면 오류로 처리
        if _util.CheckKorea(self.LayerPath):
            _util.MessageboxShowInfo(
                "Batch Processor", "\n The file path contains Korean. \n"
            )
            return

        fname, ext = os.path.splitext(self.LayerPath)
        if ext.upper() in ".ASC":
            # _util.MessageboxShowInfo("1","asc")
            inputfile = self.LayerPath
            self.LayerPath = self.LayerPath.replace(ext, ".TIF")
            _util.Convert_ASCii_To_TIFF(inputfile, self.LayerPath)
            # _util.MessageboxShowInfo("Layerpath",self.LayerPath)

            # return
        elif ext.upper() in ".TIF":
            # _util.MessageboxShowInfo("1", "tif")
            pass
        else:
            _util.MessageboxShowInfo(
                "Batch Processor",
                "Only ASCII files and TIF file formats are supported.",
            )
            return

        # 파일 이름이 없는 텍스트 박스 확인
        if self.checkTextbox(self.txtFill):
            pass
        else:
            return

        # self.checkTextbox(self.txtFlat)

        if self.checkTextbox(self.txtFD):
            pass
        else:
            return

        if self.checkTextbox(self.txtFAC):
            pass
        else:
            return

        if self.checkTextbox(self.txtSlope):
            pass
        else:
            return

        if self.checkTextbox(self.txtStream):
            pass
        else:
            return

        if self.txtCellValue.text() == "":
            _util.MessageboxShowError(
                "Batch Processor",
                " CellValue is required. ",
            )
            self.txtCellValue.setFocus()
            return False

        vlaue = self.txtCellValue.text()
        if not self.isInt(vlaue):
            _util.MessageboxShowError(
                "Batch Processor",
                " Please enter only integers. ",
            )
            return

        if self.chkStream.isChecked():
            self.checkTextbox(self.txtStreamVector)

        self.checkTextbox(self.txtCatchment)

        # 파일 경로 변수에 셋팅
        self.SettingValue()

        # Fill sink 시작
        arg = _util.GetTaudemArg(
            self.LayerPath, self.Fill, _util.tauDEMCommand.SK, False, 0
        )
        result_fill = self.ExecuteArg(arg, self.Fill)

        if result_fill:
            # FD 시작
            arg = _util.GetTaudemArg(
                self.Fill, self.FD, _util.tauDEMCommand.FD, False, 0
            )
            fill_result = self.ExecuteArg(arg, self.FD)
            if fill_result:
                # FA 시작
                arg = _util.GetTaudemArg(
                    self.FD, self.FAC, _util.tauDEMCommand.FA, False, 0
                )
                fac_result = self.ExecuteArg(arg, self.FAC)
                if fac_result:
                    # Slope 시작
                    arg = _util.GetTaudemArg(
                        self.Fill, self.Slope, _util.tauDEMCommand.SG, False, 0
                    )
                    slop_result = self.ExecuteArg(arg, self.Slope)
                    if slop_result:
                        # Stream 시작
                        cell_value = self.txtCellValue.text()
                        arg = _util.GetTaudemArg(
                            self.FAC,
                            self.Stream,
                            _util.tauDEMCommand.ST,
                            False,
                            cell_value,
                        )
                        stream_result = self.ExecuteArg(arg, self.Stream)
                        if stream_result:
                            arg = self.CreateStreamVector()

                            stream_vector_result = self.ExecuteArg(
                                arg, self.StreamVector
                            )
                            if stream_vector_result:
                                # tif 파일 asc 파일로 변환
                                self.ConvertTiff_To_Asc()
                                self.Delete_tempfile()
                                _util.MessageboxShowInfo(
                                    "Batch processor",
                                    "The process is complete.",
                                )
                                self.close()

    # arg 받아서 처리 완료 되면 레이어  Qgis 에서 올림
    def execute_arg(self, arg: str) -> bool:
        return_value = _util.Execute(arg)
        if return_value == 0:
            # self.Addlayer_OutputFile(outpath)
            return True
        else:
            _util.MessageboxShowError(
                "Batch Processor",
                " There was an error creating the file. ",
            )
            return False

    def delete_tempfile(self):
        for i in range(0, 3):
            os.remove(self.outFiles[i])
        if self.chkStream.isChecked():
            pass
        else:
            os.remove(self.outFiles[3])

    # 레이어 목록 Qgis에 올리기
    def addlayer_output_file(self, outputpath: str):
        if os.path.isfile(outputpath):
            file_name = outputpath
            file_info = QFileInfo(file_name)
            base_name = file_info.baseName()
            layer = QgsRasterLayer(file_name, base_name, "gdal")
            QgsProject.instance().addMapLayer(layer)

    # 파일 경로 변수에 셋팅
    def setting_value(self):
        self.Fill = (
            os.path.dirname(self.LayerPath) + "\\" + self.txtFill.text() + ".tif",
        )
        self.FD = os.path.dirname(self.LayerPath) + "\\" + self.txtFD.text() + ".tif"

        self.FAC = os.path.dirname(self.LayerPath) + "\\" + self.txtFAC.text() + ".tif"
        self.Slope = (
            os.path.dirname(self.LayerPath) + "\\" + self.txtSlope.text() + ".tif"
        )
        self.Stream = (
            os.path.dirname(self.LayerPath) + "\\" + self.txtStream.text() + ".tif"
        )
        self.Catchment = (
            os.path.dirname(self.LayerPath) + "\\" + self.txtCatchment.text() + ".tif"
        )
        self.StreamVector = (
            os.path.dirname(self.LayerPath)
            + "\\"
            + self.txtStreamVector.text()
            + ".shp"
        )
        self.CellValue = int(self.txtCellValue.text())

    def create_stream_vector(self):
        self.outFiles = []
        self.outFiles.append(os.path.dirname(self.Fill) + "\\temp_1.tif")
        self.outFiles.append(os.path.dirname(self.Fill) + "\\temp_1.dat")
        self.outFiles.append(os.path.dirname(self.Fill) + "\\temp_2.dat")
        # outFiles3 = "C:\GRM\Sample\Gyeongpoho_DEM_Stream.shp"
        self.outFiles.append(self.StreamVector)
        # outFiles4 = os.path.dirname(self.Fill) + "\\temp_2.tif"
        self.outFiles.append(self.Catchment)
        args = ' -fel "{0}" -p "{1}" -ad8 "{2}" -src "{3}" -ord "{4}" -tree "{5}" -coord "{6}" -net "{7}" -w "{8}" '.format(
            self.Fill,
            self.FD,
            self.FAC,
            self.Stream,
            self.outFiles[0],
            self.outFiles[1],
            self.outFiles[2],
            self.outFiles[3],
            self.outFiles[4],
        )
        streamnet = '"C:\Program Files\TauDEM\TauDEM5Exe\StreamNet.exe" '

        return streamnet + args

    # 텍스트 박스에 파일 이름이 없는 경우 체크
    def check_textbox(self, txt):
        if txt.text() == "":
            _util.MessageboxShowInfo(
                "Batch Processor",
                " A filename is required. ",
            )
            txt.setFocus()
            return False
        else:
            return True

    # 기본 변수 초기화
    def setting_file(self):
        self.LayerPath = ""
        self.Layername = ""
        self.Fill = ""
        self.Flat = ""
        self.FD = ""
        self.FAC = ""
        self.Slope = ""
        self.Stream = ""
        self.CellValue = 0

    # 프로그램 종료
    def close_form(self):
        self.close()

    def convert_tiff_to_asc(self):
        _util.Convert_TIFF_To_ASCii(self.Fill)
        # _util.Convert_TIFF_To_ASCii(self.Flat)
        _util.Convert_TIFF_To_ASCii(self.FD)
        _util.Convert_TIFF_To_ASCii(self.FAC)
        _util.Convert_TIFF_To_ASCii(self.Slope)
        _util.Convert_TIFF_To_ASCii(self.Stream)
        if self.chkStream.isChecked():
            _util.VectorLayer_AddLayer(self.StreamVector)
        _util.Convert_TIFF_To_ASCii(self.Catchment)

    def checkbox_stream(self):
        if self.chkStream.isChecked():
            self.txtStreamVector.setEnabled(True)
        else:
            self.txtStreamVector.setEnabled(False)

    def set_stream_checked(self, event):
        self.chkStream.setChecked(not self.chkStream.isChecked())

    def __init__(self, parent=None, iface=None):
        """Constructor."""
        super(BatchProcessor, self).__init__(parent)
        self.setupUi(self)
        self.iface = iface

        flat_path = os.path.dirname(os.path.abspath(__file__))

        # 파일 경로 변수 선언
        self.Settingfile()

        # 콤보 박스 레이어 셋팅
        self.SetCombobox()

        # 콤보 박스 선택 시 텍스트 창에 기본 파일 이름 적용
        self.cmbLayer.currentIndexChanged.connect(self.SelectCombobox_event)

        # OK버튼 눌렀을때 처리 부분
        self.btnOK.clicked.connect(self.Click_Okbutton)
        # self.btnOK.clicked.connect(self.CreateStreamVector)

        # Cancle버튼 클릭 이벤트
        self.btnCancel.clicked.connect(self.Close_Form)

        # # 라디오 버튼 기본 설정
        self.chkStream.stateChanged.connect(self.checkbox_Stream)
        self.chkStream.setChecked(True)
        self.checkbox_Stream()

        # Stream chk와 label 연동
        # QObject.connect(self.lblStream, SIGNAL("clicked()"),
        # self.setStreamChecked)
        self.lblStream.mouseReleaseEvent = self.setStreamChecked

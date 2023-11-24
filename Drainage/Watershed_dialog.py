# -*- coding: utf-8 -*-

from qgis.PyQt.QtWidgets import (
    QFileDialog,
    QDialog,
    QMessageBox,
    QGroupBox,
    QTextEdit,
)
from qgis.PyQt.QtCore import QFileInfo
from qgis.core import QgsVectorLayer, QgsRasterLayer, QgsProject
import os
from qgis.PyQt import QtGui, QtCore
from .Util import Util
from .Watershed_dialog_base import UiWatershedDialogBase


_Prj_Back_Path = ""
_util = Util()


class WatershedDialog(QDialog, UiWatershedDialogBase):
    # 저장 위치 출력 다이얼 로그
    def select_output_file(self):
        self.txt_output.clear()
        dir = os.path.dirname(self.TifPath)
        if self.TifPath != "" and os.path.isdir(dir):
            filename = QFileDialog.getSaveFileName(
                self, "select output file ", dir, "*.tif"
            )[0]
        else:
            filename = QFileDialog.getSaveFileName(
                self, "select output file ", os.getcwd(), "*.tif"
            )[0]
        self.txt_output.setText(filename)

    # 콤보 박스에서 선택한 레이어의 경로 받아오기
    def get_combobox_layerpath(self, combo: str, txt: str):
        if combo.currentIndex() != 0:
            if txt == "tif":
                self.TifPath = _util.get_combo_selected_layerpath(combo)
            elif txt == "shp":
                self.Shape = _util.get_combo_selected_layerpath(combo).split("|")[0]

    # 레이어 목록 Qgis에 올리기
    def addlayer_output_file(self, outputpath: str) -> str:
        if os.path.isfile(outputpath):
            file_name = outputpath
            file_info = QFileInfo(file_name)
            base_name = file_info.base_name()
            layer = QgsRasterLayer(file_name, base_name, "gdal")
            QgsProject.instance().addMapLayer(layer)

    def click_okbutton(self):
        self.get_combobox_layerpath(self.cmbLayers, "tif")
        self.get_combobox_layerpath(self.cmbShape, "shp")

        # 콤보박스 레이어 선택 하지 않았을때
        r_index = self.cmbLayers.currentIndex()
        s_index = self.cmbShape.currentIndex()

        if r_index == 0:
            _util.messagebox_show_info(
                "Watershed",
                "\n No raster layer selected. \n",
            )
            self.cmbLayers.setFocus()
            return

        if s_index == 0:
            _util.messagebox_show_info(
                "Watershed",
                "\n No shape layer selected. \n",
            )
            self.cmbShape.setFocus()
            return

        # 텍스트 박스에 결과 파일 경로가 없을때 오류 메시지 출력
        if self.txt_output.text() == "":
            _util.messagebox_show_info(
                "Watershed",
                "\n File path not selected. \n",
            )
            self.txt_output.setFocus()
            return

        # True 면 한글 포함 하고 있음, False 면 한글 없음
        if _util.check_korea(self.txt_output.text()):
            _util.messagebox_show_info(
                "Watershed",
                "\n The file path contains Korean. \n",
            )
            return

        # 선택된 레이어 경로 한글 체크
        if _util.check_korea(self.TifPath):
            _util.messagebox_show_info(
                "Watershed",
                "\n selected raster layer path contains Korean. \n",
            )
            return

        # 선택된 레이어 경로 한글 체크
        if _util.check_korea(self.Shape):
            _util.messagebox_show_info(
                "Watershed",
                "\n selected shape layer path contains Korean. \n",
            )
            return

        # True 이면 기존 파일 존재함
        if _util.check_file(self.txt_output.text()):
            _util.messagebox_show_info(
                "Watershed",
                "\n A file with the same name already exists. \n",
            )
            return

        # 레스터 레이어
        base_name = _util.get_filename(self.TifPath)
        rlayer = QgsRasterLayer(self.TifPath, base_name)
        if rlayer.isValid():
            self.rcsr = self.layer_crs(rlayer)
        else:
            self.rcsr = ""
        # 벡터 레이어
        name = _util.get_filename(self.Shape)
        vlayer = QgsVectorLayer(self.Shape, name, "ogr")
        if vlayer.isValid():
            self.scsr = self.layer_crs(vlayer)
        if self.rcsr != self.scsr:
            self.about_app()
        self.check_prj_file(self.Shape)

        # 타우프로그램 실행 시킬 arg 문자열 받아 오기
        arg = _util.get_watershed(self.TifPath, self.Shape, self.txt_output.text())
        print(arg)
        return_value = _util.execute(arg)
        print("return_value : " + str(return_value))
        if return_value >= 0:
            # self.Addlayer_OutputFile(self.txt_output.text())
            self.check_prj_file_back()
            _util.convert_tiff_to_ascii(self.txt_output.text())
            print("Convert_TIFF_To_ASCii ")
            _util.messagebox_show_info("Watershed", "processor complete")
            self.close()

    def layer_crs(self, layer):
        lyrcrs = layer.crs()
        if lyrcrs.isValid():
            return lyrcrs.toProj4()
        else:
            return ""

    def check_prj_file(self, shapefile: str):
        global _Prj_Back_Path
        file_ex = os.path.splitext(shapefile)
        ext = file_ex[1]
        ext2 = _util.get_filename(shapefile)
        replace_file = shapefile.replace(ext, ".prj")

        backfile = replace_file.replace(ext2, ext2 + "_back")
        _Prj_Back_Path = backfile
        if _util.check_file(replace_file):
            os.rename(replace_file, backfile)

    def check_prj_file_back(self):
        if _util.check_file(_Prj_Back_Path):
            reback_name_file = _Prj_Back_Path.replace("_back", "")
            os.rename(_Prj_Back_Path, reback_name_file)

    # 정보창 띄움
    def about_app(self):
        website = "http://code.google.com/p/comictagger"
        email = "comictagger@gmail.com"
        project = "test"
        msg_box = QMessageBox()
        msg_box.addButton("Continue", QMessageBox.AcceptRole)
        msg_box.addButton("Cancel", QMessageBox.RejectRole)
        msg_box.setWindowTitle(self.tr("Caution!!"))
        msg_box.setTextFormat(QtCore.Qt.RichText)
        msg_box.setIconPixmap(QtGui.QPixmap(project))
        msg_box.setText(
            "If the coordinate system of the two layers are different, there may be a problem in the watershed processing.<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><font color=white>"
            + "{0},{1}</font><br><br>".format(website, email + "comictagger@gma")
        )

        self.add_group_widget(msg_box)
        ret = msg_box.exec_()
        if ret == QMessageBox.AcceptRole:
            pass
        else:
            #             self.post_grid_remove()
            self.rdo_selection()
            self.mapcanvas.refresh()
            self.scale_changed_mapcanvas()
            self.tool.scale_changed_disconnect()

    # 메시지 창에 그룹 박스와 그룹 박스안 텍스트 창넣기
    def add_group_widget(self, parent_item: str):
        self.groupWidget = QGroupBox(parent_item)
        self.groupWidget.setTitle("FD CRS")
        self.groupWidget.setGeometry(QtCore.QRect(10, 50, 480, 130))  # 사이즈
        self.groupWidget.setObjectName("groupWidget")

        self.groupWidget1 = QGroupBox(parent_item)
        self.groupWidget1.setTitle("Point CRS")
        self.groupWidget1.setGeometry(QtCore.QRect(10, 190, 480, 130))  # 사이즈
        self.groupWidget1.setObjectName("groupWidget1")

        self.txtCSR_FD = QTextEdit(self.groupWidget)
        self.txtCSR_FD.setGeometry(10, 15, 460, 105)
        self.txtCSR_FD.setText(self.rcsr)

        self.txtCSR_Point = QTextEdit(self.groupWidget1)
        self.txtCSR_Point.setGeometry(10, 15, 460, 105)
        self.txtCSR_Point.setText(self.scsr)

    # 프로그램 종료
    def close_form(self):
        self.close()

    def __init__(self, parent=None):
        super(WatershedDialog, self).__init__(parent)
        self.setupUi(self)
        self.TifPath = ""
        self.Shape = ""
        # 다이얼 로그 창 사이즈 조절 못하게 고정
        #         self.setFixedSize(self.size())

        # LineEdit 컨트롤러 초기화
        self.txt_output.clear()

        # 레이어목록 콤보 박스 리스트 넣기 이벤트
        layers = QgsProject.instance().mapLayers().values()

        # 전달인자 layer 목록, 콤보박스,layertype("tif" or "shp" or ""-->전체 목록)
        _util.set_commbox(layers, self.cmbLayers, "tif")
        _util.set_commbox(layers, self.cmbShape, "shp")

        # 다이얼 로그 버튼 눌렀을때 파일 저장 경로 설정 이벤트
        self.btnOpenDialog.clicked.connect(self.select_output_file)

        # OK버튼 눌렀을때 처리 부분
        self.btnOK.clicked.connect(self.click_okbutton)

        # Cancle버튼 클릭 이벤트
        self.btnCancel.clicked.connect(self.close_form)

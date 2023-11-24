# -*- coding: utf-8 -*-
from qgis.PyQt.QtCore import QFileInfo
from qgis.PyQt.QtWidgets import QMessageBox
from qgis.core import (
    QgsProject,
    QgsRasterLayer,
    QgsVectorLayer,
    QgsApplication,
)
from subprocess import call
import os
import os.path
import win32api
import re
import tempfile

_iface = {}


class Util:
    def __init__(self):
        self.Input_Layer_Path = ""
        self.FillSink_Layer_Path = ""
        self.FD_Layer_Path = ""
        self.FA_Layer_Path = ""
        self.Stream_Layer_Path = ""
        self.tauDemPath = ""

        self.tauDEMCommand = self.enum(
            "SK", "FLAT", "FD", "FA", "SG", "ST", "STV", "CAT"
        )

    def enum(*sequential: str, **named: str):
        enums = dict(zip(sequential, range(len(sequential))), **named)
        reverse = dict((value, key) for key, value in enums.items())
        enums["reverse_mapping"] = reverse
        return type("Enum", (), enums)

    # Taudem path 받아 오기
    def get_taudem_path(self):
        tau_path = "C:\\Program Files\\TauDEM\\TauDEM5Exe\\"
        return tau_path

    def execute(self, arg: str):
        create_no_window = 0x08000000
        value = call(arg, creationflags=create_no_window)
        return value

    # 각각의 기능별로 arg를 생성하고 반환 하는 기능
    def get_taudem_arg(
        self,
        inputfile: str,
        outputfile: str,
        taudemcommand: str,
        facoption: str,
        optionvalue: str,
    ) -> str:
        option = optionvalue
        tau_path = self.get_taudem_path()
        input = inputfile.replace("\\", "\\\\")
        output = outputfile.replace("\\", "\\\\")
        output_temp = self.get_temp_file_path(outputfile)

        arg = ""
        if taudemcommand == self.tauDEMCommand.SK:
            tau_path = tau_path + "PitRemove.exe"
            arg = (
                '"'
                + tau_path
                + '"'
                + " -z "
                + '"'
                + input
                + '"'
                + " -fel "
                + '"'
                + output
                + '"'
            )
        elif taudemcommand == self.tauDEMCommand.FD:
            tau_path = tau_path + "D8FlowDir.exe"
            arg = (
                '"'
                + tau_path
                + '"'
                + " -fel "
                + '"'
                + input
                + '"'
                + " -p "
                + '"'
                + output
                + '"'
                + " -sd8 "
                + '"'
                + output_temp
                + '"'
            )
        elif taudemcommand == self.tauDEMCommand.FA:
            tau_path = tau_path + "AreaD8.exe"
            if str(facoption) == "True":
                arg = (
                    '"'
                    + tau_path
                    + '"'
                    + " -p "
                    + '"'
                    + input
                    + '"'
                    + " -ad8 "
                    + '"'
                    + output
                    + '"'
                )
            else:
                arg = (
                    '"'
                    + tau_path
                    + '"'
                    + " -p "
                    + '"'
                    + input
                    + '"'
                    + " -ad8 "
                    + '"'
                    + output
                    + '"'
                    + " -nc "
                )
        elif taudemcommand == self.tauDEMCommand.SG:
            tau_path = tau_path + "D8FlowDir.exe"
            arg = (
                '"'
                + tau_path
                + '"'
                + " -fel "
                + '"'
                + input
                + '"'
                + " -p "
                + '"'
                + output_temp
                + '"'
                + " -sd8 "
                + '"'
                + output
                + '"'
            )
        elif taudemcommand == self.tauDEMCommand.ST:
            tau_path = tau_path + "Threshold.exe"
            arg = (
                '"'
                + tau_path
                + '"'
                + " -ssa "
                + '"'
                + input
                + '"'
                + " -src "
                + '"'
                + output
                + '"'
                + " -thresh "
                + option
            )
        return arg

    def get_cacthments_arg(
        self,
        input_layer: str,
        fd_layer: str,
        fa_layer: str,
        stream_layer: str,
        txt_output: str,
    ) -> str:
        output1 = self.get_temp_file_path(input_layer)
        output2 = output1.replace("tif", "dat")
        output3 = output1.replace("tif", "dat")
        output4 = output1.replace("tif", "shp")
        output5 = txt_output
        input0 = input_layer
        input1 = fd_layer
        input2 = fa_layer
        input3 = stream_layer
        tau_path = self.get_taudem_path()
        tau_path = tau_path + "StreamNet.exe"
        arg = (
            '"'
            + tau_path
            + '"'
            + " -fel "
            + '"'
            + input0
            + '"'
            + " -p "
            + '"'
            + input1
            + '"'
            + " -ad8 "
            + '"'
            + input2
            + '"'
            + " -src "
            + '"'
            + input3
            + '"'
            + " -ord "
            + '"'
            + output1
            + '"'
            + " -tree "
            + '"'
            + output2
            + '"'
            + " -coord  "
            + '"'
            + output3
            + '"'
            + " -net "
            + '"'
            + output4
            + '"'
            + " -w "
            + '"'
            + output5
            + '"'
        )
        return arg

    def get_watershed(self, input_layer: str, shape_layer: str, output: str):
        tau_path = self.get_taudem_path() + "GageWatershed.exe"
        arg = '"{0}" -p "{1}" -o "{2}" -gw "{3}"'.format(
            tau_path, input_layer, shape_layer, output
        )
        return arg

    # Watershed 처리
    def get_watershed_arg(
        self,
        fill_layer: str,
        fd_layer: str,
        fa_layer: str,
        txtstream_cellvalue: str,
        shp_layer: str,
        txt_output: str,
        flag: str,
    ):
        # shape 파일의 경로를 받아 오면 경로상에 layerid가 붙어서 넘오옴 그래서 문자열 잘라서 사용
        shp_path = shp_layer.split("|")[0]

        # 임시 파일 경로 생성 함수 tempfile.mktemp()
        # tempfile.mktemp() 파이썬 기본 모듈로 파일을 같은 경로로 옮기고 사용
        tem_output = tempfile.mktemp() + ".tif"
        tem_output_2 = tempfile.mktemp() + ".tif"
        tem_output_3 = tempfile.mktemp() + ".tif"
        stream_output = tempfile.mktemp() + ".tif"

        temptif = tempfile.mktemp() + ".tif"
        tempdat = tempfile.mktemp() + ".dat"
        tempdat2 = tempfile.mktemp() + ".dat"
        temp_shape = (
            os.path.dirname(shp_path)
            + "\\"
            + os.path.basename(shp_path).replace(".shp", "_net.shp")
        )

        tau_path_aread8 = self.get_taudem_path() + "Aread8.exe"
        tau_path_peuker_douglas = self.get_taudem_path() + "PeukerDouglas.exe"
        tau_path_threshold = self.get_taudem_path() + "Threshold.exe"
        tau_path_treamnet = self.get_taudem_path() + "Streamnet.exe"

        returns = "1"
        arg = (
            '"'
            + tau_path_aread8
            + '"'
            + " -p "
            + '"'
            + fd_layer
            + '"'
            + " -ad8 "
            + '"'
            + tem_output
            + '"'
            + " -o "
            + '"'
            + shp_path
            + '"'
        )
        re = self.execute(arg)
        self.messagebox_show_error("re", str(re))
        if str(re) == "0":
            arg = (
                '"'
                + tau_path_peuker_douglas
                + '"'
                + " -fel "
                + '"'
                + fill_layer
                + '"'
                + " -ss "
                + '"'
                + tem_output_2
                + '"'
            )
            re1 = self.execute(arg)
            self.messagebox_show_error("re1", str(re1))
            if str(re1) == "0":
                arg = (
                    '"'
                    + tau_path_aread8
                    + '"'
                    + " -p "
                    + '"'
                    + fd_layer
                    + '"'
                    + " -ad8 "
                    + '"'
                    + tem_output_3
                    + '"'
                    + " -o "
                    + '"'
                    + shp_path
                    + '"'
                    + " -wg "
                    + '"'
                    + tem_output_2
                    + '"'
                )
                re2 = self.execute(arg)
                self.messagebox_show_error("re2", str(re2))
                if str(re2) == "0":
                    # stream Create
                    arg = (
                        '"'
                        + tau_path_threshold
                        + '"'
                        + " -ssa "
                        + '"'
                        + tem_output_3
                        + '"'
                        + " -src "
                        + '"'
                        + stream_output
                        + '"'
                        + " -thresh "
                        + txtstream_cellvalue
                    )
                    re3 = self.execute(arg)
                    self.messagebox_show_error("re3", str(re3))
                    if str(re3) == "0":
                        arg = (
                            '"'
                            + tau_path_treamnet
                            + '"'
                            + " -fel "
                            + '"'
                            + fill_layer
                            + '"'
                            + " -p "
                            + '"'
                            + fd_layer
                            + '"'
                            + " -ad8 "
                            + '"'
                            + fa_layer
                            + '"'
                            + " -src "
                            + '"'
                            + stream_output
                            + '"'
                            + " -ord "
                            + '"'
                            + temptif
                            + '"'
                            + " -tree "
                            + '"'
                            + tempdat
                            + '"'
                            + " -coord "
                            + '"'
                            + tempdat2
                            + '"'
                            + " -net "
                            + '"'
                            + temp_shape
                            + '"'
                            + " -w "
                            + '"'
                            + txt_output
                            + '"'
                            + " -o "
                            + '"'
                            + shp_path
                            + '"'
                        )
                        if str(flag) == "True":
                            arg = arg + " -sw"
                        re4 = self.execute(arg)
                        self.messagebox_show_error("re4", str(re4))
                        if str(re4) == "0":
                            returns = "0"
        return returns

    # 윈도우 임시 폴더에 임시 파일 생성
    def get_temp_file_path(self, tempfilepath: str):
        output_temp = win32api.GetTempPath() + os.path.basename(tempfilepath)
        output_temp = output_temp.replace("\\", "\\\\")
        return output_temp

    # 콤보박스 리스트 셋팅 type은( tif, shp , "" 일땐 모두다)
    def set_commbox(self, layers: str, commbox: str, type):
        layer_list = []

        if layers is None:
            pass
        elif type.upper() == "TIF":
            for layer in layers:
                layertype = layer.type()
                if layertype == layer.RasterLayer:
                    layer_list.append(layer.name())
        elif type.upper() == "SHP":
            for layer in layers:
                layertype = layer.type()
                if layertype == layer.VectorLayer:
                    layer_list.append(layer.name())
        elif type.upper() == "POINT":
            for layer in layers:
                if layer.type() == 0:
                    if layer.geometryType() == 0:
                        layer_list.append(layer.name())
        else:
            for layer in layers:
                layer_list.append(layer.name())
        commbox.clear()
        combolist = ["select layer"]
        combolist.extend(layer_list)
        commbox.addItems(combolist)

    # 메시지 박스 출력
    def messagebox_show_info(self, title: str, message: str):
        QMessageBox.information(None, title, message)

    def messagebox_show_error(self, title: str, message: str):
        QMessageBox.warning(None, title, message)

    # 콤보 박스에서 선택된 레이어 경로 받아 오기
    def get_combo_selected_layerpath(self, commbox):
        layername = commbox.currentText()
        layer = None
        for lyr in QgsProject.instance().mapLayers().values():
            if lyr.name() == layername:
                layer = lyr
        return layer.dataProvider().dataSourceUri()

    # 파일 존재 유무 확인
    def check_file(self, path):
        filepath = path.replace("\\", "\\\\")
        if os.path.isfile(filepath):
            return True
        else:
            return False

    # 폴더 경로 맞는지 확인
    def check_folder(self, path):
        filepath = path.replace("\\", "\\\\")
        if os.path.isdir(filepath):
            return True
        else:
            return False

    def check_taudem(self):
        if os.path.isdir("C:\\Program Files\\TauDEM"):
            return True
        else:
            return False

    # 폴더및 파일 명칭에 한글 포함하고 있는지 체크
    def check_korea(self, string):
        #         sys.setdefaultencoding('utf-8')
        strs = re.sub("[^가-힣]", "", string)
        if len(strs) > 0:
            return True
        else:
            return False

    # 파일 경로 중에 파일명만 받아 오기
    def get_filename(self, filename: str):
        s = os.path.splitext(filename)
        s = os.path.split(s[0])
        return s[1]

    def convert_tiff_to_ascii(self, inputfile: str):
        # nodata 설정옵션이 Gdal 에서 안먹음
        extension = os.path.splitext(inputfile)[1]
        output = inputfile.replace(extension, ".asc")
        qgis_path = QgsApplication.instance().applicationDirPath()
        gdal_translate = qgis_path + r"\gdal_translate.exe"
        arg = '"{0}" -of AAIGrid -co FORCE_CELLSIZE=TRUE "{1}" "{2}"'.format(
            gdal_translate, inputfile, output
        )
        result = self.execute(arg)
        if result >= 0:
            self.ASC_Header_replace(output)
            self.addlayer_output_file(output)

    def convert_ascii_to_tiff(self, inputfile: str, out_file: str, qgis_path):
        gdal_translate = "C:\\Program Files\\GDAL\\gdal_translate.exe"
        arg = '"{0}" -of GTiff  "{1}" "{2}"'.format(
            gdal_translate, inputfile, qgis_path
        )
        self.execute(arg)
        # self.addlayer_output_file(output)

    def convert_tiff_to_ascii_retpaht(self, inputfile: str):
        extension = ""
        extension = os.path.splitext(inputfile)[1]
        output = inputfile.replace(extension, "_Flat.asc")
        gdal_translate = "C:\\Program Files\\GDAL\\gdal_translate.exe"
        arg = '"{0}" -of AAIGrid "{1}" "{2}"'.format(
            gdal_translate,
            inputfile,
            output,
        )
        # result = self.execute(arg)
        return output

    # 레스터 레이어 목록 Qgis에 올리기
    def addlayer_output_file(self, outputpath: str):
        if os.path.isfile(outputpath):
            file_name = outputpath
            file_info = QFileInfo(file_name)
            base_name = file_info.base_name()
            layer = QgsRasterLayer(file_name, base_name, "gdal")
            QgsProject.instance().addMapLayer(layer)

    #   QgsProject.instance().addRasterLayer(fileName, base_name)

    def vector_layer_add_layer(self, outputpath: str):
        file_name = outputpath
        file_info = QFileInfo(file_name)
        base_name = file_info.base_name()
        layer = QgsVectorLayer(outputpath, base_name, "ogr")
        QgsProject.instance().addMapLayer(layer)
        if not layer:
            self.messagebox_show_info(
                "Vector layer add",
                "Layer failed to load!",
            )

    def asc_header_replace(self, asc_file: str):
        nodata = self.ASC_Header_nodata(asc_file)
        if nodata != "" or nodata == "-9999":
            self.ASC_Replace_data(nodata, asc_file)

    def asc_header_nodata(self, asc_file: str):
        self.nodata = ""
        data_header_items = open(asc_file).readlines()[:20]
        read_lower = [
            item.lower() for item in data_header_items
        ]  # 리스트 의 모든 글자를 소문자화 시킴
        for row in read_lower:
            if "nodata_value" in row:
                self.nodata = row.replace("nodata_value", "").strip()
                break
        return self.nodata

    def asc_replace_data(self, data: str, file: str):
        # Read contents from file as a single string
        file_handle = open(file, "r")
        file_string = file_handle.read()
        file_handle.close()

        file_string = re.sub(data, "-9999", file_string)

        file_handle = open(file, "w")
        file_handle.write(file_string)
        file_handle.close()

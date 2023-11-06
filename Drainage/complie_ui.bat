@echo off
call "C:\Program Files\QGIS 3.34.0\bin\o4w_env.bat"

@echo on 
pyuic5 -x -o Batch_Processor_dialog_base.py Batch_Processor_dialog_base.ui
pyuic5 -x -o drainage_dialog_base.py drainage_dialog_base.ui
pyuic5 -x -o drainage_dockwidget_base.py drainage_dockwidget_base.ui
pyuic5 -x -o Watershed_dialog_base.py Watershed_dialog_base.ui
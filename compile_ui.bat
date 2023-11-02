@echo off
call "C:\Program Files\QGIS 3.34.0\bin\o4w_env.bat"

@echo on
pyuic5 GRM_dialog_base.ui > GRM_dialog_base.py
@echo off
@echo XingHe Studio xDisplay Backup

rem 设置搜索路径
set AppRoot=%~dp0
set path=%path%;s:\Development\Python\Python.x86.v2.7.10\;s:\Development\Python\Python.x86.v2.7.10\Lib\;s:\Development\Python\Python.XHLib\;%AppRoot%Other.libs\;
set PYTHONPATH=s:\Development\Python\Python.x86.v2.7.10\;s:\Development\Python\Python.x86.v2.7.10\Lib\;s:\Development\Python\Python.XHLib\;%AppRoot%Other.libs\;

set OutRootApp=Application

rem 清理目录
del /f/s/q %AppRoot%%OutRootApp%
rd /s/q %AppRoot%%OutRootApp%
del /f/s/q %AppRoot%Source.py\src\build
rd /s/q %AppRoot%Source.py\src\build
del /f/s/q %AppRoot%Source.py\src\dist
rd /s/q %AppRoot%Source.py\src\dist

rem 复制 Flash播放器 到 webroot
cd %AppRoot%Source.flash\
call %AppRoot%Source.flash\UpdateClient.cmd

pause 目录以及删除成功，按任意键开始重建应用程序目录

rem 7Z
pause 按任意键开始重建7Z
s:\Applications\Apps\7Zip\App\7-Zip\7z.exe a -t7z -mx9 "d:\xDisplayAtHome.v5.05.%date:~0,4%%date:~5,2%%date:~8,2%%time:~0,2%%time:~3,2%.7z" "%AppRoot%"

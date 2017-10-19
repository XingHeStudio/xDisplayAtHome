@echo off
@echo XingHe Studio xDisplay

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

rem 建立目录
md %AppRoot%%OutRootApp%
md %AppRoot%%OutRootApp%\webroot
md %AppRoot%%OutRootApp%\video

rem 编译 xDisplayAtHome
cd call %AppRoot%Source.py\src\
call %AppRoot%Source.py\src\xCompile_xDisplayAtHome.cmd
rem 复制 xDisplayAtHome 到 APP文件夹
copy /y %AppRoot%Source.py\src\xDisplayAtHome.exe %AppRoot%%OutRootApp%\
rem 编译 xGetxDid
call %AppRoot%Source.py\src\xCompile_xGetxDid.cmd
rem 复制 xGetxDid 到 APP文件夹
copy /y %AppRoot%Source.py\src\xGetxDid.exe %AppRoot%%OutRootApp%\

rem pause 按任意键开始 复制其它相关文件到APP文件夹
rem 复制 xDisplay 相关文件到 APP文件夹
copy /y %AppRoot%Source.py\src\xDisplayAtHome.cnf %AppRoot%%OutRootApp%\
copy /y %AppRoot%Source.py\src\xDisplayAtHome.msg %AppRoot%%OutRootApp%\
copy /y %AppRoot%AppEnd.VBS %AppRoot%%OutRootApp%\StopAll.vbs
copy /y %AppRoot%Readme.txt %AppRoot%%OutRootApp%\Readme.txt

rem 复制 ffmpeg 到 APP文件夹
copy /y %AppRoot%Other.libs\ffmpeg.UPX.exe %AppRoot%%OutRootApp%\xEncoder.exe

rem 复制 文泉字体 到 APP文件夹
copy /y %AppRoot%Other.libs\TitleFont.ttf %AppRoot%%OutRootApp%\TitleFont.ttf

rem 复制 Web 到 APP文件夹
xcopy /Y/S/C/F/H/R %AppRoot%Source.py\src\webroot %AppRoot%%OutRootApp%\webroot\

rem 复制 RtmpClient
copy /y %AppRoot%RtmpClient.cmd %AppRoot%%OutRootApp%\xRtmpClient.cmd

rem 复制 Demo
copy /y %AppRoot%Other.libs\Demo.Webm %AppRoot%%OutRootApp%\video\

rem 7Z
ECHO 开始备份至7Z
pause 按任意键开始重建7Z
s:\Applications\Apps\7Zip\App\7-Zip\7z.exe a -t7z -sfx -mx9 "d:\xDisplayAtHome.v5.05.%date:~0,4%%date:~5,2%%date:~8,2%%time:~0,2%%time:~3,2%.exe" "%AppRoot%%OutRootApp%\"

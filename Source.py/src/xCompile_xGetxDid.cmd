set cAppRoot=%~dp0
rem 编译 xGetxDid
del /f/s/q %cAppRoot%build
rd /s/q %cAppRoot%build
del /f/s/q %cAppRoot%dist
rd /s/q %cAppRoot%dist
del /f/s/q %cAppRoot%xGetxDid.pyc

cd %cAppRoot%
s:\Development\Python\Python.x86.v2.7.10\python.exe  %cAppRoot%xCompile_xGetxDid.py py2exe
copy /y %cAppRoot%dist\xGetxDid.exe %cAppRoot%

del /f/s/q %cAppRoot%build
rd /s/q %cAppRoot%build
del /f/s/q %cAppRoot%dist
rd /s/q %cAppRoot%dist

s:\Applications\Tools\TOOL_编程工具\加壳解壳\UPX_WIN.EXE -9 %cAppRoot%xGetxDid.exe
s:\Development\Python\Python.x86.v2.7.10\python.exe  s:\Development\Python\Python.x86.v2.7.10\Lib\compileall.py %cAppRoot%xGetxDid.py
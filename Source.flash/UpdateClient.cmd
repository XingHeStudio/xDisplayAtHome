rem ¸´ÖÆ webroot
del /f/s/q ..\Source.py\src\webroot\history
rd /s/q ..\Source.py\src\webroot\history
xcopy /Y/S/E/C/F/H/R .\bin-release\*.* ..\Source.py\src\webroot\
del /f/s/q ..\Source.py\src\webroot\xClient.xml*

rem call s:\Project\xDisplayAtHome\Source.flash\UpdateClient.APP.cmd
rem ¸´ÖÆ webroot
del /f/s/q ..\Application\webroot\history
rd /s/q ..\Application\webroot\history
xcopy /Y/S/E/C/F/H/R .\bin-release\*.* ..\Application\webroot\
del /f/s/q ..\Application\webroot\xClient.xml*


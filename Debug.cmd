@echo off

rem XingHe Studio xDisplay Encode Client
set AppRoot=%~dp0
cd %AppRoot%Other.libs\

rem 设置参数
set xOutText=视频演示
set RtmpUrl=rtmp://127.0.0.1:1935/xDisplay/
set xDisplayName=Video

%AppRoot%Source.py\src\xGetxDid.exe %xDisplayName% > %AppRoot%Source.py\src\xGetxDid.txt
rem xGetxDid.exe RtmpVideoUrl -o 可输出信息文件
for /f %%i in ( %AppRoot%Source.py\src\xGetxDid.txt) do set xDisplayID=%%i

rem 编码行 演示高清视频 (RTMP标清+本地高清录制) <2mb/s 
set RecordFileName=%AppRoot%Source.py\src\Storage\Record_%date:~0,4%%date:~5,2%%date:~8,2%_%time:~0,2%%time:~3,2%%time:~6,2%.flv

start "RtmpCodeApp" /D "%AppRoot%Other.libs\" /HIGH  "%AppRoot%Other.libs\ffmpeg.UPX.exe" -re -i "%AppRoot%Other.libs\Demo.Webm" -vf drawtext="fontfile=TitleFont.ttf:fontsize=20:fontcolor=white:shadowcolor=black:shadowx=1:shadowy=1:text='%xOutText%':x=6:y=6" -q 5 -s 800*450 -aspect 16:9 -r 15 -threads 4 -vcodec flv -acodec libmp3lame -ar 44100 -ab 96k -ac 2 -f flv "%RtmpUrl%%xDisplayID%" -vf drawtext="fontfile=TitleFont.ttf:fontsize=18:fontcolor=white:shadowcolor=black:shadowx=2:shadowy=1:text='%xOutText%':x=12:y=12" -q 3 -s 1280*720 -aspect 16:9 -r 25 -threads 4 -vcodec flv -acodec libmp3lame -ar 44100 -ab 128k -ac 2 -f flv "%RecordFileName%"

rem start /max iexplore.exe "http://127.0.0.1:80"

rem exit
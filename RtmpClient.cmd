@echo off

rem XingHe Studio xDisplay Encode Client v5.05.20150603
set AppRoot=%~dp0
cd %AppRoot%

rem 设置参数
set VideoText=视频演示(1024×576)
set RtmpUrl=rtmp://127.0.0.1:1935/xDisplay/
set VideoName=Video
%AppRoot%xGetxDid.exe %VideoName% > %AppRoot%xGetxDid.txt
rem xGetxDid.exe RtmpVideoUrl -o 可输出信息文件
for /f %%i in (xGetxDid.txt) do set xDisplayID=%%i

rem 视频录制路径名
set RecordFileName=%AppRoot%Storage\Record_%date:~0,4%%date:~5,2%%date:~8,2%_%time:~0,2%%time:~3,2%%time:~6,2%.flv

rem 要编码的视频文件
set VideoFileName=%AppRoot%Video\Demo.Webm

rem 编码行 演示高清视频 (RTMP标清+本地高清录制) <2mb/s 
start "RtmpCodeApp" /D "%AppRoot%" /HIGH  "%AppRoot%xEncoder.exe" -re -i "%VideoFileName%" -vf drawtext="fontfile=TitleFont.ttf:fontsize=20:fontcolor=white:shadowcolor=black:shadowx=1:shadowy=1:text='%VideoText%':x=6:y=6" -q 5 -s 1024*576 -aspect 16:9 -r 15 -threads 4 -vcodec flv -acodec libmp3lame -ar 44100 -ab 96k -ac 2 -f flv "%RtmpUrl%%xDisplayID%" -vf drawtext="fontfile=TitleFont.ttf:fontsize=18:fontcolor=white:shadowcolor=black:shadowx=2:shadowy=1:text='%VideoText%':x=12:y=12" -q 3 -s 1280*720 -aspect 16:9 -r 25 -threads 4 -vcodec flv -acodec libmp3lame -ar 44100 -ab 128k -ac 2 -f flv "%RecordFileName%"

start /max iexplore.exe "http://127.0.0.1:80/"

exit

rem =========================================================
rem 枚举DShow设备
rem "xEncoder.exe" -list_devices true -f dshow -i dummy

rem 编码行 采集卡视频直播 (RTMP+本地录制) <512k/s 实际在400k/s左右 （8mb带宽可以承受20个客户端）
rem start "RtmpCodeApp" /D "%AppRoot%" /MIN /HIGH  "%AppRoot%xEncoder.exe" -copyinkf -f dshow -i video="Syntek STK1150":audio="USB Audio Interface" -target pal-dv -vf drawtext="fontfile=TitleFont.ttf:fontsize=14:fontcolor=white:shadowcolor=black:shadowx=2:shadowy=1:text='%VideoText%':x=8:y=8" -b 320k -s 480*360 -aspect 4:3 -r 10 -vcodec flv -ar 22050 -ab 32k -ac 1 -acodec libmp3lame -threads 4 -f flv "%RtmpUrl%%xDisplayID%" -target pal-dv -vf drawtext="fontfile=TitleFont.ttf:fontsize=14:fontcolor=white:shadowcolor=black:shadowx=2:shadowy=1:text='%VideoText%':x=8:y=8" -q 2 -s 720*576 -aspect 4:3 -r 25 -vcodec flv -ar 44100 -ab 128k -ac 1 -acodec libmp3lame -threads 4 -f flv "%RecordFileName%" 

rem 编码行 演示高清视频 (RTMP标清+本地高清录制) <2mb/s 
rem start "RtmpCodeApp" /D "%AppRoot%" /HIGH  "%AppRoot%xEncoder.exe" -re -i "%VideoFileName%" -vf drawtext="fontfile=TitleFont.ttf:fontsize=20:fontcolor=white:shadowcolor=black:shadowx=1:shadowy=1:text='%VideoText%':x=6:y=6" -q 5 -s 720*405 -aspect 16:9 -r 15 -threads 4 -vcodec flv -acodec libmp3lame -ar 44100 -ab 96k -ac 2 -f flv "%RtmpUrl%%xDisplayID%" -vf drawtext="fontfile=TitleFont.ttf:fontsize=18:fontcolor=white:shadowcolor=black:shadowx=2:shadowy=1:text='%VideoText%':x=12:y=12" -q 3 -s 1280*720 -aspect 16:9 -r 25 -threads 4 -vcodec flv -acodec libmp3lame -ar 44100 -ab 128k -ac 2 -f flv "%RecordFileName%"

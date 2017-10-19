#=========================================================================================#

<ERROR.Title>错误信息</ERROR.Title>

<MESSAGE.Title>提示信息</MESSAGE.Title>
<ERROR.001>要获取的视频名称错误，无法连接！</ERROR.001>
<ERROR.002>要获取的视频名称为空，无法连接！</ERROR.002>
<ERROR.010>要获取的视频UID错误，无法解析！</ERROR.010>
<ERROR.011>要获取的视频UID为空，无法解析！</ERROR.011>
<ERROR.012>要获取的视频UID不存在，无法解析！</ERROR.012>

#=========================================================================================#

<XML.CNFFORMAT>
	<?xml version="1.0" encoding="UTF-8"?>
	<config>
		#视频ID对应的配置信息
		<Var.DateTime>%DateTime%</Var.DateTime>#视频Uid生成时间
		<Var.Url>%Url%</Var.Url>#视频的Url
		<Var.Did>%Did%</Var.Did>#视频的Did		
		<Var.Stretch>%Stretch%</Var.Stretch>#显示是否拉伸
		<Var.ChkStretch>%ChkStretch%</Var.ChkStretch>#是否显示拉伸选择控件
		<Var.Mute>%Mute%</Var.Mute>#设置是否静音
		<Var.ChkMute>%ChkMute%</Var.ChkMute>#是否显示静音选择控件
		<Var.MsgReSize>%MsgReSize%</Var.MsgReSize>#是否显示调整窗口大小信息
		<Var.FlashDebug>%FlashDebug%</Var.FlashDebug>#是否显示Flash调试信息		
	</config>
</XML.CNFFORMAT>

#=========================================================================================#

<Page.Index>
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>{{ Title }}</title>
    <link rel="stylesheet" href="default.css">
  </head>
  <body>
  <table width="800" height="50" border="0" align="center">
      <tr>
        <td width="325" align="left" valign="middle"><span class="LogoX">x</span><span class="LogoD">D</span><span class="LogoI">i</span><span class="LogoS">s</span><span class="LogoPlay">play</span>&nbsp;<span class="LogoAt">At</span>&nbsp;<span class="Logo">Home&nbsp;Service</span></td>
        <td width="280" align="right" valign="middle"></td>
        <td width="195" align="left" valign="middle"></td>
      </tr>
  </table>
  <table width="800" height="450" border="0" align="center">
    <tr>
        <td align="center" valign="top" bgcolor="#D9ECFF">
        <iframe name="xDisplayAtHome" marginwidth=0 marginheight=0 scrolling="no" frameborder="0" width=100% height=100% src="/{{ Web.xDisplay }}:{{ Video }}" >视频</iframe>
        </td>
    </tr>
  </table>
  <table width="800" height="50" border="0" align="center">
      <tr>
        <td align="right" valign="middle" class="Foot">Created by <a href="http://XingHeStudio.com" target=_blank >XingHeStudio</a>&nbsp;&nbsp;(&nbsp;<a href="https://git.oschina.net/XingHeStudio/xDisplayAtHome" target=_blank >Project Page</a>&nbsp;)</td>
      </tr>
  </table>  
  </body>
</html>
</Page.Index>

#=========================================================================================#

<Page.Message>
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>{{ Title }}</title>
    <link rel="stylesheet" href="default.css">
  </head>
  <body>
  <table width="750" height="50" border="0" align="center">
      <tr>
        <td width="325" align="left" valign="middle"><span class="LogoX">x</span><span class="LogoD">D</span><span class="LogoI">i</span><span class="LogoS">s</span><span class="LogoPlay">play</span>&nbsp;<span class="LogoAt">At</span>&nbsp;<span class="Logo">Home&nbsp;Service</span></td>
        <td width="280" align="right" valign="middle"></td>
        <td width="195" align="left" valign="middle"></td>
      </tr>
    </table>
  <table width="750" height="50" border="0" align="center">
    <tr>
      <td>&nbsp;</td>
    </tr>
  </table>
  <table width="650" height="300" border="0" align="center">
    <tr>
        <td align="center" valign="top" bgcolor="#D9ECFF">
        <p class="Message01">{{ Titlemsg }}</p>
          <table width=100% height="220" border="0">
            <tr>
              <td align="left" valign="top" width="20">
              </td>
              <td align="left" valign="top" height="50">
                {{ Message }}
              </td>
              <td align="left" valign="top" width="20">
              </td>
            </tr>
          </table>
        </td>
    </tr>
  </table>
  <table width="750" height="50" border="0" align="center">
    <tr>
      <td>&nbsp;</td>
    </tr>
  </table>  
  <table width="500" height="50" border="0" align="center">
      <tr>
        <td align="right" valign="middle" class="Foot">Created by <a href="http://XingHeStudio.com" target=_blank >XingHeStudio</a>&nbsp;&nbsp;(&nbsp;<a href="https://git.oschina.net/XingHeStudio/xDisplayAtHome" target=_blank >Project Page</a>&nbsp;)</td>
      </tr>
  </table>  
  </body>
</html>
</Page.Message>

#=========================================================================================#

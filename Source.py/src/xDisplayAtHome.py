#coding=UTF-8
# xDisplayAtHome Service v5.05.20150603
# 星河创作室(XingHeStudio.com)
# Create by Stream.Wang 2012-09-22
# Modify by Stream.Wang 2015-06-03

import os,sys,datetime
import tornado.web, tornado.ioloop
import xhlib

if hasattr(sys,"setdefaultencoding"):sys.setdefaultencoding("utf-8")

#-------------------------------------------------------
# 系统初始化->读取参数

# 系统初始化->输出调试信息
global sys_showdebug
sys_showdebug=False
def sys_debug(inDebugStr='',printtxt=sys_showdebug):
    if printtxt==True : 
        dt=datetime.datetime.now()
        tDtStr=dt.strftime('%Y-%m-%d %H:%M:%S')+'.'+str(int(dt.microsecond/1000))
        xinDebugStr=inDebugStr.rstrip()
        print('[Debug] '+tDtStr+' >> '+xinDebugStr)
    return     
    
# 系统初始化->服务版本
global sys_servicever
sys_servicever=r'v5.05.20150603'
sys_debug('sys_servicever: '+sys_servicever)

# 系统初始化->初始化Did存储空间
global sys_DidConfig
sys_DidConfig='#Display ID Config Setup\r\n'

# 系统初始化->系统应用程序名    
global sys_appname
sys_appname=os.path.basename(sys.argv[0]) #系统应用程序名
sys_debug('sys_appname: '+sys_appname)

# 系统初始化->系统所在路径
global sys_apppath
sys_apppath=os.path.dirname(sys.argv[0])+xhlib.sys_pathstr() #系统所在路径
sys_debug('sys_apppath: '+sys_apppath)

# 系统初始化->系统配置文件路径名
global sys_appcnf
sys_appcnf=xhlib.fil_changefileext(sys.argv[0],'.cnf') #配置文件
sys_debug('sys_appcnf: '+sys_appcnf)

# 系统初始化->读取系统配置文件
global sys_config
if os.path.isfile(sys_appcnf):
    sys_config=xhlib.fil_file2str(sys_appcnf) # 读取系统配置文件
    sys_debug('Read Config File:'+sys_appcnf)
    #sys_debug('sys_config:\n'+sys_config)
else:
    print '[ERROR] load Config File fail!'
    sys.exit()

# 系统初始化->系统信息文件路径名
global sys_appmsg
sys_appmsg=xhlib.fil_changefileext(sys.argv[0],'.msg') #信息文件
sys_debug('sys_appmsg: '+sys_appmsg)
    
# 系统初始化->读取系统信息文件
global sys_message
if os.path.isfile(sys_appmsg):
    sys_message=xhlib.fil_file2str(sys_appmsg) # 读取系统信息文件
    sys_debug('Read Message File:'+sys_appmsg)    
    #sys_debug('sys_message:\n'+sys_message)
else:
    print '[ERROR] load Message File fail!'
    sys.exit()

def GetCnf(insys_config,VarName,VarType='S',DefVar='',VarNameStr='',Trim=True):
    #返回指定名称的配置 S=Strig B=Boolean I=Integer F=Float
    return xhlib.str_getxmlcfg(insys_config, VarName, VarType, DefVar, VarNameStr, Trim,sys_showdebug)
    
def GetMsg(insys_message,VarName):
    #返回指定名称的信息
    outvar=xhlib.str_getxmltxt(insys_message,VarName)
    return str(outvar)

def GetPath(insys_config,VarName,VarNameStr,ReplaceTF=True,CreateTF=True):
    outvar=GetCnf(insys_config,VarName,'S',sys_apppath)
    #if ReplaceTF==True: outvar=outvar.replace(r'%apppath%' , sys_apppath )
    if (ReplaceTF==True) : outvar=xhlib.str_replace(r"%s" % outvar, r'%apppath%', r"%s" % sys_apppath)
    if ReplaceTF==True: outvar=outvar.replace(r'%|%' , xhlib.sys_pathstr() )
    if outvar[-1]<>xhlib.sys_pathstr() : outvar=outvar+xhlib.sys_pathstr()
    if (CreateTF==True)and(os.path.exists(outvar)==False) : os.mkdir(outvar)
    sys_debug(VarNameStr+': '+outvar)
    return outvar

def GetUid(zDisplayDName,RtmpHost='127.0.0.1',RtmpPort='1935',RtmpRoot='xDisplay'):
    #获取视频设置
    tDTStr="""
    <Type.Default>
        <Stretch>False</Stretch> #初始化显示是否拉伸（True / False）
        <ChkStretch>True</ChkStretch> #是否显示设置拉伸控件（True / False）
        <Mute>False</Mute> #初始化静音（True / False）
        <ChkMute>True</ChkMute> #是否显示设置静音控件（True / False）
        <MsgReSize>True</MsgReSize> #是否显示调整窗口大小信息（True / False）
        <FlashDebug>False</FlashDebug>#是否显示Flash调试信息（True / False）
    </Type.Default>"""
    #获取视频类型设置
    xType=xhlib.str_getxmlcfg(sys_config,'Type.Default','s',tDTStr,'Type.Default',True,False)
    xStretch=str(xhlib.str_getxmltxt(xType,r'Stretch')).strip()#读取是否拉伸
    xChkStretch=str(xhlib.str_getxmltxt(xType,r'ChkStretch')).strip()#读取是否显示拉伸控件
    xMute=str(xhlib.str_getxmltxt(xType,r'Mute')).strip()#读取是否静音
    xChkMute=str(xhlib.str_getxmltxt(xType,r'ChkMute')).strip()#读取是否显示静音控件
    xMsgReSize=str(xhlib.str_getxmltxt(xType,r'MsgReSize')).strip()#是否显示调整窗口大小信息
    #生成XML信息    
    import xGetxDid
    xuid=GetMsg(sys_message,'XML.CNFFORMAT')#读取模板
    #xuid=xuid.replace(r'%Url%',r'rtmp://'+RtmpHost+':'+RtmpPort+'/'+RtmpRoot)
    #xuid=xuid.replace(r'%Did%',xGetxDid.Did_Encryption(zDisplayDName) )        
    #xuid=xuid.replace(r'%Stretch%', xStretch)
    #xuid=xuid.replace(r'%ChkStretch%', xChkStretch)
    #xuid=xuid.replace(r'%Mute%', xMute)
    #xuid=xuid.replace(r'%ChkMute%', xChkMute)
    #xuid=xuid.replace(r'%MsgReSize%', xMsgReSize)
    xuid=xhlib.str_replace(xuid,r'%Url%',r'rtmp://'+RtmpHost+':'+RtmpPort+'/'+RtmpRoot)
    xuid=xhlib.str_replace(xuid,r'%Did%',xGetxDid.Did_Encryption(zDisplayDName) )        
    xuid=xhlib.str_replace(xuid,r'%Stretch%', xStretch)
    xuid=xhlib.str_replace(xuid,r'%ChkStretch%', xChkStretch)
    xuid=xhlib.str_replace(xuid,r'%Mute%', xMute)
    xuid=xhlib.str_replace(xuid,r'%ChkMute%', xChkMute)
    xuid=xhlib.str_replace(xuid,r'%MsgReSize%', xMsgReSize)
    xuid=xhlib.str_replace(xuid,r'%FlashDebug%', str(sys_flashdebug))    
    xdt=datetime.datetime.now()
    xdtstr=xdt.strftime('%Y-%m-%d %H:%M:%S.')+("%03d" % int(xdt.microsecond/1000))
    #xuid=xuid.replace(r'%DateTime%', xdtstr)
    xuid=xhlib.str_replace(xuid,r'%DateTime%', xdtstr)
    #写入Did配置
    return xuid

def Setlog(logstr,logtype=''):
    #写入日志
    if (sys_log==True):
        LogFile=path_logfile+logtype+datetime.datetime.now().strftime('%Y%m%d%H')+'.log'#日志文件
        xhlib.fil_writelog(LogFile,logstr)

# 系统初始化->读取系统变量->服务名称 sys.ServiceName
global sys_servicename
sys_servicename=GetCnf(sys_config,'sys.servicename','S', r'xDisplay Service','sys_servicename')#服务名称

# 系统初始化->读取系统变量->网页服务名称 sys.WebPageName
global sys_webpagename
sys_webpagename=GetCnf(sys_config,'sys.webpagename','S', r'xDisplay Web Service','sys_webpagename')#网页服务名称

# 系统初始化->读取系统变量->服务名称加版本 ServiceNameVer
global sys_servicenamever
sys_servicenamever=str(sys_servicename)+' '+ str(sys_servicever)
sys_debug('sys_servicenamever: '+sys_servicenamever)    

# 系统初始化->系统获取外部参数
argvhp=''#保存web端口参数
argvrp=''#保存rtmp端口参数
argvht=''#保存web启用参数
argvrt=''#保存rtmp启用参数
args=sys.argv
argnum=len(args)
for i in args:
    if i>0:
        if i.split('=')[0].lower()=='httpport'.lower(): argvhp=str( i.split('=')[1].lower())
        if i.split('=')[0].lower()=='rtmpport'.lower(): argvrp=str( i.split('=')[1].lower())        
        if i.split('=')[0].lower()=='httpservice'.lower(): argvht=str( i.split('=')[1].lower())
        if i.split('=')[0].lower()=='rtmpservice'.lower(): argvrt=str( i.split('=')[1].lower())

# 系统初始化->初始化HTTP监听端口 sys_httpport
try:
    sys_httpport = int(argvhp) #HTTP监听端口 > 来自外部参数
    sys_debug('sys_httpport: arg.httpport='+argvhp)
except:
    sys_debug('sys_httpport: arg.httpport Ignore')
    sys_httpport=GetCnf(sys_config,'sys.httpport','I',80,'sys_httpport') 

# 系统初始化->初始化RTMP监听端口 sys_rtmpport
try:
    sys_rtmpport = int(argvrp) #RTMP监听端口 > 来自外部参数
    sys_debug('sys_rtmpport: arg.rtmpport='+argvrp)    
except:
    sys_debug('sys_rtmpport: arg.rtmpport Ignore')    
    sys_rtmpport=GetCnf(sys_config,'sys.rtmpport','I',1935,'sys_rtmpport')

# 系统初始化->初始化HTTP服务开关 sys_httpservice
try:
    sys_httpservice = bool(int(argvht)) #HTTP服务开关 > 来自外部参数
    sys_debug('sys_httpservice: arg.httpservice='+str(bool(int(argvht))))    
except:
    sys_debug('sys_httpservice: arg.httpservice Ignore ')    
    sys_httpservice=GetCnf(sys_config,'sys.httpservice','B',True,'sys_httpservice')

# 系统初始化->初始化RTMP服务开关 sys_rtmpservice
try:
    sys_rtmpservice = int(argvrt) #RTMP服务开关 > 来自外部参数
    sys_debug('sys_rtmpservice: arg.rtmpservice='+argvrt)    
except:
    sys_debug('sys_rtmpservice: arg.rtmpservice Ignore')
    sys_rtmpservice=GetCnf(sys_config,'sys.rtmpservice','B',True,'sys_rtmpservice')

#-------------------------------------------------------
# 系统初始化->读取系统变量
def LoadSysconfig():
    global sys_config
    sys_config=xhlib.fil_file2str(sys_appcnf) # 读取系统配置文件
    global sys_message
    sys_message=xhlib.fil_file2str(sys_appmsg) # 读取系统信息文件
    
    # 系统初始化->读取系统变量->系统日志目录 path.LogFile
    global path_logfile
    path_logfile=GetPath(sys_config,'path.logfile','path_logfile',True,True)
    
    # 系统初始化->读取系统变量->系统网页目录 path.WebRoot
    global path_webroot
    path_webroot=GetPath(sys_config,'path.webroot','path_webroot',True,True)

    # 系统初始化->读取系统变量->系统存储目录 path.Storage
    global path_storage
    path_storage=GetPath(sys_config,'path.Storage','path_storage',True,True)

    # 系统初始化->读取系统变量->系统网页模板目录 path.Template
    global path_template
    path_template=GetPath(sys_config,'path.template','path_template',True,True)    

    # 系统初始化->读取系统变量->是否记录日志 sys.Log
    global sys_log
    sys_log=GetCnf(sys_config,'sys.log','B', True,'sys_log')#是否记录日志    

    # 系统初始化->读取系统变量->是否输出错误 sys.EchoError
    global sys_echoerror
    sys_echoerror=GetCnf(sys_config,'sys.echoerror','B', False,'sys_echoerror')#是否输出错误    
    
    # 系统初始化->读取系统变量->是否即时更新配置 sys.RefreshSetup
    global sys_refreshsetup
    sys_refreshsetup=GetCnf(sys_config,'sys.refreshsetup','B', False,'sys_refreshsetup')#是否即时更新配置
        
    # 系统初始化->读取系统变量->是否显示调试信息 sys.FlashDebug
    global sys_flashdebug
    sys_flashdebug=GetCnf(sys_config,'sys.flashdebug','B', False,'sys_flashdebug')#是否显示调试信息

    # 系统初始化->读取系统变量->HTTP日志文件前缀 log.HttpLog
    global log_httplog
    log_httplog=GetCnf(sys_config,'log.httplog','s', 'Http.','log_httplog')#是否即时更新配置
        
    # 系统初始化->读取系统变量->网页Message路径 web.Message
    global web_message
    web_message=GetCnf(sys_config,'web.message','S',r'Message.html','web_message')#网页Message路径

    # 系统初始化->读取系统变量->xDisplay根名称 web.xDisplay
    global web_xDisplay
    web_xDisplay=GetCnf(sys_config,'web.xDisplay','S',r'xDisplay.html','web_xDisplay')#xDisplay根名称
    
    # 系统初始化->读取系统变量->RTMP根名称 web.RtmpRoot
    global web_rtmproot
    web_rtmproot=GetCnf(sys_config,'web.rtmproot','S',r'xDisplay','web_rtmproot')#RTMP根名称
    
    # 系统初始化->读取系统变量->客户端播放器配置页面路径 web.ClientXml
    global web_clientxml
    web_clientxml=GetCnf(sys_config,'web.clientxml','S',r'xClient.xml','web_clientxml')#客户端播放器配置页面路径
    
    # 系统初始化->读取系统变量->客户端播放器页面路径 web.ClientPage
    global web_clientpage
    web_clientpage=GetCnf(sys_config,'web.clientpage','S',r'xClient.html','web_clientpage')#客户端播放器页面路径
    
    # 系统初始化->读取系统变量->Index页面路径 web.IndexPage
    global web_indexpage
    web_indexpage=GetCnf(sys_config,'web.Index','S',r'index.html','web_indexpage')#Index页面路径

    #装载配置完成
    return

#-------------------------------------------------------
#读取初始化数据    
LoadSysconfig()

# 系统初始化->RTMP服务创建
import rtmp,multitask
rtmpsvr = rtmp.FlashServer()
if (sys_rtmpservice==True):
    rtmpsvr.start(r'0.0.0.0',sys_rtmpport) #开始监听RTMP
    
# 系统初始化->RTMP进程启动
def StartRtmp():
    multitask.run() 
    
# 系统初始化->定义页面入口名称
global Url_Root
Url_Root=r'/' #根路径

global Url_index
Url_index=r'/'+web_indexpage #xClient路径

global Url_Message
Url_Message=r'/'+web_message #Message路径

global Url_xDisplay
Url_xDisplay=r'/'+web_xDisplay+r':.*' #xDisplay路径

global Url_ClientXml
Url_ClientXml=r'/'+web_clientxml #ClientXml路径

# 系统初始化->Tornado设置信息
settings = {"static_path": path_webroot,"template_path":path_template, 'gzip':True, 'debug':False, 'cookie_secret':sys_servicename}
                
#=======================================================
# 页面处理过程
class App_Root(tornado.web.RequestHandler):
    def get(self):
        if sys_refreshsetup==True : LoadSysconfig() #是否即时更新配置
        if sys_log==True: Setlog(str(self.request),log_httplog) #HTTP日志        
        self.redirect('http://'+self.request.headers['Host']+Url_index+'?v=Video')
        return

class App_Index(tornado.web.RequestHandler):
    def get(self):
        stt = datetime.datetime.now()-datetime.timedelta(microseconds=1000)
        self.set_header('Server', sys_servicename)
        if sys_refreshsetup==True : LoadSysconfig() #是否即时更新配置
        if sys_log==True: Setlog(str(self.request),log_httplog) #HTTP日志
        #输出开始
        try:
            tVideo=self.get_argument("v")
        except:
            tVideo='Video'        
        outhtml=GetMsg(sys_message,'Page.Index')
        #outhtml=outhtml.replace(r'{{ Title }}', sys_webpagename)        
        #outhtml=outhtml.replace(r'{{ Video }}', tVideo)
        #outhtml=outhtml.replace(r'{{ Web.xDisplay }}', web_xDisplay)
        outhtml=xhlib.str_replace(outhtml,r'{{ Title }}', sys_webpagename)
        outhtml=xhlib.str_replace(outhtml,r'{{ Video }}', tVideo)
        outhtml=xhlib.str_replace(outhtml,r'{{ Web.xDisplay }}', web_xDisplay)        
        self.write(outhtml)
        #输出结束
        self.write('<!-- Processing time ['+str((datetime.datetime.now()-stt).microseconds/1000/1000.00000000)+']-->')
        return

class App_Message(tornado.web.RequestHandler):
    def get(self):
        stt = datetime.datetime.now()-datetime.timedelta(microseconds=1000)
        self.set_header('Server', sys_servicename)
        if sys_refreshsetup==True : LoadSysconfig() #是否即时更新配置
        if sys_log==True: Setlog(str(self.request),log_httplog) #HTTP日志
        #输出开始
        try:
            tMID=self.get_argument("MID")
        except:
            tMID='MESSAGE.001'
        if tMID.find('MESSAGE.')>-1:
            tStr2=GetMsg(sys_message,'MESSAGE.Title') 
        elif tMID.find('ERROR.')>-1:
            tStr2=GetMsg(sys_message,'ERROR.Title')         
        else : 
            tStr2='Message Title'
        if (tMID.find('MESSAGE.')>-1)or(tMID.find('ERROR.')>-1):
            tStr3=GetMsg(sys_message,tMID)
            if (tStr3.strip()==''): tStr3= 'Message Text ...'
        else:
            tStr3= 'Message Text ...'
        outhtml=GetMsg(sys_message,'Page.Message')
        #outhtml=outhtml.replace(r'{{ Title }}', sys_webpagename+' -- '+tStr2)        
        #outhtml=outhtml.replace(r'{{ TitleMsg }}', tStr2)
        #outhtml=outhtml.replace(r'{{ Message }}', tStr3)
        outhtml=xhlib.str_replace(outhtml,r'{{ Title }}', sys_webpagename+' -- '+tStr2)
        outhtml=xhlib.str_replace(outhtml,r'{{ TitleMsg }}', tStr2)
        outhtml=xhlib.str_replace(outhtml,r'{{ Message }}', tStr3)
        self.write(outhtml)
        #输出结束
        self.write('<!-- Processing time ['+str((datetime.datetime.now()-stt).microseconds/1000/1000.00000000)+']-->')
        return

class App_xDisplay(tornado.web.RequestHandler):
    def get(self):
        self.set_header('Server', sys_servicename)
        if sys_refreshsetup==True : LoadSysconfig() #是否即时更新配置
        if sys_log==True: Setlog(str(self.request),log_httplog) #HTTP日志
        #输出开始        
        #解析视频ID
        try:
            tDName=self.request.uri[len(r'/'+web_xDisplay+r':'):].split('?')[0]
            tDName=xhlib.str_trim(tDName)
        except:
            tDName = '';
            Setlog('DName is Error : '+str(self.request),log_httplog)
            self.redirect('http://'+self.request.headers['Host']+Url_Message+'?MID=ERROR.001')
            return            
        #输出视频名称为空
        if tDName=='' :
            #要获取的视频名称为空，无法连接！
            Setlog('DName is Null : '+str(self.request),log_httplog)
            if sys_echoerror==True:
                self.redirect('http://'+self.request.headers['Host']+Url_Message+'?MID=ERROR.002')
                return
            else:
                self.set_header('Connection', 'close')
                self.set_status(404)
                return
        #输出结束
        tMsg=GetUid(tDName,self.request.headers['Host'],str(sys_rtmpport),web_rtmproot)
        tUid=xhlib.str_guid()
        global sys_DidConfig
        sys_DidConfig=sys_DidConfig+'<'+tUid+'>'+tMsg+'</'+tUid+'>'
        self.redirect('http://'+self.request.headers['Host']+'/'+web_clientpage+'?uid='+tUid)        
        return
    
class App_ClientXml(tornado.web.RequestHandler):
    def get(self):
        stt = datetime.datetime.now()-datetime.timedelta(microseconds=1000)
        self.set_header('Server', sys_servicename)
        if sys_refreshsetup==True : LoadSysconfig() #是否即时更新配置
        if sys_log==True: Setlog(str(self.request),log_httplog) #HTTP日志
        #输出开始      
        try:
            tUID=self.get_argument("uid")
        except:
            tUID=''
            Setlog('UID is Error : '+str(self.request),log_httplog)            
            self.redirect('http://'+self.request.headers['Host']+Url_Message+'?MID=ERROR.010')
            return               
        #输出视频UID为空
        if tUID=='' :
            #要获取的视频名称为空，无法连接！
            Setlog('UID is Null : '+str(self.request),log_httplog)
            if sys_echoerror==True:
                self.redirect('http://'+self.request.headers['Host']+Url_Message+'?MID=ERROR.011')
                return
            else:
                self.set_header('Connection', 'close')
                self.set_status(404)
                return
        try:      
            global sys_DidConfig  
            tXML=GetMsg(sys_DidConfig,tUID)
        except:
            Setlog('UID is Error : '+str(self.request),log_httplog)            
            self.redirect('http://'+self.request.headers['Host']+Url_Message+'?MID=ERROR.010')
            return
        if tXML.split()=='' :
            Setlog('UIDXML is Null : '+str(self.request),log_httplog)
            self.redirect('http://'+self.request.headers['Host']+Url_Message+'?MID=ERROR.012')
            return                           
        #输出结束
        self.write(tXML)
        #输出结束
        self.write('<!-- Processing time ['+str((datetime.datetime.now()-stt).microseconds/1000/1000.00000000)+']-->')
        return
    
# tornado.web
application = tornado.web.Application([
                                       (Url_Root,      App_Root),        #根路径
                                       (Url_index,     App_Index),       #index路径
                                       (Url_Message,   App_Message),     #message路径
                                       (Url_xDisplay,  App_xDisplay),    #xDisplay路径
                                       (Url_ClientXml, App_ClientXml),   #xClientXml路径
                                       (r"/(.*)", tornado.web.StaticFileHandler,{'path':path_webroot}),                                       
                                       ],**settings) 

#=======================================================
#系统主程序开始
#-------------------------------------------------------
if __name__ == '__main__':
    #开始主程序
    print '-'*(len(sys_servicenamever)+20)
    print sys_servicenamever
    print '-'*(len(sys_servicenamever)+20)
    print 'Parameter(Default):'
    print '  [httpservice=1] [rtmpservice=1] [httpport=80] [rtmpport=1935]'    
    print '-'*(len(sys_servicenamever)+20)
    print '>>>'
    #RtmpLite Service Start
    if (sys_rtmpservice==True):
        import thread
        print sys_servicename+' (Rtmp) [ Port:'+str(sys_rtmpport)+' ] OK !'        
        thread.start_new_thread(StartRtmp,())    
    else:
        print sys_servicename+' (Rtmp) not Start [ Stop ] !'
    #XingHe Studio xDisplay Service Start
    if sys_httpservice==True:
        application.listen(sys_httpport) #Web服务监听端口
        print sys_servicename + ' (Http) [ Port:'+str(sys_httpport)+' ] OK !'
        tornado.ioloop.IOLoop.instance().start()
    else:
        print sys_servicename + ' (Http) not Start [ Stop ] !'                
#=======================================================
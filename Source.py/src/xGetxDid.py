#coding=UTF-8
# xDisplay Did Build Tools (xGetxDid) v5.05.20150603
# 星河创作室(XingHeStudio.com)
# Create by Stream.Wang 2012-09-22
# Modify by Stream.Wang 2015-06-03

import sys
import xhlib
outstr1='xDisplay Did Build Tools (xGetxDid) v5.05.20150603'

def Did_Encryption(inStr):
    #编码字符串
    #print 'Did_Encryption : '+inStr
    #Source
    outStr=inStr
    if outStr==None : outStr=''
    #print 'Source[%s]:%s\n' % (str(len(outStr)),outStr)
    
    #zlib
    import zlib
    outStr=zlib.compress(outStr)
    #print 'zlib[%s]:%s\n' % (str(len(outStr)), outStr)
    
    #base64
    import base64
    outStr=base64.b64encode(outStr)
    #print 'base64[%s]:%s\n' % (str(len(outStr)), outStr)
    
    #str2hex
    uinstr=xhlib.str_str2hex( outStr )
    outStr=uinstr.upper()
    #print 'Hex[%s]:%s\n' % (str(len(outStr)), outStr)
    
    #md5
    import hashlib
    md5outStr=hashlib.md5(outStr)
    md5Str=md5outStr.hexdigest().upper()
    #print 'md5[%s]:%s\n' % (str(len(md5Str)), md5Str)  

    #return
    outStr=md5Str[:16]+outStr+md5Str[16:]
    #print 'Enc Return[%s]:%s\n' % (str(len(outStr)), outStr)    
    return outStr

def Did_Decryption(inStr):
    #解码字符串
    #print 'Did_Decryption : '+inStr    
    #长度不够
    if len(inStr)<32+1:return ''
    
    #取数据md5
    outStr=inStr
    md5Str=outStr[:16]+outStr[len(inStr)-16:]
    outStr=outStr[16:len(inStr)-16]
    #print 'sha1[%s]:%s\n' % (str(len(sha1Str)), sha1Str)
    #print 'Source[%s]:%s\n' % (str(len(outStr)),outStr)
    
    #验证sha1
    import hashlib
    md5outStr=hashlib.md5(outStr)
    xmd5Str=md5outStr.hexdigest().upper()
    #print 'xmd5[%s]:%s\n' % (str(len(xsha1Str)), xsha1Str)
    #sha1验证错误
    if xmd5Str<>md5Str:return '' 
    #else:print 'md5 CHK ok !\n'
    
    #str2hex
    outStr=xhlib.str_hex2str(outStr)
    #print 'Hex[%s]:%s\n' % (str(len(outStr)), outStr)
    
    #base64
    import base64
    outStr=base64.b64decode(outStr)
    #print 'base64[%s]:%s\n' % (str(len(outStr)), outStr)
    
    #zlib
    import zlib
    outStr=zlib.decompress(outStr)
    #print 'zlib[%s]:%s\n' % (str(len(outStr)), outStr)

    #return
    #print 'Dec Return[%s]:%s\n' % (str(len(outStr)), outStr)    
    return outStr
           
#-------------------------------------------------------

#取是否输出参数 -o (有参数会有本地输出，无参数只显示Did的编码信息)
try:
    if  xhlib.str_trim(str(sys.argv[2])).lower()=='-o'.lower():
        Xoutput=True
    else:
        Xoutput=False
except:
    Xoutput=False
    
#输出版本信息
if Xoutput==True: print outstr1
outstr2='='*(len(outstr1)+2)
if Xoutput==True: print outstr2
#取Did参数
try:
    xDid = xhlib.str_trim( str(sys.argv[1]) )
except:
    xDid = '[ ERROR xDisplay ID ! ]'
#xDid=r'TestDid'
outstr3='xDisplay ID : '+xDid
#输出Did
if Xoutput==True: print outstr3
#输出编码后Did
if xDid<> '[ ERROR xDisplay ID ! ]' :
    outcode=Did_Encryption(xDid)
    outstr4='xDisplay StrLink : '+outcode
    if Xoutput==True: 
        print outstr4
    else:
        print outcode
else:
    outstr4=''
#输出编码后文件
if (outstr4<>'') and (Xoutput==True):
    CnfFile=xhlib.fil_changefileext(sys.argv[0],'.txt')
    xhlib.fil_str2file(outstr1+'\n'+outstr2+'\n'+outstr3+'\n'+outstr4+'\n', CnfFile)

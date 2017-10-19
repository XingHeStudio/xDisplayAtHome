#coding=UTF-8
# xDisplayAtHome Service v5.05.20150603
# 星河创作室(XingHeStudio.com)
# Create by Stream.Wang 2012-09-22
# Modify by Stream.Wang 2015-06-03

from distutils.core import setup
import sys
sys.path.append(r"s:\Project\xDisplayAtHome\Source.py\src")
sys.path.append(r"s:\Project\xDisplayAtHome\Other.libs\Rtmplite")
sys.path.append(r"s:\Development\Python\Pytnon.XHLib4P2\src")
sys.path.append(r"s:\Development\Python\Python.x86.v2.7.9\Lib\site-packages\pywin32_system32")
import py2exe

setup(
    version = "5.05",
    description = "xDisplayAtHome Service v5.05.20150603",
    name = r"xDisplayAtHome",
    options = {"py2exe": {"compressed": 1,
                          "optimize": 2,
                          "ascii": 0,
                          "bundle_files": 1}},
    zipfile = None,
    # targets to build
    console = [{"script": r"xDisplayAtHome.py", "icon_resources": [(1, r"xDisplayAtHome.ico")]} ]
    )




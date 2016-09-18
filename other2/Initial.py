#coding:utf-8
import SaveInfo
import SaveInfo_2

def start():
    SaveInfo.save(0,0,"关键字")
    SaveInfo.save(0,1,"总新闻数")
    SaveInfo_2.save2(0,0,'错误代码')
    SaveInfo_2.save2(0,1,'url')
    SaveInfo_2.save2(0,2,'在数据文件中的行数')
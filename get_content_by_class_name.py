# coding = utf-8
# author = colorfulsummer

import re
import urllib2
import chardet
import sys
import time
from bs4 import BeautifulSoup


#单个url抓取数据
def main_one(url,num,parameter):

    #判断URL是否可以打开
    try:
        fd = urllib2.urlopen(url)
        s = fd.read()
    except Exception,e:
        print '输入的url不能打开--',e
        #sys.exit()

    #获取网页编码
    charset_ = chardet.detect(s)
    charset = charset_['encoding']
    #charset为编码
    print charset

    
    #获取网页内容
    argument = []
    dtime = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    if charset == 'utf-8':
        soup = s
    elif charset == 'GB2312':
        soup = s
        soup = soup.decode('gb2312','ignore')
        soup = re.sub('charset=gb2312','charset=utf-8',soup,re.I)
        soup = soup.encode('utf-8','ignore')
    else:
        print '不知道的编码方式'
        sys.exit()

    try:
        soup = BeautifulSoup(soup,'html.parser')
        argument = parameter[:]
        for i in range(len(parameter)):
            argument[i] = soup.find(class_=parameter[i])
            argument[i] = argument[i].get_text(' ', strip=True)
        string = ' '.join(argument)

        infile = open(dtime+'.txt','a+')
        infile.writelines(url)
        infile.writelines(string.encode('utf-8'))
        infile.close()
    except Exception,e:
        print '不能获取到当前输入的class信息',e
        sys.exit()


#多个url抓取数据
def main_more(url,depth,num,parameter):

    while depth>0:
        depth = int(depth)
        depth -= 1
        url_ = url+str(depth)
        print url_

        #判断URL是否可以打开
        try:
            fd = urllib2.urlopen(url_)
            s = fd.read()
        except Exception,e:
            print '输入的url不能打开--',e
            #sys.exit()

        #获取网页编码
        charset_ = chardet.detect(s)
        charset = charset_['encoding']
        #charset为编码
        #print charset
       
        argument = parameter[:]
        #列表复制不能直接，直接等于修改其中一个列表另一个也会变化，因为指向的是同一个对象。
        dtime = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        if charset == 'utf-8':
            soup = s
        elif charset == 'GB2312':
            soup = s
            soup = soup.decode('gb2312','ignore')
            soup = re.sub('charset=gb2312','charset=utf-8',soup,re.I)
            soup = soup.encode('utf-8','ignore')
        else:
            print '不知道的编码方式'
            sys.exit()

        try:
            soup = BeautifulSoup(soup,'html.parser')
            
            for i in range(len(parameter)):
                argument[i] = soup.find(class_=parameter[i])
                argument[i] = argument[i].get_text(' ', strip=True)
            string = ' '.join(argument)
            print string

            infile = open(dtime+'.txt','a+')
            infile.writelines(url_)
            infile.writelines(string.encode('utf-8'))
            infile.close()
        except Exception,e:
            print '不能获取到当前输入的class信息',e
            #sys.exit()




if __name__ == '__main__':
    choice = raw_input('单个url还是多个url?\n')

    if choice.isdigit()==False or len(choice)!=1:
        print '输入的格式有误'
        sys.exit()


    if int(choice)==1:
        argv = raw_input('输入url+num+class\n')
        try:
            argv = argv.split(' ')
            url = argv[0]
            num = argv[1]
            parameter = argv[2:]
            length = len(parameter)
            main_one(url,num,parameter)
        except Exception,e:
            print '输入单个url参数时出错--',e
    elif int(choice)==2:
        argv = raw_input('输入url+depth+num+class\n')
        try:
            argv = argv.split(' ')
            url = argv[0]
            depth = argv[1]
            num = argv[2]
            parameter = argv[3:]
            length = len(parameter)
            main_more(url,depth,num,parameter)
        except Exception,e:
            print '输入多个url参数时出错--',e
    else:
        print '---------------------'
        sys.exit()

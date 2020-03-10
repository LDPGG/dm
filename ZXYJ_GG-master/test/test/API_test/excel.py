#coding=utf-8
'''''
Created on 2016年1月22日
@author: cf
'''
import xlwt
workbook=xlwt.Workbook(encoding='utf-8')
booksheet=workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)
DATA=(('学号','姓名','年龄','性别','成绩'),
      ('1001','A','11','男','12'),
      ('1002','B','12','女','22'),
      ('1003','C','13','女','32'),
      ('1004','D','14','男','52'),
      )
for i,row in enumerate(DATA):
    for j,col in enumerate(row):
        booksheet.write(i,j,col)
workbook.save(r'C:\Users\duan\Desktop\grade.xls')



# from pyExcelerator import *
# import os
# currentpath = os.getcwd()
# testlog = open('test.mak','w')
# os.mkdir(r'Excel')
# print "currentpath: ",currentpath
# for file in os.listdir(currentpath):
#     if os.path.isfile(os.path.join(currentpath,file))==True:
#
# if file.find('.txt')>0:  //如果是别的格式直接将下面的.txt改为你所需要的格式后缀就可以了
# file_ = open(file,'r')
# content = file_.read()
# file_.close()
# testlog.write( content )
# print 1
# os.popen('log_parse.exe test.mak >> shuju.log')
# print 2
# for _file in os.listdir(currentpath):
# if os.path.isfile(os.path.join(currentpath,_file))==True:
# if _file.find('.log')>0:
work = Workbook()
works = work.add_sheet('Sheet1')
print 3
file_object = open(_file)
for i in range(0,2):
works.col(i).width = 10000
i = 0
for line in file_object:
line = line.rstrip('\n')
print 4
if not line.split():
i = i + 1
if line.strip():
array = line.split(':')
lineleft = array[0]
lineright = array[1]
works.write(i,0,lineleft)
works.write(i,1,lineright)
i = i + 1
_file = _file.rstrip('.log')
_file = 'Excel\%s.xls' % _file
work.save(_file)
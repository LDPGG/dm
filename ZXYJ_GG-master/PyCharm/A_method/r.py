import xlwt
from xlutils.copy import copy
import xlrd

def a():
    # 只能写不能读
    stus = [['姓名', '年龄', '性别', '分数'],
            [qq, 20, '女', 89.9]
            ]
    book = xlwt.Workbook()  # 新建一个excel
    sheet = book.add_sheet('case1_sheet')  # 添加一个sheet页
    row = 0  # 控制行
    for stu in stus:
        col = 0  # 控制列
        for s in stu:  # 再循环里面list的值，每一列
            print('-------------------------------------')
            sheet.write(row, col, s)
            col += 1
        row += 1
    # book.save('stu_1.xls')  # 保存到当前目录下
# a()

def b():
    # 只能读不能写
    book = xlrd.open_workbook('stu_1.xls')  # 打开一个excel
    sheet = book.sheet_by_index(0)  # 根据顺序获取sheet
    sheet2 = book.sheet_by_name('case1_sheet')  # 根据sheet页名字获取sheet
    print(sheet.ncols)  # 获取excel里面有多少列
    print(sheet.nrows)  # 获取excel里面有多少行
    print(sheet.get_rows())#
    for i in sheet.get_rows():
        print(i)  # 获取每一行的数据
    print('----------------------------------')
    for i in range(sheet.nrows):  # 0 1 2 3 4 5
        print(sheet.row_values(i))  # 获取第几行的数据

    for i in range(sheet.ncols):
        print(sheet.col_values(i))  # 获取第几列的数据


def c():
    # xlutils:修改excel
    book1 = xlrd.open_workbook('stu_1.xls')
    book2 = copy(book1)  # 拷贝一份原来的excel
    # print(dir(book2))
    sheet = book2.get_sheet(0)  # 获取第几个sheet页，book2现在的是xlutils里的方法，不是xlrd的
    sheet.write(1, 3, 0)
    sheet.write(1, 0, 'hello')
    book2.save('stu.xls')

c()

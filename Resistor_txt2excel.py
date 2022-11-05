'''
在第31行修改你的txt文件名(或者就将原始数据文件重命名为test.txt)
输出文件默认名称为test.xls
需要安装xlwt库
'''

import xlwt


def txt_xls(filename, xlsname):
    try:
        f = open(filename)
        xls = xlwt.Workbook()
        # 生成excel的方法，声明excel
        sheet = xls.add_sheet('sheet1', cell_overwrite_ok=True)
        x = 0
        while True:
            # 按行循环，读取文本文件
            line = f.readline()
            if not line:
                break  # 如果没有内容，则退出循环
            for i in range(len(line.split('\t'))):
                item = line.split('\t')[i]
                sheet.write(x, i, item)  # x单元格经度，i 单元格纬度
            x += 1  # excel另起一行
        f.close()
        xls.save(xlsname)  # 保存xls文件
    except:
        raise


if __name__ == "__main__":
    filename = "./test.txt"
    xlsname = "./test.xls"
    txt_xls(filename, xlsname)

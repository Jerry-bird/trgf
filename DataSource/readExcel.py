import os

from xlrd import open_workbook

from Conf import getpathInfo

path = getpathInfo.get_path()

#print(path)


class readExcel():
    def get_xls(self, xls_name, sheet_name):
        cls = []
        xlspath = os.path.join(path, 'excel', xls_name)
        #print(xlspath)
        file = open_workbook(xlspath)
        sheet = file.sheet_by_name(sheet_name)
        nrows = sheet.nrows
        for i in range(nrows):
            if sheet.row_values(i)[0] != u'case_name':
                cls.append(sheet.row_values(i))
        return cls


if __name__ == '__main__':
    print(readExcel().get_xls('personinfo.xls', 'Sheet1'))
    print(readExcel().get_xls('personinfo.xls', 'Sheet1')[1][1])

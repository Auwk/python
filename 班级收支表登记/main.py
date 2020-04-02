import dq
import fileinput
def sr():
    a=input('1.收入,2.支出')
        if a == '1':
            b1 = input('输入收入组成')
            c1 = input('输入收入来源')
            d = input('输入收入总数')
            return a,b1,c1，d
        if a == '2':
            b2 = input('输入支出金额')
            c2 = input('输入支出用途')
            return a,b2,c2

fname = '机器人班费收支情况.xlsx'
def xr():
    with fileinput.input(fname) as lines:


                                #f.write(name[-2:]+'\t'+name[:-2]+'\n')

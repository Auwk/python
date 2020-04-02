import fileinput
def demo_fileinput():
    with fileinput.input(['D:\Documents\Desktop\lc.txt','D:\Documents\Desktop\lt.txt']) as lines:
        for line in lines:
            print('总第%d行，'%fileinput.lineno(),'文件%s中第%d行：'
                  %(fileinput.filename(),fileinput.filelineno()))
            print(line.strip())

demo_fileinput()

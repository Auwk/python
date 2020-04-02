import os
#os.mkdir('test2')               #当前目录下创建文件test2
#print(os.listdir('D:\Documents\Desktop\python'))   #显示文件目录中的所有文件
#os.rmdir('D:\Documents\Desktop\AA')               #删除文件，该目录必须存在且为空
#print('目录：',os.path.isdir('yinyong'))        #检查某文件是否为目录
#print('文件：',os.path.isfile('D:\Documents\Desktop\lc.txt')) #检测对应目录的文件是否存在
for i in os.walk('D:\Documents\Desktop\python\yinyong'):    #遍历目录下所有文件及及目录及子目录中文件
    print(i)


#print(os.listdir('D:\Documents\Desktop\python'))




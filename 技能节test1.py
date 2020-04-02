import Serial
import xlwt

ser=serial.Serial(5,9600,timeout=0.5)
ser.open()
s = ser.read(10)#从端口读10个字节
ser.baudrate = 9600 #设置波特率
print(s)
ser.close()#关闭端口
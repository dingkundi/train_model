import os
import re
from openpyxl import Workbook
import pandas as pd

wb = Workbook()
# grab the active worksheet
ws = wb.active
ws.append(["A", "B","C",'E','F','F1','G1',"H10", "I1","J1",'K1','L1','M1','N1',"O1", "P1","Q1",'R1','S1','T1','U1','V1','W1','X1','DATE','TIME'])


def read_file(filename):
    with open(filename, 'a+') as fr:
        fr.seek(0)  # 移动文件指针
        content = fr.read()  # content 类型是字符串
        return content #返回聊天内容
def write_file(filename, content):
    #用来读取文件内容的
    with open(filename, 'a+') as fw:
        fw.write(str(content))

path = os.getcwd()
data_path = path+"/data/"
files_name = os.listdir(data_path)
for file_name in files_name:
    file_name = './data/'+file_name
    content = read_file(file_name)
    write_file('data.txt',content)


details = read_file('data.txt')
pattern = re.compile('(.*?)\n(.*?)\n(.*?)\n(.*?)\n(.*?)\n(.*?)\n(.*?)\n(.*?)\n(.*?)\n(.*?)\n(.*?)\n(.*?)\n(.*?)\n(.*?)\n(.*?)\n(.*?)\n(.*?)\n(.*?)\n(.*?)\n(.*?)\n(.*?)\n(.*?)\n(.*?)\n(.*?)\n(.*?)\n(.*?)\n99999.000\n', re.S)
items = re.findall(pattern, details)
for item in items:
    #print(item)
    a = item[0]
    b = item[1]
    c = item[2]
    d = item[3]
    e = item[4]
    f = item[5]
    g = item[6]
    h = item[7]
    i = item[8]
    j = item[9]
    k = item[10]
    l = item[11]
    m = item[12]
    n = item[13]
    o = item[14]
    p = item[15]
    q = item[16]
    r = item[17]
    s = item[18]
    t = item[19]
    u = item[20]
    v = item[21]
    w = item[22]
    x = item[23]
    y = item[24]
    z = item[25]
    ws.append([a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q,r,s,t,u,v,w,x,y,z])
wb.save("result.xlsx")












































































































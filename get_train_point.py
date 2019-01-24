#-*-conding:utf-8-*-
def get_trains_point(filename):
    import pandas as pd
    import os
    import re
    #创建一个用来存放迁移积分的文件
    fp = open('test.txt', 'w')
    #在第一行添加一系列数据，作为行号
    add_line = "sed -i '1i 1 2 3 4 5 6 7 8' {}".format(filename)
    os.system(add_line)
    #读迁移积分所计算的数据，并得到迁移积分TP
    fd = pd.read_table(filename, delim_whitespace=True)
    TP =  fd.iloc[[3],[5]]
    TP = abs(TP.iloc[0][0])
    #得到两个单体的名称
    frag = re.findall(r"[A-Z]+\d+", filename)
    #将数据写入文件
    print >> fp, "%s\t%s\t%.6f" %(frag[0], frag[1], TP)
    fp.close()
    #删除所添加的第一行
    del_line = "sed -i '1d' {}".format(filename)
    os.system(del_line)
    return 0

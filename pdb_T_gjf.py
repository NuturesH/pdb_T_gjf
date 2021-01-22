#-*-coding:utf-8-*-
# lasted edited by ys_song, 2021-1-22
class PDB_T_GJF:
    #初始化数据
    def __init__(self, filename):
        self.filename = filename
        #print(filename)
    #设定坐标转换函数
    def PDB_Coord(self):
        import pandas as pd
        import os
        #生成一个副本文件
        filename = self.filename + ".swap"
        cp_swap_f = "cp {} {}".format(self.filename, filename)
        os.system(cp_swap_f)
        #删除由VMD所所产生的格式，行首和行尾
        del_header_tail = "sed -i '1d' {0} && sed -i '$d' {0}".format(filename)
        os.system(del_header_tail)
        #添加MG原子
        add_mg = "sed -i '/MG/ s/$/MG/g' {0}".format(filename)
        os.system(add_mg)
        #用pandas读取修改过后的pdb文件
        pf = pd.read_table(filename, header=None, delim_whitespace=True)
        #设置gjf和coord以及chk名称
        coord_fname = filename.replace('pdb.swap', 'coord') #coord 名称
        gjf_fname = filename.replace('pdb.swap', 'gjf') #gjf 名称
        chk_fname = filename.replace('pdb.swap', '').replace('/', '\/') #chk 名称，后期shell脚本需要调用
        #pandas 格式化输出浮点数
        pf = pf.round(3)
        # change the column index here by ys_song
        pf.to_csv(coord_fname, sep='\t', index=False, header=False, columns=[10, 5, 6, 7])
        #整合模板文件和坐标文件,生成完整的gjf文件
        complete_gjf = "cat {0} {1} > {2}".format('mod.gjf', coord_fname, gjf_fname)
        os.system(complete_gjf)
        #最终修改文件，关于chk部分
        replace_chk = "sed -i 's/mod/{0}/g' {1}".format(chk_fname, gjf_fname)
        # add it to os.system by ys_song
        os.system(replace_chk)
        #gjf 文件尾部增加一行
        add_last_line = "echo ' ' >> {}".format(gjf_fname)
        os.system(add_last_line)
        #删除副本文件
        rm_swap_f = "rm {}".format(filename)
        os.system(rm_swap_f)
        return 0

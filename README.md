# pdb_T_gjf
pdb file trans gjf file
# get train point 
get train point from frontier.dat
# get train point
文件包含一个函数，给予这个函数一个需要处理的文件，会得到其中的迁移积分，将利用bioparc命令所生成的文件，从中提取出所需要的迁移积分，三行五列
# pdb_T_gjf 
文件中包含一个类，给予这个类需要处理的文件名称，之后用两个函数进行处理。
  函数PDB_Coord第一步将vmd所生成的pdb文件转化为原子名称加坐标的形式。 
                第二步将所生成的坐标文件加上g16命令的模板文件生成初始的gjf文件
                第三步将所生成的gjf文件进行修改，修改其中chk文件的路径及名称

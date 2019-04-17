#!-*-coding:utf-8-*-
import numpy as np
import os
import re
class E_COUP:
    def __init__(self, INF1, INF2):
        self.INF1 = INF1
        self.INF2 = INF2
    #求文件中的偶极矩
    def coup(self,INF ):
        import re
        import os
        INF = INF + ".log"
	order = "grep -C 2 'electric dipole moments' %s" %(INF)
        #print order 
        values = os.popen(order).read()
        #print values
        EDM = values.split('\n')[4]
        vec = re.findall(r"-?\d+\.\d+", EDM)[0:3]
        vec_i = np.array([float(i) for i in vec])
        return vec_i
    #求原子坐标
    def coor(self, INF, ATOM):
        INF = INF + ".pdb"
        order = "grep '%s' %s" %(ATOM, INF)
        line = os.popen(order).read()
        line_one = line.split("\n")[0]
        coord_c = re.findall(r"-?\d+\.\d+", line_one)[0:3]
        coord = np.array([float(i) for i in coord_c])
        return coord
    #求MG 向量， N2,N4向量
    def vec(self, INF1, INF2):
        import numpy as np
        #INF1 = self.INF1
        #INF2 = self.INF2
        #文件1中的MG 、N2、N4
        MG_i = self.coor(INF1, "MG")
        ND_2_i = self.coor(INF1, "ND")
        NB_4_i = self.coor(INF1, "NB")
        #文件2中的MG、N2、N4
        MG_j = self.coor(INF2, "MG")
        ND_2_j = self.coor(INF2, "ND")
        NB_4_j = self.coor(INF2, "NB")
        #求MG向量， N2到N4的向量
        MG_ij = np.array([(MG_j[k]-MG_i[k])/0.529177 for k in range(3)])
        N_i = np.array([(NB_4_i[k]-ND_2_i[k])/0.529177 for k in range(3)])
        N_j = np.array([(NB_4_j[k]-ND_2_j[k])/0.527177 for k in range(3)])
        #归一化MG向量
        nom_MG = np.linalg.norm(MG_ij)
        #print nom_MG
        ZH = []
        for i in range(3):
             k = MG_ij[i]/nom_MG
             ZH.append(k)
        MG_ij_norm =  np.array(ZH)
        #ZH = [(MG_ij[k]/nom_MG for k in range(3))]
        #print ZH 
        return MG_ij,MG_ij_norm, N_i, N_j
    #得到激发能的值
    def Excited_values(self):
        import re
        INF = self.INF1 + ".log"
        #print INF
        order = "grep 'Excited State   1' %s" %(INF)
        #print order
        line = os.popen(order).read()
        #print line
        values = 8065.4941275*float(re.findall(r"-?\d+\.\d+", line)[0])
        vector = self.coup(self.INF1)
        return values,vector
        
    #根据公式来开始计算
    def coup_values(self):
        import numpy as np
        INF1 = self.INF1
        INF2 = self.INF2
        Rij,Rij_norm, Ni, Nj = self.vec(INF1,INF2)
        ui = self.coup(INF1)
        uj = self.coup(INF2)
        
        if np.dot(Ni, ui) < 0:
             neg_ui = [-k for k in ui]
             ui = np.array(neg_ui)
        if np.dot(Nj, uj) < 0:
             neg_uj = [-k for k in uj]
             uj = np.array(neg_uj)
        
        #print np.dot(ui,uj)
        #print np.linalg.norm(Rij)
        Cij = 219475*((np.dot(ui, uj) - 3*np.dot(ui, Rij_norm)*np.dot(uj, Rij_norm))/np.linalg.norm(Rij)**3)
        print Cij
        return Cij

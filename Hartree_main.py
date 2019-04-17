from coupling import E_COUP
import sys
import numpy as np
import pandas as pd
# read filename to list
filename = sys.argv[1]
print filename
Fname = [i.strip() for i in open(filename)]
# restruct 27*27 hartree matrix
diople_matrix = np.array([])
hartree_matrix = np.array([])
for i in Fname:
    for j in Fname:
        print i, j
        func = E_COUP(i,j)
        #add hartree and diople
        if i == j:
            hartree, diople = func.Excited_values()
            hartree_matrix = np.append(hartree_matrix, hartree)
            diople_matrix = np.append(diople_matrix, diople)
            #Vector.append(Vec.tolist())
       # add hartree
        else:
            hartree = func.coup_values()
            #print Val
            hartree_matrix = np.append(hartree_matrix, hartree) 
            #Values.append(Val)
#Values = np.array(Values)
#Vector = np.array(Vector)
# transfrom (, -1) to (27 *27)
dimensions = len(Fname)
#print diople_matrix
hartree_matrix = hartree_matrix.reshape(dimensions,dimensions)
diople_matrix = diople_matrix.reshape(dimensions, 3)
# get feature_val and feature_vex
feature_val, feature_vec = np.linalg.eig(hartree_matrix)
#restruct new diople matrix
new_diople_matrix = np.dot(feature_vec, diople_matrix)
#get new diople matrix norm**2
diople_norm = np.array([np.linalg.norm(i)**2 for i in new_diople_matrix]).reshape(dimensions, 1)
#diople_norm = diople_norm.reshape()
#charge data struct
new_diople_matrix = pd.DataFrame(np.hstack((new_diople_matrix, diople_norm)))
diople_matrix = pd.DataFrame(diople_matrix)
hartree_matrix = pd.DataFrame(hartree_matrix)
feature_vec = pd.DataFrame(feature_vec)
#charge column name
new_diople_matrix.rename(columns={0:'X', 1:'Y', 2:'Z', 3:'norm*2'} , inplace=True)
diople_matrix.rename(columns={0:'X', 1:'Y', 2:'Z'}, inplace=True)
with pd.ExcelWriter("Result.xlsx") as writer:
    diople_matrix.to_excel(writer, sheet_name = 'diople')
    hartree_matrix.to_excel(writer, sheet_name = 'hartree')
    feature_vec.to_excel(writer, sheet_name = 'FreactureVec')
    new_diople_matrix.to_excel(writer, sheet_name = ' new_diople')
#np.savetxt("eig.csv", Eig_vc, delimiter = ',')
#np.savetxt("New_Diople.csv", new_Dipole_vc, delimiter =',')
#print Values, Vector

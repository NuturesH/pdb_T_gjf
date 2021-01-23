# lasted edited by ys_song, 2021-1-22
# work with pdb_T_gjf.py file
import pdb_T_gjf as pg
for i in range(0,20):
    print(i)
    filename = "molx_" + str(i) + ".pdb"
    aa = pg.PDB_T_GJF(filename)
    aa.PDB_Coord()

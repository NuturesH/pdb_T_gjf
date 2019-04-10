class FC：
    def __init__(self, filename):
	    self.filename = filename
	def LFC(self):
		import os
		name = self.filename.split(".pdb")[0]
                resname = "".join(list(name)[-1].lowder())
		one = "antechamber -i {0}.pdb -fi pdb -o {0}.mol2 -fo mol2 -c bcc -s 2".format(name)
		os.system(one)
		two = "parmchk -i {0}.mol2 -f mol2 -o {0}.frcmod".format(name)
		os.system(two)
		fp = open("mod.tleap", 'w')
		print >> fp, "tleap -f oldff/leaprc.ff99SB"
		print >> fp, "source leaprc.gaff"
		print >> fp, "{0} = loadmol2 {1}.mol2".format(resname, name)
		print >> fp, "check {}".format(resname)
		print >> fp, "loadamberparams {}.frcmod".format(name)
		print >> fp, "saveoff {} {}.lib".format(resname, name)
		print >> fp, "quit"
		fp.close()
		three = "tleap -f mod.tleap"
		os.system(three)
		return 0

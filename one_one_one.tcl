mol new 2fkw_C_R.pdb
set j 502
set pro [atomselect top "same residue as within 5 of resid $j"]
set resname1 BCL
echo $resname1
set residues [lsort -unique -integer [$pro get residue]]
foreach i $residues {
    set pros [atomselect top "resid $j or residue $i"]
    set resname2 [lsort -unique [[atomselect top "residue $i"] get resname]]
    echo $resname2
    mkdir $resname1$j\_$resname2$i
    $pros writepdb $resname1$j\_$resname2$i\/$resname1$j\_$resname2$i
}

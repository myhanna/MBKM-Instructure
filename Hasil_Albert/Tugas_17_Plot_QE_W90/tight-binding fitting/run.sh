#!/bin/bash

PW_COMMAND="/clusterfs/staff/myhanna/apps/qe-7.2/bin/pw.x"
W90_COMMAND="/clusterfs/staff/myhanna/apps/qe-7.2/W90/wannier90.x"
PW2W90_COMMAND="/clusterfs/staff/myhanna/apps/qe-7.2/bin/pw2wannier90.x"
POSTW90_COMMAND="/clusterfs/staff/myhanna/apps/qe-7.2/W90/postw90.x"

prefix="gr"

echo "scf calculation"
mpirun -np 4 $PW_COMMAND < $prefix.scf.in > $prefix.scf.out

echo "nscf calculation"
mpirun -np 4 $PW_COMMAND < $prefix.nscf.in > $prefix.nscf.out

echo "generate nnkp"
$W90_COMMAND -pp $prefix

echo "compute overlap"
mpirun -np 4 $PW2W90_COMMAND < $prefix.pw2wan.in > $prefix.pw2wan.out

echo "compute the MLWFs"
$W90_COMMAND $prefix

rm -rf ./work/
echo "JOB DONE (^_^)"

#!/bin/sh

f2py --fcompiler=gfortran --f90flags=-ffree-line-length-0 -m fortran -c fortran.f90 
cd ../day-1/
ln -s ../tools/fortran.cpython*so .
cd ../day-2/
ln -s ../tools/fortran.cpython*so .
cd ../tools/

#!/bin/sh

f2py --fcompiler=gfortran --f90flags=-ffree-line-length-0 -m fortran -c fortran.f90 
cd ../tutorial-1/
ln -s ../tools/fortran.cpython*so .
cd ../tutorial-2/
ln -s ../tools/fortran.cpython*so .
cd ../tutorial-3/
ln -s ../tools/fortran.cpython*so .
cd ../tutorial-4/
ln -s ../tools/fortran.cpython*so .
cd ../tools/

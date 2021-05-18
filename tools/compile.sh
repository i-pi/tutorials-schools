#!/bin/sh

f2py --fcompiler=gfortran --f90flags=-ffree-line-length-0 -m fortran -c fortran.f90 
cp fortran.cpython*so ../tutorial-1 
cp fortran.cpython*so ../tutorial-2 

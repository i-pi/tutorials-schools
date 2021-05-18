#!/bin/sh

f2py --fcompiler=gfortran --f90flags=-ffree-line-length-0 -m fortran -c fortran.f90 
cp fortran.cpython*so ../day-1 

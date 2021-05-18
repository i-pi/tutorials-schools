units		electron
atom_style	full

# Since one can only use Ewald with triclinic boxes, 
# and there is no TIP4P/Ewald in LAMMPS, this potential
# is not exactly QTIP4P/f. Do **NOT** use this example
# as a template for anything serious!
pair_style	    lj/cut/coul/long 17.01
bond_style      class2 
angle_style     harmonic
kspace_style	ewald 0.0001

read_data	data.ice
pair_coeff  * * 0 0
pair_coeff  1  1  0.000295147 5.96946

neighbor	2.0 bin

timestep	0.00025

fix 1 all ipi lammps_ice 32345 unix

run		100000000


<< test for run using reduced index file for comparison with test97 >>
MONITOR 1
LIBVERSION 0
GETXS 1 211
GETDECAY 1
FISPACT
* IRRADIATION OF Ti EEF 175 FW 1.0 MW/M2
<< -----set initial conditions----- >>
MASS 1.0 1
TI 100.0
MIND 1.E5
GRAPH 3 2 1 1 2 3
WALL 1.00
SORTDOM 10 10
UNCERT -1 0.01 0.02 10 3
ATOMS
HAZA
HALF
ATWO
DOSE 1
<< -----irradiation phase----- >>
TIME 2.5 YEARS
ATOMS
<< -----cooling phase----- >>
FLUX 0.
ZERO
TIME 1 MINS ATOMS
TIME 1 HOURS ATOMS
TIME 1 DAYS ATOMS
TIME 7 DAYS ATOMS
TIME 1 YEARS ATOMS
END
* END
/*

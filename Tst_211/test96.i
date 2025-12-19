<< -----get nuclear data----- >>
GETXS 0
GETDECAY 0
FISPACT
* Aluminium
<< -----set initial conditions----- >>
MASS 1.57E-05 1
Al 100.0
<<MIND 1.0>>
SPLIT 1
UNCERT 2
UNCTYPE 3
SORTDOM 10 5
FLUX 4.725E+08
ATOMS
HAZA
HALF
CLEAR
<< -----irradiation phase----- >>
TIME 600 ATOMS
<< -----cooling phase----- >>
FLUX 0.0
ZERO
TIME  123 ATOMS
TIME   29 ATOMS
TIME  154 ATOMS
TIME   30 ATOMS
TIME  269 ATOMS
TIME   30 ATOMS
TIME  271 ATOMS
TIME   30 ATOMS
END
* END

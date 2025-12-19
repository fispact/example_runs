<< -----get nuclear data----- >>
PROJ 3
GETXS 0
GETDECAY 0
FISPACT
* IRRADIATION OF Pb
<< -----set initial conditions----- >>
MASS 1.0 1
Pb 100.0
MIND 1.E5
GRAPH 5 2 1 1 2 3 4 5
FLUX 1.0E+13
ATOMS
HAZA
HALF
<< -----irradiation phase----- >>
TIME 1.0 YEARS
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



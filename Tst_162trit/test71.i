<< -----get nuclear data----- >>
GETXS 0
GETDECAY 0
FISPACT
* Flash radiography, fusion gamma
<< -----set initial conditions----- >>
MASS 1.0 1
Ti 100.0
MIND 1.E5
GRAPH 5 2 1 1 2 3 4 5
FLUX 1.00E+15
ATOMS
HAZA
HALF
ATWO
SORTDOMINANT 20 10
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


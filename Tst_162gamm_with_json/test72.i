<< -----get nuclear data----- >>
JSON
GETXS 0
GETDECAY 0
FISPACT
* Flash radiography, fusion gamma
<< -----set initial conditions----- >>
MASS 1.0 2
Fe 99.9999
U   0.0001
USEFISSION
MIND 1.E5
GRAPH 5 2 1 1 2 3 4 5
FLUX 1.00E+15
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
TIME 5000 YEARS ATOMS
END


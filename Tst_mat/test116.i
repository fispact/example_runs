<< -----get nuclear data----- >>
CLOBBER
GETXS 0
GETDECAY 0
ALLDIS 30
ATDISP 3 
Be 35.0 
C 34.0 Mg 24.5
FISPACT
* IRRADIATION OF TI 1.0 MW/M2
<< -----set initial conditions----- >>
MASS 1.0 1
Ti 100.0
DENSITY 19.254
MIND 1.E5
WALL 1.00
ATOMS
<< -----irradiation phase----- >>
HALF
HAZA
TAB1 42 
TAB2 43 
TAB3 44 
TAB4 45
BREM 4 Ar39 Ar42 K42 Cl38
TIME 2.5 YEARS
ATOMS
<< -----cooling phase----- >>
FLUX 0.
ZERO
NOT1 
NOT2  
NOT3 
NOT4
TIME 1.022 YEARS ATOMS
END
* END


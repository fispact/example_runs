<< -----get nuclear data----- >>
PROJ 2
NOERROR
GETXS 0
GETDECAY 0
FISPACT
* IRRADIATION OF TI by d, IFMIF
<< -----set initial conditions----- >>
MASS 1.0 1
Ti 100.0
DENSITY 19.254
MIND 1.E5
FLUX 1.0E14
UNCERT 3
ATOMS
HALF
<< -----irradiation phase----- >>
TIME 1.0 YEARS
ATOMS
<< -----cooling phase----- >>
FLUX 0.0
ZERO
TIME 10.0 YEARS ATOMS
END
* END


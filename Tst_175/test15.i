<< -----get nuclear data----- >>
LIBVERSION 0
GETXS 0
GETDECAY 0
FISPACT
* IRRADIATION OF Ti EEF 175 FW 1.0 MW/M2
<< -----set initial conditions----- >>
MASS 1.0 1
Ti 100.0
MIND 1.E5
WALL 1.00
UNCERT 3
ATOMS
HAZA
HALF
ATWO
<< Test case for comment >>
GENERIC 0
DOSE 1
<< -----irradiation phase----- >>
TIME 2.5 YEARS
ATOMS
<< -----cooling phase----- >>
FLUX 0.
ZERO
TIME 1 MINS ATOMS
TIME 1 HOURS ATOMS
TIME << Test case for comment >> 1 DAYS ATOMS
TIME 7 DAYS ATOMS
TIME 1 YEARS ATOMS
END
* END


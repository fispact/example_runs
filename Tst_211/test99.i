<< -----get nuclear data----- >>
GETXS 0
GETDECAY 0
FISPACT
* IRRADIATION OF Ti EEF 175 FW 1.0 MW/M2
<< -----set initial conditions----- >>
MASS 1.0 1
Ti 100.0
TOLER 0 1.0E-1 1.0E-9
TOLER 1 1.0E-1 1.0E-9
WALL 1.00
MIND 1.0E-5
UNCERT 3
SORTDOM 10 5
ATOMS
HAZA
HALF
ATWO
DOSE 1
<< 
-----irradiation phase----- 
irradiation split into 2 steps
to check pathways and
sensitivity for multiple irradiation
step (c.f., results of test86)
>>
TIME 2.0 YEARS
SPECTRUM
TIME 0.5 YEARS ATOMS
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

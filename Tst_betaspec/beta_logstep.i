<< -----collapse cross section data----- >>
CLOBBER
MONITOR 1
SPEK
GETXS 1 709
<< -----condense decay data----- >>
GETDECAY 1
<< -----set initial conditions and get nuclear data----- >>
FISPACT
* irradiate steel
BETASPEC 0
<< ----- steel composition ----- >>
DENSITY 4.0
FUEL 3
H3 5.613E20
CO60 2.4E16
C14 2.612E22
<< -----other initialisation options----- >>
MIND 1.0E5
ATOMS
FLUX 0.0
TIME 1 YEAR ATOMS
END
* END
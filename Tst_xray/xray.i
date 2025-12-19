<< -----collapse cross section data----- >>
CLOBBER
MONITOR 1
SPEK
GETXS 1 709
<< -----condense decay data----- >>
SAVELINES
GETDECAY 1
<< -----set initial conditions and get nuclear data----- >>
FISPACT
* irradiate steel
<< ----- steel composition ----- >>
DENSITY 10.0
FUEL 1
CO60 1E20
<< -----other initialisation options----- >>
MIND 1.0E5
HAZARDS
HALF
TAB4 77
<< -----irradiation phase----- >>
SPECTRUM
FLUX 4.51E13
TIME 24 HOURS
SPECTRUM
FLUX 0.0
TIME 30 DAYS 
SPECTRUM
FLUX 1.51E11
TIME 1 YEARS                      
SPECTRUM
END
* END

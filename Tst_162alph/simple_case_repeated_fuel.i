<< -----set initial switches and get nuclear data----- >>
CLOBBER
GETXS 0
GETDECAY 0
FISPACT
* Fe simulation
DENSITY 1.0 
FUEL 4
U235 1.0E24
U238 1.0E24
U235 1.0E24
U238 1.0E24
<< -----irradiation phase----- >>
FLUX 1.0E+10
ATOMS
TIME 7 HOURS
ATOMS
END
* END
/*

<< -----get nuclear data----- >>
CLOBBER
LIBVERSION 0
GETXS 0
GETDECAY 0
FISPACT
* 1 PPM OF CO IN FE EEF FW 1.0 MW/M2

<< -----set initial conditions----- >>
MASS 1.0 2 
Fe 99.9999 
Co  0.0001
MIND 1.E5
WALL 1
ATOMS
UNCERT 3

<< -----irradiation phase----- >>
TIME 2.5 YEARS
ATOMS

<< -----cooling phase----- >>
FLUX 0.
ZERO
TIME 0.1 YEARS ATOMS
TIME 0.9 YEARS ATOMS
END
* END


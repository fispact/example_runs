<< ---prepare collapsed cross section and condensed decay data. 
The crossec crossunc and fluxes (or arb_flux) files are used from the
files file in the order in which they appear. See files.test60 ---->>
LIBVERSION 0
MONITOR 1
GETXS 1 69 << first collapse >>
SPEK
GETDECAY 1 << condense decay data >>
FISPACT
* THREE COLLAPSES AND CONDENSE
GETXS 1 69 << second collapse >>
GETXS 1 69 << third collapse >>
END
* END OF COLLAPSE

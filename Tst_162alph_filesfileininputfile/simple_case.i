<< FILES
# gamma attenuation data
absorp  ../../nuclear_data/decay/abs_2012

# index of nuclides to be included
ind_nuc  ../../nuclear_data/TENDL2017data/tendl17_decay12_index

# Library cross section data
enbins ../../nuclear_data/ebins/ebins_162
xs_endf ../../nuclear_data/TENDL2017data/tal2017-a/gxs-162

# Binary cross section data
xs_endfb ../../nuclear_data/bin/tal2017-a.bin

# Library probability tables for self-shielding
prob_tab  ../../nuclear_data/TENDL2017data/tal2017-n/tp-709-294

# fluxes
fluxes  fluxes
arb_flux  spectra

# Library decay data
dk_endf ../../nuclear_data/decay/decay_2012

# Library fission  data
fy_endf ../../nuclear_data/UKFY41data/ukfy4_1a

# Spontaneous fission data
sf_endf ../../nuclear_data/GEFY61data/gefy61_sfy

# Library regulatory data
hazards ../../nuclear_data/decay/hazards_2012
clear   ../../nuclear_data/decay/clear_2012
a2data  ../../nuclear_data/decay/a2_2012

# collapsed cross section data (in and out)
collapxi  COLLAPX
collapxo  COLLAPX

# condensed decay and fission data (in and out)
arrayx  ARRAYX
>>

<< -----set initial switches and get nuclear data----- >>
CLOBBER
GETXS 1 1
GETDECAY 1
SPEK
PROJ 4
FISPACT
* Fe simulation
DENSITY 1.0 
FUEL 2
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

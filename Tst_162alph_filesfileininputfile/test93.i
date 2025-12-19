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

<< -----get nuclear data----- >>
GETXS 0
GETDECAY 0
FISPACT
*PWR FUEL 3.1% U235 FBR-Na End of Cycle
<< -----set initial conditions----- >>
DENSITY 10.1
FUEL 2
U235 7.948E22
U238 2.453E24
USEFIS
MIND 1.E5
HAZA
HALF
GRAPH 5 2 1 1 2 3 4 5
FLUX 3.34E+10
ATOMS
ATWO
DOSE 1
<< -----irradiation phase----- >>
TIME 30.4375 DAYS
TAB1 41
ATOMS
TIME 60.875 DAYS
ATOMS
TIME 91.3125 DAYS
ATOMS
TIME 182.625 DAYS
ATOMS
TIME 182.625 DAYS
ATOMS
TIME 182.625 DAYS
ATOMS
<< -----cooling phase----- >>
FLUX 0.
ZERO
NOSTABLE
TIME 60
ATOMS
TIME 1 DAYS ATOMS
TIME 29.4375 DAYS ATOMS
TIME 152.1875 DAYS ATOMS
TIME 182.625 DAYS ATOMS
TIME 2 YEARS ATOMS
TIME 2 YEARS ATOMS
TIME 5 YEARS ATOMS
END
* END

